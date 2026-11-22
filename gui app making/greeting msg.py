from tkinter import *
from datetime import date
from datetime import datetime

root=Tk()
root.title("hi!")
root.geometry("400x300")
heading=Label(text="participant name",fg="white",bg="#072F5F",height=1,width=300)
name_label=Label(text="Participant Name",bg="#3895D3")
name_entry= Entry()

time_label = Label(root)
time_label.pack()
def display_welcome():
    name = name_entry.get()
    text_box.delete(1.0, END)
    greeting = "hello " + name + "!\n"
    msg = "welcome to the workshop!\n"
    workdate = "Date Today: " + str(date.today()) + "\n"
    now = "Time: " + datetime.now().strftime("%H:%M:%S")
    text_box.insert(END, greeting)
    text_box.insert(END, msg)
    text_box.insert(END, workdate)
    text_box.insert(END, now)
text_box= Text(height=4,width=40)
welbut= Button(text="check in.",command=display_welcome,height=1,bg="#1261A0", fg="white")

heading.pack()
name_label.pack(pady=10)
name_entry.pack()
welbut.pack(pady=10)
text_box.pack()
root.mainloop()
