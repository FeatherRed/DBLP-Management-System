import pickle
import re
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import create

class Allindex:
    def __init__(self,author_to_title,title_to_info,buckets,edge_author,top_n_keywords,inverted_index):
        self.author_to_title = author_to_title
        self.title_to_info = title_to_info
        self.buckets = buckets
        self.edge_author = edge_author
        self.top_n_keywords = top_n_keywords
        self.inverted_index = inverted_index
    def reset(self):
        return self.author_to_title,self.title_to_info,\
               self.buckets,self.edge_author,\
               self.top_n_keywords,self.inverted_index
def split_sentence(sentence):
    # 使用正则表达式匹配句子中的单词
    words = re.findall(r'\b\w+\b', sentence)
    return words

def build_index(data):#建立作者到标题、标题到内容的索引
    type_name = ["article", "book", "www", "inproceedings", "mastersthesis", "incollection", "proceedings", "phdthesis"]
    edge_author0 = defaultdict(list)
    edge_author = defaultdict(list)
    author_to_titles = defaultdict(list)
    title_to_info = defaultdict(list)
    for tname in type_name:
        for publication in data[tname]:
            if "title" in publication:
                title = publication["title"]
            else:
                if "booktitle" in publication:
                    title = publication["booktitle"]
                else:
                    title = ""
            if "authors" in publication:
                authors = publication["authors"]
            else:
                if "editor" in publication:
                    authors = publication["editor"]
                else:
                    if "author" in publication:
                        authors = publication["author"]
                    else:
                        if "editors" in publication:
                            authors = publication["editors"]
                        else:
                            authors = []
            # 构建作者到文献标题的映射
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(publication)
                else:
                    author_to_titles[author] = [publication]
            # 构建文献标题到文献信息的映射
            if title in title_to_info:
                title_to_info[title].append(publication)
            else:
                title_to_info[title] = [publication]
            for author1 in authors:
                # if author1 not in edge_author:
                #    edge_author[author1] = []
                for author2 in authors:
                    if author2 == author1:
                        continue
                    #if author2 in edge_author[author1]:
                    #    continue
                    edge_author0[author1].append(author2)
    for author in edge_author0:
        cnt = defaultdict(int)
        for author2 in edge_author0[author]:
            if author2 in cnt:
                cnt[author2] += 1
            else:
                cnt[author2] = 1
        for author2 in cnt:
            edge_author[author].append((author2, cnt[author2]))
    buckets = [[] for _ in range(32767)]
    for author in author_to_titles:
        buckets[len(author_to_titles[author])].append(author)
    top_n_keywords, inverted_index = build_inverted_index(title_to_info)
    Index = Allindex(author_to_titles,title_to_info,buckets,edge_author,top_n_keywords,inverted_index)
    return Index

def print_pre_n_author(x,buckets):#输出最多的前n个作者
    cnt = 0

    for i in range(32766,0,-1):
        if len(buckets[i]) == 0:
            continue
        if cnt <= x:
            for author in buckets[i]:
                cnt += 1
                if cnt <= x:
                    print(f"{author}: {i} publications")
        else:
            break



def find_author(s, author_to_titles):#返回值为标题列表，文献详细信息列表
    titlelist = []
    publicationlist = []
    if s in author_to_titles:
        print("yes")
        for publication in author_to_titles[s]:
            if "title" in publication:
                title = publication["title"]
            else:
                if "booktitle" in publication:
                    title = publication["booktitle"]
                else:
                    title = ""
            titlelist.append(title)
            publicationlist.append(publication)
    return titlelist, publicationlist

def find_title(s, title_to_info):#返回值为文献详细信息列表
    publicationlist = []
    if s in title_to_info:
        for publication in title_to_info[s]:
            publicationlist.append(publication)
    return publicationlist

def keywords_search(query_words0, inverted_index, title_to_info):#返回值为标题列表，文献详细信息列表
    # 将用户输入的多个单词拆分成列表
    query_words = split_sentence(query_words0)
    # 初始化结果为 None
    result_titles = None
    for word in query_words:
        word = word.lower()
        if word in inverted_index:
            titles = set(inverted_index[word])
            # 如果结果为 None，将结果初始化为第一个单词的结果，否则取当前单词结果与之前结果的交集
            if result_titles is None:
                result_titles = titles
            else:
                result_titles = result_titles.intersection(titles)
    titlelist = []
    publicationlist = []
    for title in result_titles:
        for publication in title_to_info[title]:
            titlelist.append(title)
            publicationlist.append(publication)
    return titlelist, publicationlist

def top_keyword_per_year(year,top_n_keywords, num):#用于输出某年的词频
    cnt = 0
    keywords_list = []
    for keywords in top_n_keywords[year]:
        cnt = cnt + 1
        keywords_list.append(keywords)
        if cnt == num:
            return keywords_list
    return keywords_list

def count_matches(query_words, title):
    title = title.lower()
    title = split_sentence(title)
    cnt = 0
    for word in title:
        if word in query_words:
            cnt += 1
    return cnt

