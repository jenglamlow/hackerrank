from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for a in attrs:
            print("->", a[0], ">", a[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for a in attrs:
            print("->", a[0], ">", a[1])

parser = MyHTMLParser()
s = ""
for i in range(int(input())):
    s += input()
parser.feed(s)