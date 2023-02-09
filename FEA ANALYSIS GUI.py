from tkinter import *
root=Tk()



root.title("FEA ANALYSIS OF CANTILEVER BEAM USING PYTHON GUI")

My_label1=Label(root,text="REGISTRATION FORM" , fg="red", bg="yellow")
My_label1.grid(row=0,column=1)


My_label1=Label(root,text="Enter Your Name")
My_label1.grid(row=1,column=0)

My_label2=Label(root,text="Enter your Form No.")
My_label2.grid(row=2,column=0)

My_label2=Label(root,text="Email")
My_label2.grid(row=3,column=0)

My_label3=Label(root,text="Enter Your Marks in percentage")
My_label3.grid(row=4,column=0)


a=Entry(root,width=50,borderwidth=6)
a.grid(row=1,column=1, columnspan=3, padx=10,pady=10)

b=Entry(root,width=50,borderwidth=6)
b.grid(row=2,column=1, columnspan=3, padx=10,pady=10)

c=Entry(root,width=50,borderwidth=6)
c.grid(row=3,column=1, columnspan=3, padx=10,pady=10)

d=Entry(root,width=50,borderwidth=6)
d.grid(row=4,column=1, columnspan=3, padx=10,pady=10)


def button_submit():
    l=[a,b,c,d]
    for i in l:
        i.delete(0,END)
    My_label4=Label(root,text="Form Submitted Sucessfully",fg="green")
    My_label4.grid(row=7,column=0)
    

def button_info():
    My_label5=Label(root,text="The form is Registeration form,the form once filled and verified, after that no details will be changed,After filling all details check all deatails and click on submit button ",bg="yellow")
    My_label5.grid(row=6,column=0)
#buttons creating
b1=Button(root,text="Submit",padx=50,pady=10 , fg="red" ,bg="yellow",command=button_submit)
b2=Button(root,text="Information",padx=50,pady=10 , fg="red", bg="yellow",command=button_info)

b1.grid(row=5,column=0)
b2.grid(row=5,column=1)





root.mainloop()
