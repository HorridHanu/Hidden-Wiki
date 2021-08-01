#
#!/usr/bin/python3
#
#  [Program]
#
#  H-Wiki
#  HIDDEN WIKI
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.




__author__ = "Horrid Hanu"
__license__ = "GPL (GENERAL PUBLIC LICENSE)"
__version__ = "1.0"


"""Let's do some serious work! This will be mess of code. But who cares :)"""


"""General module import """
import tkinter
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter import ttk
import googletrans
from wikipedia import *
import pyperclip



"""Define finction for search"""

def Search():
    """ print("Work") """
    clear = "   "

    Text_area.config(state=NORMAL)
    Text_area.delete(1.0, END)
    # Text_area.config(state=DISABLED)
    Question = My_entry.get()
    Languages = combobox.get()

    for key, value in Language_dict.items():
        if Languages == value:
            wikipedia.set_lang(key)

    page = wikipedia.page(Question)
    Text_area.config(state=NORMAL)
    Text_area.insert(END, page.content)
    Text_area.config(state=DISABLED)


"""Define Copy Function"""
def Copy():
    content = Text_area.get(1.0, END)
    pyperclip.copy(content)


"""Define Edit Function"""
def Edit():
    Text_area.config(state=NORMAL)


"""Define Clear Function"""
def Clear():
    Text_area.config(state=NORMAL)
    Text_area.delete(1.0, END)
    Text_area.config(state=DISABLED)



"""All languages form google"""
Language_dict = googletrans.LANGUAGES



"""Main setup"""
root = Tk()
root.geometry('700x500+200+10')
root.title('HIDDEN-WIKI✔')
root.config(bg='black')
image = PhotoImage(file='find.png')
root.iconphoto(False, image)



"""Main label"""
My_lable = Label(root, text="HIDDEN-WIKI✔",
                 font=('Courier New', 20, 'bold'),
                 fg='White', bg='black', relief=SUNKEN, border=5)
My_lable.pack(padx=20, pady=30, anchor=W)



"""Search Entry"""
My_entry = Entry(My_lable, font=('Courier New', 30),
                 width=40, relief=SUNKEN, border=5)
My_entry.pack(padx=10, pady=20)
My_entry.focus()



"""Combobox for languages"""
combobox = ttk.Combobox(My_lable,
                        font=('times new roman', 21, 'bold'),
                        justify=CENTER, width=15, state='readonly')
combobox.pack(anchor=W, pady=10, padx=20)


combobox['values'] = [e for e in Language_dict.values()]
combobox.set('Select languages')



"""Search Button"""
Search = Button(My_lable, text='Search',
                font=('cooper black', 20, 'bold'),
                bg='red4', fg='white', relief=SUNKEN, border=5, command=Search)
Search.pack(padx=20, pady=7, anchor=E)



"""Frame for text area and scrollbar"""
My_frame = Frame(My_lable, )
My_frame.pack()



"""Scroll bar"""
sb = Scrollbar(My_frame)
sb.pack(side=RIGHT, fill=Y)



"""Text Area"""
Text_area = Text(My_frame, yscrollcommand=sb.set, wrap='word',
                 font=('Helvetica', 20), height=12, bg='brown',
                 fg='black', relief=SUNKEN, border=5)
Text_area.pack()
sb.config(command=Text_area.yview)



"""Button Frame"""
Button_frame = Frame(My_lable, bg='black', height=20)
Button_frame.pack(pady=4, fill=X)



"""Copy Button"""
Copy = Button(Button_frame, text='COPY', width=12,
              font=('cooper black', 13, 'bold'),
              fg="white", bg="orange", command=Copy)

Copy.pack(side=LEFT, padx=130)



"""Clear Button"""
Clear = Button(Button_frame, text='CLEAR', width=12,
               font=('cooper black', 13, 'bold'),
               fg="white", bg="orange", command=Clear)
Clear.pack(side=LEFT, )



"""Edit Button"""
Edit = Button(Button_frame, text='EDIT', width=12,
              font=('cooper black', 13, 'bold'),
              fg="white", bg="orange", command=Edit)

Edit.pack(side=LEFT, padx=100)




    # define function for View Help
def Help():
    tmsg.showerror("Help", "\n[*] Check your internet connection must be stabled :("
                           "\n[*] Must remind to selected the languages"
                           "\n\n[+] These packages must be installed!"
                           "\n[+] GoogleTrans : pip install googletrans"
                           "\n[+] Wikipedia : pip install wikipedia"
                           "\n[+] PyperClip : pip install pyperclip"
                           "\n[+] Upgrade pip : pip install --upgrade pip (Not recommended❕)")


    # define function for about!
def about():
    tmsg.showerror("About", "H-WIKI by Hanu.."
                            "\nGet All Hidden Information"
                            "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pending"
                            " Or Existing Intellecutal Property Right In"
                            " United State And Other Countries.")

def Exit():
        root.destroy()

    # define function for Next version
def Next_version():
    tmsg.showwarning("VERSION.",
                     f"\n[*] Version {__version__}"
                     f"\n[*] Author {__author__}"
                     f"\n[*] License {__license__}"
                     f"\n[*] GUI version AVAILABLE"
                     f"\n[*] Go To https://Github.com/HorridHanu/MovieInfo-Python")




    #Main Menu!


    # Submenu View Help
mainmenu = Menu(root)
m5 = Menu(mainmenu, tearoff=0)


    # Veiw Help
m5.add_command(label="View help", command=Help, compound=tkinter.LEFT)

    # next version
m5.add_command(label="Version..", command=Next_version, compound=tkinter.LEFT)
# m5.add_separator()

    # about
m5.add_command(label="About", command=about, compound=tkinter.LEFT)
m5.add_separator()
    # Exit
m5.add_command(label='Exit', command=Exit, compound=tkinter.LEFT)

mainmenu.add_cascade(label="Help", menu=m5)


    # View help menu END

root.config(menu=mainmenu)    #configure the mainmenu as menu



root.mainloop()