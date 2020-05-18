import os 

from tkinter import *
from tkinter import filedialog

from bs4 import BeautifulSoup
from html.parser import HTMLParser
from html.entities import name2codepoint

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

# file name
files = []
fn = ''
string = ''

def OpenFile(): 
    global fn
    fn = filedialog.askopenfilename(filetypes = [('*.html files', '.html')])
    if fn == '':
        return
    text_box.delete('1.0', 'end') 
    text_box.insert('1.0', open(fn, 'rt').read())

def StartRemoving():
    for filename in os.listdir():
        if filename.endswith('.html'):
            files.append(filename)
            file_content = open(filename, 'rt').read()
            soup = BeautifulSoup(file_content, 'html.parser')
            tag, class_name = start_tag.get().split(',')
            result = soup.find(tag, class_=class_name).prettify()
            text_box.delete('1.0', 'end')
            text_box.insert('1.0', result)


def SaveFile():
    sfn = filedialog.asksaveasfilename(filetypes = [('*.html files', '.html')])
    if sfn == '':
        return
    if not fn.endswith(".html"):
        sfn+=".html"
    open(sfn, 'wt').write(text_box.get('1.0', 'end'))

def Quit():
    global app
    app.destroy()

app = Tk()

# start Tag
start_tag = StringVar()
start_tag_label = Label(app, text='Tag', font=('bold', 14), pady=10)
start_tag_label.grid(row=1, column=0, sticky=W)
start_tag_entry = Entry(app, textvariable=start_tag, width=40)
start_tag_entry.grid(row=1, column=1, columnspan=2)

# description label
label = Label(app, text='Intag input you write tag first than class after comma, without space')
label.grid(row=2, column=0, columnspan=2)

# end Tag
# end_tag = StringVar()
# end_tag_label = Label(app, text='End Tag', font=('bold', 14), pady=20)
# end_tag_label.grid(row=3, column=0, sticky=W)
# end_tag_entry = Entry(app, textvariable=end_tag, width=40)
# end_tag_entry.grid(row=3, column=1, columnspan=2)

# text after serching
scroll_for_tb = Scrollbar(app)
scroll_for_tb.grid(row=4, column=3)

text_box = Text(app, height=20, border=1)
text_box.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
text_box.configure(yscrollcommand=scroll_for_tb.set)

scroll_for_tb.configure(command=text_box.yview)

# open file buttin
open_buttom = Button(app, text="Open File", width=12, command=OpenFile)
open_buttom.grid(row=5, column=0)

# start button
start_button = Button(app, text="Start", width=12)
start_button.grid(row=5, column=1)

# save one file button
save_button = Button(app, text="Save", width=12, command=SaveFile)
save_button.grid(row=5, column=2)

# button for all files
all_files_button = Button(app, text="All files", width=12, command=StartRemoving)
all_files_button.grid(row=6, column=0)

# Quit button
quit_button = Button(app, text="Quit", width=12, command=Quit)
quit_button.grid(row=6, column=2)

app.title('Deparser')
app.geometry('630x470')


app.mainloop()


# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "Open", command = OpenFile)
# filemenu.add_command(label = "Save", command = SaveFile)

# filemenu.add_separator()

# filemenu.add_command(label = "Exit", command = root.quit)
# menubar.add_cascade(label = "File", menu = filemenu)
