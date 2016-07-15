from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print("->", a[0], ">", a[1])
    def handle_endtag(self, tag):
        pass
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print("->", a[0], ">", a[1])

parser = MyHTMLParser()
s = ""
for i in range(int(input())):
    s += input()
parser.feed(s)