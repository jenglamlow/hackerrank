import xml.etree.ElementTree as etree
from xml.etree.ElementTree import XMLParser

class MaxDepth:
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):
        self.depth -= 1
    def data(self, data):
        pass
    def close(self):
        if self.maxDepth > 0:
            return self.maxDepth - 1
        else:
            return self.maxDepth

S = ""
for _ in range(int(input())):
    S += input()

target = MaxDepth()
parser = XMLParser(target=target)
parser.feed(S)
print(parser.close())
