# 导入必要的模块
from lxml import etree  # 用于XML解析
import html  # 用于HTML实体转义
import pickle   #存record
import Function_index
from Record_class import Article, Book, WWW, Inproceedings, Mastersthesis, Incollection, Proceedings, Phdthesis
# 创建记录元素的函数
def create_record_element(element, tag):
    record_info = {}  # 用于存储记录信息的字典
    # 遍历子元素
    for child in element:
        # 根据子元素的标签进行处理
        if child.tag == 'author':
            record_info.setdefault('authors', []).append(html.unescape(child.text))
        elif child.tag == 'editor':
            record_info.setdefault('editors', []).append(html.unescape(child.text))
        else:
            record_info[child.tag] = child.text
    # 根据记录类型返回相应的记录对象
    match tag:
        case "article": return Article(**record_info)
        case "book": return Book(**record_info)
        case "www": return WWW(**record_info)
        case "inproceedings": return Inproceedings(**record_info)
        case "mastersthesis": return Mastersthesis(**record_info)
        case "incollection": return Incollection(**record_info)
        case "proceedings": return Proceedings(**record_info)
        case "phdthesis": return Phdthesis(**record_info)

# 从XML文件中读取记录
def read_records_from_xml(file_path):
    record_types = ['article', 'book', 'www', 'inproceedings', 'mastersthesis', 'incollection', 'proceedings','phdthesis']
    records = {record_type: [] for record_type in record_types}  # 初始化记录字典
    context = etree.iterparse(file_path, events=('start', 'end'))  # 创建XML解析器上下文
    current_record_type = None  # 当前记录类型初始化为空
    # 遍历XML解析器上下文中的事件和元素
    for event, element in context:
        if event == 'start' and element.tag in record_types:
            # 如果是起始事件且元素标签在记录类型列表中，则更新当前记录类型
            current_record_type = element.tag
        if event == 'end' and current_record_type is not None and element.tag == current_record_type:
            # 如果是结束事件且当前记录类型不为空且元素标签与当前记录类型相同，则创建记录对象并添加到记录字典中
            record = create_record_element(element, current_record_type)
            records[current_record_type].append(record)
            element.clear()  # 清除当前元素及其子元素
            while element.getprevious() is not None:
                del element.getparent()[0]  # 删除当前元素的父节点的第一个子节点
    del context  # 删除XML解析器上下文
    return records  # 返回记录字典

def createpkl(records,filename):
    for key, value in records.items():
        records[key] = [item.to_dict() for item in value]
    # 将记录字典写入pkl文件
    output_file = filename + ".pkl"
    Index = Function_index.build_index(records)
    with open(output_file, 'wb') as f:
        pickle.dump(Index,f)
    return Index
def readpkl(filepath):
    with open(filepath, "rb") as f:
        allindex = pickle.load(f)
    return allindex

# 定义记录类型列表和XML文件路径
if __name__ == "__main__":
    file_path = 'test1_deal.xml'

    # 从XML文件中读取记录
    records = read_records_from_xml(file_path)

    # 将记录对象转换为字典
    for key, value in records.items():
        records[key] = [item.to_dict() for item in value]

    # 将记录字典写入JSON文件
    output_file = 'Record.pkl'
    with open(output_file, 'w') as f:
        pickle.dump(records, f, True)  # 以缩进格式写入pkl文件
