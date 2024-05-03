import pickle
import re
from collections import defaultdict

def split_sentence(sentence):
    # 使用正则表达式匹配句子中的单词
    words = re.findall(r'\b\w+\b', sentence)
    return words

def build_index(filename):#建立作者到标题、标题到内容的索引
    type_name = ["article", "book", "www", "inproceedings", "mastersthesis", "incollection", "proceedings", "phdthesis"]
    edge_author = defaultdict(list)
    author_to_titles = {}
    title_to_info = {}
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
                        authors = []
            # 构建作者到文献标题的映射
                for author in authors:
                    if author in author_to_titles:
                        author_to_titles[author].append(title)
                    else:
                        author_to_titles[author] = [title]
            # 构建文献标题到文献信息的映射
                title_to_info[title] = publication
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
    return author_to_titles, title_to_info, buckets

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

def top_n_keywords_per_year(n):
    #桶排序计算每年前n的关键词
    top_n_keywords = defaultdict(list)
    for year, keywords in keywords_per_year.items():
        # 计算词频
        word_count = defaultdict(int)
        for word in keywords:
            word_count[word] += 1

        # 构建桶
        max_count = 62000
        buckets_words = [[] for _ in range(max_count + 1)]
        for word, count in word_count.items():
            if count > max_count:
                print(word,count,year)
            else:
                buckets_words[count].append(word)

        # 找出排名前若干位的关键词
        top_n = min(n, len(keywords))
        count = 0
        for i in range(max_count, 0, -1):
            for word in buckets_words[i]:
                top_n_keywords[year].append((word, i))
                count += 1
                if count >= top_n:
                    break
            if count >= top_n:
                break
    return top_n_keywords

def find_author():
    s = input("please input author")
    if s in author_to_titles:
        for title in author_to_titles[s]:
            print(title)
    else:
        print("invalid author name")

def find_title():
    s = input("please input title")
    if s in title_to_info:
        print(title_to_info[s])
    else:
        print("invalid article name")

def fuzzy_search(query_words0):
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
    if result_titles:
        print("模糊搜索结果:")
        for title in result_titles:
            print(title)
            # 输出文献的其他信息
            print(title_to_info[title])
    else:
        print("找不到与所有输入单词相关的文献.")

def top_keyword_per_year():#用于输出某年的词频
    year = input("please input year")
    cnt = 0
    for keywords in top_n_keywords[year]:
        cnt = cnt + 1
        print(keywords)
        if cnt == 10:
            break

# while True :
#     opt = eval(input("please input your choice: "))
#     if opt == 1:
#         opt1 = eval(input("please input"))
#         if opt1 == 1:
#             find_author()
#         else:
#             find_title()
#     if opt == 3:
#         pren = eval(input("please input"))
#         print_pre_n_author(pren)
#     if opt == 4:
#         year = input("please input year")
#         cnt = 0
#         for keywords in top_n_keywords[year]:
#             cnt = cnt + 1
#             print(keywords)
#             if cnt == 10 :
#                 break
#     if opt == 5:
#         s = input("please input words")
#         fuzzy_search(s)
#     if opt == 2:
#         s = input("please input author")
#         if s not in edge_author:
#             print("invalid author")
#         for author in edge_author[s]:
#             print(author)
if __name__ == "__main__":
    type_name = ["article" , "book" , "www" , "inproceedings" , "mastersthesis" , "incollection" , "proceedings" , "phdthesis"]
    edge_author = defaultdict(list)
    filename = 'dblp.pkl'
    author_to_titles, title_to_info = build_index(filename)
    buckets = [[] for _ in range(32767)]
    for author in author_to_titles:
        buckets[len(author_to_titles[author])].append(author)
    print("finished building title index")
    blocked_word_list = ["via","it","-","of","for","in","and","or","is","the","are","a","an","on","with","to","using","by","from","where","into","within","onto","this","that","based","can","be","have","still","how","but","as","should"]
    keywords_per_year = defaultdict(list)
    inverted_index = {}
    top_n_keywords = top_n_keywords_per_year(100)
    for title, info in title_to_info.items():  # 建立倒排索引
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