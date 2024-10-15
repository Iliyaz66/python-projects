from tkinter import *
from random import randint

method=Tk()
method.title("My password generator")
method.iconbitmap("")
method.geometry("510x310")

my_password=chr(randint(32,125))
def new_rand():

    pw_entry.delete(0,END)

    pw_length=int(my_entry.get())
    my_passwor="$45t7123"
    for x in range(pw_length):
         my_password+=chr(randint(32,125))
    pw_entry.insert(0,my_password)

def clipper():
    method.clipboard_clear()
    method.clipboard_append(pw_entry.get())

lf=LabelFrame(method,text="how many characters?")
lf.pack(pady=20)

my_entry=Entry(lf,font=("Helvetica",24))
my_entry.pack(pady=20,padx=20)

pw_entry=Entry(method,text="",font=("Helvetica",24),bd=0,bg="systembuttonface")
pw_entry.pack(pady=20)

my_frame=Frame(method)
my_frame.pack(pady=20)

my_button=Button(my_frame,text="Generate a password",command=new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button=Button(my_frame,text="Copy To Clipboad",command=clipper)
clip_button.grid(row=0,column=1,padx=10)
                                    
method.mainloop()
