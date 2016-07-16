import xml.etree.ElementTree as etree

S = ""
for _ in range(int(input())):
    S += input()

tree = etree.ElementTree(etree.fromstring(S))
count = 0
count += len(tree.getroot().attrib)
for t in tree.findall('.//'):
    count+=len(t.attrib)
print(count)