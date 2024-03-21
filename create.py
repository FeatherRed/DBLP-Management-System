from lxml import etree
import json

class Article:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.journal = kwargs.get('journal', None)
        self.year = kwargs.get('year', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number', None)
        self.pages = kwargs.get('pages', None)
        self.month = kwargs.get('month', None)
        self.publisher = kwargs.get('publisher', None)
        self.booktitle = kwargs.get('booktitle', None)
        self.editors = kwargs.get('editors', [])
        self.url = kwargs.get('url', None)
        self.ee = kwargs.get('ee', None)
        self.cite = kwargs.get('cite', None)
        self.cdrom = kwargs.get('cdrom', None)
        self.crossref = kwargs.get('crossref', None)
        self.publnr = kwargs.get('publnr', None)
        self.note = kwargs.get('note', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

def create_article_element(element):
    article_info = {}
    for child in element:
        if child.tag == 'author':
            article_info.setdefault('authors', []).append(child.text)
        else:
            article_info[child.tag] = child.text
    return Article(**article_info)


def read_articles_from_xml(file_path):
    articles = []
    context = etree.iterparse(file_path, events=('start', 'end'))
    for event, element in context:
        if event == 'end' and element.tag == 'article':
            article = create_article_element(element)
            articles.append(article)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    del context
    return articles


# 读取 XML 文件并创建 Article 对象列表
file_path = 'test.xml'
articles = read_articles_from_xml(file_path)

# 打印所有 Article 对象的信息
output_file = 'articles.json'
with open(output_file, 'w') as f:
    articles_data = [article.to_dict() for article in articles]
    json.dump(articles_data, f, indent=4)
