from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("TextEdit")
root.geometry("1200x660+0+0")


def new_file():
    my_text.delete("1.0", END)
    root.title('New File- TextEdit')
    status_bar.config(text="New File   ")


def open_file():
    my_text.delete("1.0", END)  
    text_file = filedialog.askopenfilename(initialdir="F:\HTML", title="Open File", filetypes=(
        ("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("PDF Files", "*.pdf")))
    name = text_file
    status_bar.config(text=f'{name}       ')
    name = name.replace("F:\HTML", "")
    root.title(f'{name}- TextEdit')

    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)  # Add file to textbox
    text_file.close()  # Close the text file


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="F:\HTML", title="Save File", filetypes=(
        ("All Files", "*.*"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("PDF Files", "*.pdf")))
    if text_file:
        name = text_file
        status_bar.config(text=f'{name}       ')
        name = name.replace("F\HTML", "")

        text_file = open(text_file, "w")
        text_file.write(1.0, END)
        text_file.close()


f1 = Frame(root)
f1.pack(pady=5)

text_scroll = Scrollbar(f1)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(f1, width=97, height=25, font=("Lucida Typewriter", 16), selectbackground="yellow",
               selectforeground="black", undo="True", yscrollcommand=text_scroll.set)
my_text.pack()
text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)

# File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Status Bar
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
