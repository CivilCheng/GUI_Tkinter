# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 23:32:52 2022

@author: cheng
"""

import os
from tkinter import filedialog
from tkinter import *

def browse_button():
    filename = filedialog.askdirectory()
    e1_value.set(filename)
    return filename

def list_filename():
    listbox1.delete(0, END)
    name_list = os.listdir(e1_value.get())
    
    for i in name_list:
        listbox1.insert(END, i)
    

window = Tk()
window.geometry('600x400')

lb1 = Label(window, text='Path')
lb1.grid(row=0, column=0)

button1 = Button(text="Browse", command=browse_button).grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


listbox1 = Listbox(window, width=20, height=10, selectmode=SINGLE)

button2 = Button(text="Open", command=list_filename).grid(row=0, column=4)

listbox1.grid(row=1, column=1, columnspan=2)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=1, column=3, sticky="NS")
scrollbar1.config( command = listbox1.yview )









window.mainloop()



