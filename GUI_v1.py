# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 23:32:52 2022

@author: cheng
"""

import os
import pandas as pd
from tkinter import filedialog
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def browse_button():
    path = filedialog.askdirectory()
    e1_value.set(path)
    return path

def list_filename():
    listbox1.delete(0, END)
    name_list = os.listdir(e1_value.get())
    
    for i in name_list:
        listbox1.insert(END, i)
    
def getElement(event):
    selection = event.widget.curselection()
    if selection:
        
        #get file name
        index = selection[0]
        name = event.widget.get(index)
        lb3_value.set(name)
        
        #import data
        global data
        path_name = os.path.join(e1_value.get(), name)
        data = pd.read_csv(path_name)
        
        listbox2.delete(0, END)
        for i in data.columns:
            listbox2.insert(END, i)
        
    else:
        lb3_value.set('')

def plot(event):
    global data
    
    selection = event.widget.curselection()
    if selection:
        
        #get file name
        index = selection[0]
        col = event.widget.get(index)
        
        # the figure that will contain the plot
        fig = Figure(figsize = (2, 2),
                      dpi = 100)
              
        # adding the subplot
        plot1 = fig.add_subplot(111)
      
        # plotting the graph
        plot1.plot(data[col])
      
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = window)  
        canvas.draw()
      
        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=5, column=1, columnspan=2)
      
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
      
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().grid(row=6, column=1, columnspan=2)    
    
    

window = Tk()
window.geometry('600x600')

dataset = IntVar()


lb1 = Label(window, text='Path')
lb1.grid(row=0, column=0)

button1 = Button(text="Browse", command=browse_button).grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


listbox1 = Listbox(window, width=30, height=10, selectmode=SINGLE)

button2 = Button(text="Open", command=list_filename).grid(row=0, column=4)

listbox1.grid(row=1, column=1, columnspan=2)
listbox1.bind('<<ListboxSelect>>', getElement)

scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=1, column=3, sticky="NS")
scrollbar1.config( command = listbox1.yview )

lb2 = Label(window, text='Name: ')
lb2.grid(row=2, column=0)

lb3_value = StringVar()
lb3 = Label(window, textvariable=lb3_value)
lb3.grid(row=2, column=1)

lb4 = Label(window, text='Column: ')
lb4.grid(row=3, column=0)

listbox2 = Listbox(window, width=30, height=5, selectmode=SINGLE)
listbox2.grid(row=3, column=1, columnspan=2)
listbox2.bind('<<ListboxSelect>>', plot)

lb5 = Label(window, text='Graph')
lb5.grid(row=4, column=1)




window.mainloop()



