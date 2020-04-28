from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
# read write files
from io import *
# html parser
from html.parser import HTMLParser

# class FileReadWrite:
#     def read(file_name):
#         # f = open("documentation.html", "r")
#         f = open(file_name, "r")
#         text = f.read()
#         len(text)
#         text

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry2 = Entry(master)

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.entry2.grid(row=2, column=1, columnspan=3, sticky=W+E)

        self.add_button.grid(row=3, column=0)
        self.subtract_button.grid(row=3, column=1)
        self.reset_button.grid(row=3, column=4, sticky=W+E)
        # self.create_widgets(master)

        mask = Tk.READABLE | Tk.WRITABLE
        
        self.tk.createfilehandler(file, mask, callback)
        self.tk.deletefilehandler(file)

        # import tkinter
        # widget = tkinter.Tk()
        # mask = tkinter.READABLE | tkinter.WRITABLE
        # file = 'documentation.html'
        # widget.tk.createfilehandler(file, mask, callback)

    def widget(self):
        self.input = Input(self)


    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()