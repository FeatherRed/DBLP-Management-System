from lxml import etree

def read_all_tags(file_path, publtypes):
    all_tags = {publtype: set() for publtype in publtypes}
    context = etree.iterparse(file_path, events=('start', 'end'))
    for event, element in context:
        if event == 'end' and element.tag in publtypes:
            if element.text:
                print(f"Content of {element.tag}: {element.text}")
            else:
                print(f"No content found for {element.tag}")
            all_tags[element.tag].update(child.tag for child in element)
            element.clear()
            while element.getprevious() is not None:
                del element.getparent()[0]
    del context
    return all_tags

file_path = 'test.xml'
publtypes = ["article","book","www","inproceedings","mastersthesis","incollection","proceedings","phdthesis"]
tags = read_all_tags(file_path, publtypes)
for publtype, tags in tags.items():
    print(f"Tags in {publtype}: {tags}")
