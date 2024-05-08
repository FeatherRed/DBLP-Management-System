import pickle
import re
from collections import defaultdict
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def split_sentence(sentence):
    # 使用正则表达式匹配句子中的单词
    words = re.findall(r'\b\w+\b', sentence)
    return words

def build_index(filename):#建立作者到标题、标题到内容的索引
    type_name = ["article", "book", "www", "inproceedings", "mastersthesis", "incollection", "proceedings", "phdthesis"]
    edge_author = defaultdict(list)
    author_to_titles = defaultdict(list)
    title_to_info = defaultdict(list)
    with open(filename, 'rb') as file:
        data = pickle.load(file)
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
                    #if author1 not in edge_author:
                    #    edge_author[author1] = []
                    for author2 in authors:
                        if author2 == author1:
                            continue
                        if author2 in edge_author[author1]:
                            continue
                        edge_author[author1].append(author2)
    buckets = [[] for _ in range(32767)]
    for author in author_to_titles:
        buckets[len(author_to_titles[author])].append(author)
    return author_to_titles, title_to_info, buckets, edge_author

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

def fuzzy_search(query_words0, inverted_index, title_to_info):#返回值为标题列表，文献详细信息列表
    # 将用户输入的多个单词拆分成列表
    query_words = split_sentence(query_words0)
    # 初始化结果为 None
    result_titles = None
    for word in query_words:
        word = word.lower()
        if word in inverted_index:
            print(inverted_index[word])
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

def word_cloud(year, top_n_keywords):
    word_frequance = {key: value for key, value in top_n_keywords[year]}
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_frequance)

    # 可视化词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

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
if __name__ == "__main__":
    type_name = ["article" , "book" , "www" , "inproceedings" , "mastersthesis" , "incollection" , "proceedings" , "phdthesis"]

    filename = 'dblp.pkl'
    author_to_titles, title_to_info , buckets, edge_author= build_index(filename)
    top_n_keywords, inverted_index = build_inverted_index(title_to_info)
    print("finished building title index")
    #for author in author_to_titles:
    #    bj = defaultdict(int)
    #    for title in author_to_titles[author]:
    #        if title in bj:
    #            print(author, title)
    #        else:
    #            bj[title] = 1
    while True:
        year=input("Enter year: ")
        word_cloud(year, top_n_keywords)
