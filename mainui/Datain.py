'''
该文件主要是对xml进行数据处理
'''
import html
import os

def xmlprocessing(file_path,new_file_path):
    '''
    :string file_path:      orignal file path -->> dblp.xml
    :string new_file_path:  new file path     -->> dblp_deal.xml
    :return:
    '''
    with open(file_path, 'r', encoding='utf-8') as input_file, open(new_file_path, 'w',encoding='utf-8') as output_file:
        # 逐行读取原始XML文件
        for line in input_file:
            line = line.replace('&lt;', '__LT__')
            line = line.replace('&gt;', '__GT__')
            line = line.replace('&#60', '__LT__')
            line = line.replace('&#62', '__GT__')
            line = line.replace('&#916;', '__delta__')
            line = line.replace('&quot;', '__quot__')
            line = line.replace('&#34;', '__quot__')
            line = html.unescape(line)
            line = line.replace('&', ' and ')
            line = line.replace('title>>', 'title>&gt;')
            line = line.replace('<<', '&lt;&lt;')
            line = line.replace('>>', '&gt;&gt;')
            line = line.replace('__LT__', '&lt;')
            line = line.replace('__GT__', '&gt;')
            line = line.replace('__delta__', '&#916;')
            line = line.replace('__quot__', '&quot;')
            line = line.replace('<i>','')
            line = line.replace('</i>', '')
            line = line.replace('<sup>', '')
            line = line.replace('</sup>', '')
            line = line.replace('<sub>', '')
            line = line.replace('</sub>', '')
            # 将修改后的行写入目标文件
            output_file.write(line)


def preprocessing(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]        ##获得该文件名字
    new_file_path = file_name + "_deal.xml"                             ##新的文件
    #先判断当前是否是已经处理过的
    if os.path.exists(new_file_path):                                   ##判断是否已经处理好
        #print("The xml file has been processed")
        return
    else:
        #print("Now let's start working on the xml file")
        xmlprocessing(file_path,new_file_path)

if __name__ == "__main__":
    file_path = "test1_deal.xml"
    preprocessing(file_path)