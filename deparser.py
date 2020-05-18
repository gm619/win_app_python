from html.parser import HTMLParser
from lxml import html

file = open('documentation.html', 'r').read()

tree = html.fromstring(file)
allH2 = tree.xpath('//div[@class="related"]')
print(allH2)


# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)

#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)

#     def handle_data(self, data):
#         print("Encountered some data  :", data)

# parser = MyHTMLParser()
# parser.feed(file)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global string
        string += "Start tag: {tag} \n"
        for attr in attrs:
            string += "     attr: {attr} \n"

        return string

    def handle_endtag(self, tag):
        global string
        string += "End tag  : {tag} \n"

        return string

    def handle_data(self, data):
        global string
        string += "Data     : {data} \n"

        return string

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)