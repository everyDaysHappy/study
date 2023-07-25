from xml.etree import ElementTree as ET

# 直接解析xml文件
tree = ET.parse('TestFile/test.xml')

# 获取根标签
root = tree.getroot()  # fcc_merch

# 获取跟标签2
# root = ET.XML(内容)  以字符串的形式获取

# 获取根标签的孩子标签
for child in root:
    # child.tag 子标签
    # chile.attrib 子标签的属性
    print(child.tag, child.attrib)
    for node in child:
        print(node.tag, node.attrib, node.text)

# 定式寻找第一个目的标签
data_tag = root.find('data')
# 找到所有的目标标签
# data_tag = root.findall('data')
print(data_tag.tag, data_tag.attrib)

country_tag = data_tag.find('country')
print(country_tag.tag, country_tag.attrib)

# 修改节点内容和属性
itemName_tag = root.find('item').find('name')
print(itemName_tag.text)
itemName_tag.text = 'Hello World!'
itemName_tag.set('update', '2023-03-17')
print(itemName_tag.text, itemName_tag.attrib)

# 删除文件
# root.remove(root.find('item'))

# 保存文件
tree.write('new.xml', encoding='utf-8')


