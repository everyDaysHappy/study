from xml.etree import ElementTree as ET

# 创建跟标签
root = ET.Element('home')

# 创建儿子节点
son1 = ET.Element('son', {'name': '大儿子'})
son2 = ET.Element('son', {'name': '二儿子'})

# 创建孙子节点
grandson1 = ET.Element('grandson', {'name': '大孙子'})
grandson2 = ET.Element('grandson', {'name': '二孙子'})
# 孙子节点添加到儿子节点
son1.append(grandson1)
son2.append(grandson2)

# 儿子节点添加到根标签
root.append(son2)
root.append(son1)

tree = ET.ElementTree(root)
# short_empty_elements 是否进行标签的简写，标签没有值，没必要再写结束标签 <son name="大儿子" /> = <son name="大儿子"></son>
tree.write('TestFile/makeXml.xml', encoding='utf-8', short_empty_elements=True)

# 创建节点的第二种方式
# root1 = ET.Element('Tree')
# Son1 = root1.makeelement('Son1')
# root1.append(Son1)

# 创建节点的第三种方式
Root = ET.Element('family')
RootSon = ET.SubElement(Root, 'son', attrib={'name': '儿子'})
RootGrandSon = ET.SubElement(RootSon, 'grandson', attrib={'name': '孙子'})
RootSon.text = '儿贼'
RootGrandSon.text = '孙贼'



