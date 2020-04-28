from tkinter import filedialog
from tkinter import *

def Quit(ev):
    global root
    root.destroy()
    
def OpenFile(ev): 
    fn = filedialog.askopenfilename(filetypes = [('*.html files', '.html')])
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(fn, 'rt').read())
    
def SaveFile(ev):
    fn = filedialog.asksaveasfilename(filetypes = [('*.txt files', '.txt')])
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

root = Tk()

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 140, width = 600)
# my frames
tagsFrame = Frame(root, height = 120, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)
# my frames packer
tagsFrame.pack(side = 'top', fill = 'x', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)
starttagsbox = Entry(tagsFrame, font='Arial 14')
# starttagsbox = Entry(tagsFrame, textvariable=StringVar())
endtagsbox = Entry(tagsFrame, textvariable=StringVar())

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set


textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')
starttagsbox.pack(side='left', fill='none')
endtagsbox.pack(side='left', fill='none')

loadBtn = Button(panelFrame, text = 'Open File')
saveBtn = Button(panelFrame, text = 'Save')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", OpenFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 80, height = 40)
saveBtn.place(x = 100, y = 10, width = 40, height = 40)
quitBtn.place(x = 150, y = 10, width = 40, height = 40)

root.mainloop()