def fuzzy_search(query_words0, inverted_index, title_to_info):
    query_words0 = query_words0.lower()
    query_words = split_sentence(query_words0)
    result_titles = None
    titlelist = []
    publicationlist = []
    for word in query_words:
        if word in inverted_index:
            titles = set(inverted_index[word])
            # 如果结果为 None，将结果初始化为第一个单词的结果，否则取当前单词结果与之前结果的交集
            if result_titles is None:
                result_titles = titles
            else:
                result_titles = result_titles.union(titles)
    maxmatch = 30
    frequence_buckets = [[] for _ in range(maxmatch+1)]
    if result_titles is None:
        return titlelist, publicationlist
    for title in result_titles:
        frequence_buckets[count_matches(query_words, title)].append(title)
    for i in range(maxmatch,0,-1):
        if len(frequence_buckets[i]) == 0:
            continue
        for title in frequence_buckets[i]:
            for publication in title_to_info[title]:
                titlelist.append(title)
                publicationlist.append(publication)
    return titlelist, publicationlist

def word_cloud(year, top_n_keywords):
    word_frequance = {key: value for key, value in top_n_keywords[year]}
    print(word_frequance)
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_frequance)
    # 可视化词云
    return wordcloud
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()

def build_inverted_index(title_to_info):
    blocked_word_list = ["via", "it", "-", "of", "for", "in", "and", "or", "is", "the", "are", "a", "an", "on", "with",
                         "to", "using", "by", "from", "where", "into", "within", "onto", "this", "that", "based", "can",
                         "be", "have", "still", "how", "but", "as", "should"]
    keywords_per_year = defaultdict(list)
    inverted_index = defaultdict(list)

    for title in title_to_info:  # 建立倒排索引
        for info in title_to_info[title]:
            words = split_sentence(title)  # 将文献标题拆分为单词
            bj = {}
            for word in words:
                word = word.lower()
                if "year" in info:
                    year = info["year"]
                    if word not in blocked_word_list:
                        keywords_per_year[year].append(word)
                if word in bj:
                    continue
                bj[word] = 1
                if word in inverted_index:
                    inverted_index[word].append(title)
                else:
                    inverted_index[word] = [title]
    top_n_keywords = defaultdict(list)
    for year, keywords in keywords_per_year.items():
        # 计算词频
        word_count = defaultdict(int)
        for word in keywords:
            word_count[word] += 1

        # 构建桶
        max_count = 67000
        buckets_words = [[] for _ in range(max_count + 1)]
        for word, count in word_count.items():
            if count > max_count:
                print(word, count, year)
            else:
                buckets_words[count].append(word)

        # 找出排名前若干位的关键词
        top_n = min(100, len(keywords))
        count = 0
        for i in range(max_count, 0, -1):
            for word in buckets_words[i]:
                top_n_keywords[year].append((word, i))
                count += 1
                if count >= top_n:
                    break
            if count >= top_n:
                break
    return  top_n_keywords, inverted_index

def Bron_Kerbosch(R, P, X, graph, cliques):#B-K算法
    if not P and not X:
        if len(R) not in cliques:
            cliques[len(R)] = 1
        else:
            cliques[len(R)] += 1
        return

    for v in list(P):  # 将集合转换为列表
        Bron_Kerbosch(
            R | {v},
            P & set(graph[v]),
            X & set(graph[v]),
            graph,
            cliques
        )
        P.remove(v)
        X.add(v)

def clique_analysis(year, title_to_info):#给出年份，得到这一年的聚团分析
    clique_edge = defaultdict(list)
    for title in title_to_info:
        for publication in title_to_info[title]:
            if "year" in publication:
                year0 = publication["year"]
                if year0 == year:
                    if "authors" in publication:
                        authors = publication["authors"]
                    else:
                        if "editor" in publication:
                            authors = publication["editor"]
                        else:
                            if "author" in publication:
                                authors = publication["author"]
                            else:
                                if "editors" in publication:
                                    authors = publication["editors"]
                                else:
                                    authors = []
                    for author in authors:
                        if author not in clique_edge:
                            clique_edge[author] = []
                        for author2 in authors:
                            if author == author2:
                                continue
                            if author2 in clique_edge[author]:
                                continue
                            clique_edge[author].append(author2)
    cnt = 0
    num = defaultdict(int)
    for author in clique_edge:
        cnt += 1
        num[author] = cnt
    edge = defaultdict(list)
    for author in clique_edge:
        if author not in edge:
            edge[num[author]] = []
        for author2 in clique_edge[author]:
            edge[num[author]].append(num[author2])
    cliques = defaultdict(int)
    #print(cnt)
    Bron_Kerbosch(set(), set(edge.keys()), set(), edge, cliques)
    return cliques

def corperation(author1, author2, author_to_titles):
    titlelist1, publicationlist1 = find_author(author1, author_to_titles)
    titlelist3 = []
    publicationlist3 = []
    for title in titlelist1:
        if author2 in publicationlist1[titlelist1.index(title)]["authors"]: #通过详细信息中的作者列表判断是否合作
            titlelist3.append(title)
            publicationlist3.append(publicationlist1[titlelist1.index(title)])
    return titlelist3, publicationlist3

if __name__ == "__main__":
    #type_name = ["article" , "book" , "www" , "inproceedings" , "mastersthesis" , "incollection" , "proceedings" , "phdthesis"]

    #filename = 'dblp.pkl'
    allindex = create.readpkl("test.pkl")
    author_to_titles, title_to_info , buckets, edge_author, top_n_keywords, inverted_index = allindex.reset()
    print("finished building title index")
    #for author in author_to_titles:
    #    bj = defaultdict(int)
    #    for title in author_to_titles[author]:
    #        if title in bj:
    #            print(author, title)
    #        else:
    #            bj[title] = 1