# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:55:55 2023

@author: lucas
"""

import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
def clickMe():
    tkinter.messagebox.showinfo(title='say ur word',message="that hurts")
window.title("My first GUI code")

window.geometry('300x300')

label = tk.Label(window,text="My GUI")

label.pack()
entry = tk.Entry(window,width = 20)
entry.pack()
button = tk.Button(window,text = "button",command = clickMe)
button.pack()
window.mainloop()