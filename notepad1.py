from random import randrange as r
from time import time as t
import os
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter import *


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt"),
                                      ("Html Documents", "*.html")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<>"))


def copy():
    TextArea.event_generate(("<>"))


def paste():
    TextArea.event_generate(("<>"))


def about():
    showinfo('''Notepad is the default text editor built-in Windows OS.\n It is used to create, edit and save text documents. \nIn this Notepad, there are 3 menus with options for CREATE, SAVE, NEW, CUT, COPY AND PASTE. \nIt is the exact replica of the Notepad in Windows.''')


if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Notepad")
    root.geometry("1000x1000")
    TextArea = Text(root, font=("Lucida Console", 34))
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=MenuBar)
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.mainloop()
#import modules
# ask how many questions user wants
no_questions = int(input('How many questions do you want?: '))
max_num = int(input('Highest number used in practice?: '))
# set score start at zero
score = 0
answer_list = []
# loop through number of questions
start = t()
for q in range(no_questions):
    num1, num2 = r(1, max_num+1), r(1, max_num+1)
    ans = num1 * num2
    u_ans = int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
    if u_ans == ans:
        score += 1
    end = t()
print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct in {round(end-start,1)} seconds ({round((end-start)/no_questions,1)}seconds/question)')
for a in answer_list:
    print(a)
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score
