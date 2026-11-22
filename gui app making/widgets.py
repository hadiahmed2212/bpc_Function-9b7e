from tkinter import *
from datetime import date
root=Tk()
root.title('Widgets.😊')
root.geometry("500x500")
lbl=Label(text= "Hi👋",fg="white", bg="#3FC553",height=1,width=300)

name_lbl=Label(text="Full name?", bg="#0412DB")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message= "Welcome to the app! \n today's date is: \n 😊"
    greet= "Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box= Text(height=3)
btn=Button(text="Begin",command=display,height=1, bg="blue",fg="white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()