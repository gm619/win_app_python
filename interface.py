import os 

from tkinter import *
from tkinter import filedialog

from bs4 import BeautifulSoup
from html.parser import HTMLParser
from html.entities import name2codepoint

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

def FindInFile():
    global fn
    file_content = open(fn, 'rt').read()
    soup = BeautifulSoup(file_content, 'html.parser')
    
    # v 0.0.1b
    # tag, class_name = start_tag.get().split(',')
    # result = soup.find(tag, class_=class_name).prettify()
    # text_box.delete('1.0', 'end')
    # text_box.insert('1.0', result)

    # v 0.0.1
    # if search_tag:
    #     try:
    #         tag, class_name = search_tag.split(',')
    #         result = soup.find(tag, class_=class_name).prettify()
    #         text_box.delete('1.0', 'end')
    #         text_box.insert('1.0', result)
    #     except ValueError:
    #         print("MOLOKO")
    #     except AttributeError:
    #         print("KOFE")
    #     try:
    #         tag = search_tag.split(',')
    #         print(tag)
    #         print("KEFIR")
    #         result = soup.find(tag).prettify()
    #     except:
    #         print("KAKAO")
    # else:
    #     text_box.delete('1.0', 'end')
    #     text_box.insert('1.0', 'You do not enter "tag"')

    # v 0.0.2
    search_tag = start_tag.get()
    input_mass = map(lambda elem: str(elem).lstrip(), search_tag.split(";"))

    exec_params = {"class": "class_"}
    tags_params = {}    

    for elem in input_mass:
        key, values = elem.split("=")
        key = exec_params[key] if key in exec_params else key
        tags_params[key] = values

    result = soup.find(tags_params.pop("tag"), **tags_params).prettify()
    text_box.delete('1.0', 'end')
    text_box.insert('1.0', result)


def StartRemoving():
    if not start_tag.get():
        text_box.delete('1.0', 'end')
        text_box.insert('1.0', "tag is empty")
    else:
        for filename in os.listdir():
            if filename.endswith('.html'):
                file_content = open(filename, 'rt').read()
                soup = BeautifulSoup(file_content, 'html.parser')

                # v 0.0.1
                # tag, class_name = start_tag.get().split(',')   
                # if not class_name:
                #     result = soup.find(tag).prettify()
                # else:
                #     result = soup.find(tag, class_=class_name).prettify()
                # filename = "new_"+filename
                # open(filename, 'wt').write(result)
                # text_box.delete('1.0', 'end')
                # text_box.insert('1.0', "Done")

                # v 0.0.2
                search_tag = start_tag.get()
                input_mass = map(lambda elem: str(elem).lstrip(), search_tag.split(";"))

                exec_params = {"class": "class_"}
                tags_params = {}    

                for elem in input_mass:
                    key, values = elem.split("=")
                    key = exec_params[key] if key in exec_params else key
                    tags_params[key] = values

                result = soup.find(tags_params.pop("tag"), **tags_params).prettify()
                filename = "new_"+filename
                open(filename, 'wt').write(result)
                text_box.delete('1.0', 'end')
                text_box.insert('1.0', "Done")

def SaveFile():
    sfn = filedialog.asksaveasfilename(filetypes = [('*.html files', '.html')])
    if sfn == '':
        return
    if not sfn.endswith(".html"):
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
label1 = Label(app, text='In tag input you write tag=div first, after semicolon')
label1.grid(row=2, column=0, columnspan=2, sticky=W)
label2 = Label(app, text='you can type class or id that separating them semicolon')
label2.grid(row=3, column=0, columnspan=2, sticky=W)
label3 = Label(app, text='example: tag=div; class=related; id="first" equal "div class="related" id="first"')
label3.grid(row=4, column=0, columnspan=2, sticky=W)

# text after serching
scroll_for_tb = Scrollbar(app)
scroll_for_tb.grid(row=5, column=3, sticky=N+S+W)

text_box = Text(app, height=20, border=1)
text_box.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
text_box.configure(yscrollcommand=scroll_for_tb.set)

scroll_for_tb.configure(command=text_box.yview)

# open file buttin
open_buttom = Button(app, text="Open File", width=12, command=OpenFile)
open_buttom.grid(row=6, column=0)

# start button
start_button = Button(app, text="Start", width=12, command=FindInFile)
start_button.grid(row=6, column=1)

# save one file button
save_button = Button(app, text="Save", width=12, command=SaveFile)
save_button.grid(row=6, column=2)

# button for find child of tag in files
# child_button = Button(app, text="Children tag", width=12)
# child_button.grid(row=7, column=0)

# button for find parent of tag in files
parent_button = Button(app, text="All files", width=12, command=StartRemoving)
parent_button.grid(row=7, column=1)

# Quit button
quit_button = Button(app, text="Quit", width=12, command=Quit)
quit_button.grid(row=7, column=2)

app.title('Deparser')
app.geometry('640x500')

app.mainloop()

# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff = 0)
# filemenu.add_command(label = "Open", command = OpenFile)
# filemenu.add_command(label = "Save", command = SaveFile)

# filemenu.add_separator()

# filemenu.add_command(label = "Exit", command = root.quit)
# menubar.add_cascade(label = "File", menu = filemenu)
