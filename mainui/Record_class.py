'''
['article','book','www','inproceedings','mastersthesis','incollection','proceedings','phdthesis']
Tags in article: {'pages', 'cite', 'year', 'cdrom', 'author', 'editor', 'booktitle', 'volume', 'ee', 'month', 'title', 'url', 'number', 'journal', 'crossref', 'publnr', 'note', 'publisher'}
Tags in book: {'booktitle', 'volume', 'url', 'pages', 'cite', 'year', 'cdrom', 'series', 'crossref', 'school', 'editor', 'journal', 'note', 'author', 'ee', 'month', 'title', 'isbn', 'publisher'}
Tags in www: {'cite', 'year', 'author', 'editor', 'ee', 'title', 'url', 'crossref', 'note'}
Tags in inproceedings: {'pages', 'cite', 'year', 'booktitle', 'author', 'cdrom', 'editor', 'volume', 'ee', 'month', 'url', 'title', 'crossref', 'number', 'note'}
Tags in mastersthesis: {'pages', 'year', 'school', 'author', 'ee', 'title', 'isbn', 'note', 'publisher'}
Tags in incollection: {'pages', 'cite', 'booktitle', 'year', 'author', 'cdrom', 'ee', 'number', 'title', 'crossref', 'url', 'chapter', 'note', 'publisher'}
Tags in proceedings: {'pages', 'cite', 'booktitle', 'year', 'author', 'editor', 'school', 'volume', 'address', 'series', 'ee', 'title', 'url', 'isbn', 'number', 'journal', 'note', 'publisher'}
Tags in phdthesis: {'pages', 'year', 'author', 'school', 'volume', 'series', 'ee', 'title', 'number', 'isbn', 'month', 'note', 'publisher'}
Tags in rel: set()
'''

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
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Book:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.journal = kwargs.get('journal', None)
        self.year = kwargs.get('year', None)
        self.volume = kwargs.get('volume', None)
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
        self.note = kwargs.get('note', None)
        self.isbn = kwargs.get('isbn', None)
        self.school = kwargs.get('school', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class WWW:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.year = kwargs.get('year', None)
        self.editors = kwargs.get('editors', [])
        self.url = kwargs.get('url', None)
        self.ee = kwargs.get('ee', None)
        self.cite = kwargs.get('cite', None)
        self.crossref = kwargs.get('crossref', None)
        self.note = kwargs.get('note', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Inproceedings:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.year = kwargs.get('year', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number',None)
        self.pages = kwargs.get('pages', None)
        self.month = kwargs.get('month', None)
        self.booktitle = kwargs.get('booktitle', None)
        self.editors = kwargs.get('editors', [])
        self.url = kwargs.get('url', None)
        self.ee = kwargs.get('ee', None)
        self.cite = kwargs.get('cite', None)
        self.cdrom = kwargs.get('cdrom', None)
        self.crossref = kwargs.get('crossref', None)
        self.note = kwargs.get('note', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Mastersthesis:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.year = kwargs.get('year', None)
        self.pages = kwargs.get('pages', None)
        self.publisher = kwargs.get('publisher', None)
        self.ee = kwargs.get('ee', None)
        self.note = kwargs.get('note', None)
        self.isbn = kwargs.get('isbn', None)
        self.school = kwargs.get('school', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Incollection:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.year = kwargs.get('year', None)
        self.number = kwargs.get('number', None)
        self.pages = kwargs.get('pages', None)
        self.publisher = kwargs.get('publisher', None)
        self.booktitle = kwargs.get('booktitle', None)
        self.url = kwargs.get('url', None)
        self.ee = kwargs.get('ee', None)
        self.cite = kwargs.get('cite', None)
        self.cdrom = kwargs.get('cdrom', None)
        self.crossref = kwargs.get('crossref', None)
        self.note = kwargs.get('note', None)
        self.chapter = kwargs.get('chapter', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Proceedings:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.journal = kwargs.get('journal', None)
        self.year = kwargs.get('year', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number', None)
        self.pages = kwargs.get('pages', None)
        self.publisher = kwargs.get('publisher', None)
        self.booktitle = kwargs.get('booktitle', None)
        self.editors = kwargs.get('editors', [])
        self.url = kwargs.get('url', None)
        self.ee = kwargs.get('ee', None)
        self.cite = kwargs.get('cite', None)
        self.note = kwargs.get('note', None)
        self.isbn = kwargs.get('isbn', None)
        self.school = kwargs.get('school', None)
        self.series = kwargs.get('series', None)
        self.address = kwargs.get('address', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}

class Phdthesis:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', None)
        self.authors = kwargs.get('authors', [])
        self.year = kwargs.get('year', None)
        self.volume = kwargs.get('volume', None)
        self.number = kwargs.get('number', None)
        self.pages = kwargs.get('pages', None)
        self.month = kwargs.get('month', None)
        self.publisher = kwargs.get('publisher', None)
        self.ee = kwargs.get('ee', None)
        self.note = kwargs.get('note', None)
        self.isbn = kwargs.get('isbn', None)
        self.school = kwargs.get('school', None)
        self.series = kwargs.get('series', None)

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None and len(v) > 0}
