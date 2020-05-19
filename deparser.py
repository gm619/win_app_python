# def test(*args, id_="", class_="", attrs_=""):
def test(tag, id_="", class_="", attrs_=""):
    print(tag)
    print(class_)
    print(id_)
    print(attrs_)


exec_params = {"class": "class_",
               "id": "id_",
               "attr": "attrs_"}

input_mass = map(lambda elem: str(elem).lstrip(),
                 "tag=div; id=my-beautifull-pony; class=once upon a time; attr=single".split(";"))
print(input_mass)

tag = None
tags_params = {}

for elem in input_mass:
    print("element "+elem)

    key, values = elem.split("=")

    key = exec_params[key] if key in exec_params else key

    tags_params[key] = values

    print(tags_params)

test(tags_params.pop("tag"), **tags_params)

# from html.parser import HTMLParser
# from lxml import html

# file = open('documentation.html', 'r').read()

# tree = html.fromstring(file)
# allH2 = tree.xpath('//div[@class="related"]')
# print(allH2)


# # class MyHTMLParser(HTMLParser):
# #     def handle_starttag(self, tag, attrs):
# #         print("Encountered a start tag:", tag)

# #     def handle_endtag(self, tag):
# #         print("Encountered an end tag :", tag)

# #     def handle_data(self, data):
# #         print("Encountered some data  :", data)

# # parser = MyHTMLParser()
# # parser.feed(file)

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         global string
#         string += "Start tag: {tag} \n"
#         for attr in attrs:
#             string += "     attr: {attr} \n"

#         return string

#     def handle_endtag(self, tag):
#         global string
#         string += "End tag  : {tag} \n"

#         return string

#     def handle_data(self, data):
#         global string
#         string += "Data     : {data} \n"

#         return string

#     def handle_comment(self, data):
#         print("Comment  :", data)

#     def handle_entityref(self, name):
#         c = chr(name2codepoint[name])
#         print("Named ent:", c)

#     def handle_charref(self, name):
#         if name.startswith('x'):
#             c = chr(int(name[1:], 16))
#         else:
#             c = chr(int(name))
#         print("Num ent  :", c)

#     def handle_decl(self, data):
#         print("Decl     :", data)