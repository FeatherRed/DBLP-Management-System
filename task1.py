import  json
#with open('Record.json', 'r') as file:
#    json_content = file.read()

# 解析JSON内容并转换为Python数据结构
#data = json.loads(json_content)
def build_index(filename):
    author_to_titles = {}
    title_to_info = {}
    with open(filename, 'r') as file:
        data = json.load(file)
        for publication in data["article"]:
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
        for publication in data["book"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["www"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["inproceedings"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["mastersthesis"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["incollection"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["proceedings"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
        for publication in data["phdthesis"]:
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
            for author in authors:
                if author in author_to_titles:
                    author_to_titles[author].append(title)
                else:
                    author_to_titles[author] = [title]
            title_to_info[title] = publication
    return author_to_titles, title_to_info

filename = 'Record.json'
author_to_titles, title_to_info = build_index(filename)
buckets = [[] for _ in range(32767)]
for author in author_to_titles:
    buckets[len(author_to_titles[author])].append(author)
def print_pren_author(x):
    cnt=0
    for i in range(32766,0,-1):
        if len(buckets[i])==0:
            continue
        if cnt<=x:
            for author in buckets[i]:
                cnt+=1
                if cnt<=x:
                    print(f"{author}: {i} publications")
        else:
            break

while True:
    opt=eval(input("please input your choice: "))
    if opt == 1:
        opt1=eval(input("please input"))
        s=input("please input")
        if opt1 == 1:
            if s in author_to_titles:
                for title in author_to_titles[s]:
                    print(title)
            else:
                print("invalid author name")
        else:
            if s in title_to_info:
                print(title_to_info[s])
            else:
                print("invalid article name")