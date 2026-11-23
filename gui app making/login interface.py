from tkinter import *
root=Tk()
root.title('Sign Up')
root.geometry("400x400")

frame=Frame(master=root, height=200, width=360, bg= 'grey')
lbl1=Label(frame,text='Full Name?', bg='purple',fg='white',width=12)
lbl2=Label(frame,text='Email?', bg='purple',fg='white',width=12)
lbl3=Label(frame,text='Password', bg='purple',fg='white',width=12)
lbl4=Label(frame,text='⚠️Dont share your password with others⚠️', bg='red',fg='white',width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
pw_entry=Entry(frame,show='*')

def display():
    name=name_entry.get()
    greet="Hi "+name
    msg="\n New Account Made!"
    text_box.insert(END,greet)
    text_box.insert(END,msg)
text_box=Text(bg='Dark Green',fg='orange')
btn=Button(text='Create Account',command=display,bg='red')
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
lbl3.place(x=20,y=95)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pw_entry.place(x=150, y=140)
btn.place(x=130, y=210)
text_box.place(y=250)
root.mainloop()