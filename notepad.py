from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile(event=None):
    global file
    root.title("Untitled - file")
    file = None
    TextArea.delete(1.0,END)


def openFile(event=None):
    global file
    file  = askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])
    if file == "":
        file = None
    else:
        # file = 
        root.title(os.path.basename(file+" - Notepad"))
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile(event=None):
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])
        if file=="":
            file = None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad")



def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by yatish\nHere you can manage your files and data and store it in your pc.")
    pass

def select_all():
    TextArea.tag_add('sel', '1.0', 'end')

if __name__  ==  "__main__":
    #general settings here
    root = Tk()
    root.title("Untitled - notepad")
    root.geometry("500x500")
    root.bind('<Control-o>', openFile)
    root.bind('<Control-s>', saveFile)
    root.bind('<Control-n>', newFile)

    
    #Add text area
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    #craeting a menu bar
    MenuBar = Menu(root)

    #filemenu starts
    FileMenu = Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label="New     Ctrl+N",command=newFile)
    FileMenu.add_command(label="Open     Ctrl+O",command=openFile)
    FileMenu.add_command(label="Save     Ctrl+S",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #filemenu ends
    
    # edit menu starts
    EditMenu =  Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    EditMenu.add_command(label="Select all",command=select_all)
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    # edit menu ends

    # Help menu starts
    HelpMenu =  Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    # edit menu ends



    root.config(menu=MenuBar)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()


