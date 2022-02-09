
from tkinter import *
from turtle import width
from pyparsing import col

window=Tk()

def kg_conv():
   print(e1_value.get())
   grams=float(e1_value.get())*1000
   pounds=float(e1_value.get())*2.20462
   ounces=float(e1_value.get())*352.74
   t1.insert(END, grams) 
   t2.insert(END, pounds)
   t3.insert(END, ounces) 


#button
b1=Button(window, text="convert",command=kg_conv)
b1.grid(row=0,column=2)
#rowspan=0

#enter value
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

e2=Label(window,text="kg")
e2.grid(row=0,column=0)

#display text kg
t1=Text(window, height=1,width=20)
t1.grid(row=1,column=0)
t2=Text(window, height=1,width=20)
t2.grid(row=1,column=1)
t3=Text(window, height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()