#Mini project group 12
#Group Members
#Saurabh Patil(2020116)
#Safhan Shirgaonkar(2020129)
#Mubeen Tambe(2020136)
#Samuel Freddy(2020156)


import tkinter
from tkinter import *
import numpy as np
from matplotlib import pyplot as plt
#creating a label widget
import math
from PIL import Image, ImageTk
root=Tk()
root.geometry("1350x700+0+0")
root.title("Cantilever Beam Analysis Software-Developed By Group 12 (Third Year Mini Project)")
title = Label(root, text="Cantilever Beam Analysis For Rectangular Cross-Section", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#badc57", fg="Black", relief=GROOVE)
title.pack(fill=X)
# Set the window background color
root.configure(bg="#badc57")


root.title("FEA ANALYSIS OF CANTILEVER BEAM USING PYTHON GUI")
'''
My_label1=Label(root,text="CANTILEVER BEAM ANALYSIS BY FEA" ,  font=("Arial", 15 ) ,fg="white", bg="Black")
My_label1.grid(row=2,column=3)
root.geometry("1000x500")
'''

exp_value = StringVar()
python_value = StringVar()
ansys_value = StringVar()
python_ansys=StringVar()
python_exp=StringVar()
exp_ansys=StringVar()
project_no=StringVar()
project_name=StringVar()
material_name=StringVar()

F1 = LabelFrame(root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1, text="Project Name:",  font=('times new roman', 15, 'bold'),bg="#badc57")
cname_lbl.grid(row=0, column=0, padx=20, pady=5)
cname_txt = Entry(F1, width=15, font='arial 15', bd=7, relief=GROOVE)
cname_txt.grid(row=0, column=1, pady=5, padx=10)

cphn_lbl = Label(F1, text="Material: ", bg="#badc57", font=('times new roman', 15, 'bold'))
cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
cphn_txt = Entry(F1, width=15, font='arial 15', bd=7, relief=GROOVE)
cphn_txt.grid(row=0, column=3, pady=5, padx=10)

c_bill_lbl = Label(F1, text="Project No: ", bg="#badc57", font=('times new roman', 15, 'bold'))
c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
c_bill_txt = Entry(F1, width=15,  font='arial 15', bd=7, relief=GROOVE)
c_bill_txt.grid(row=0, column=5, pady=5, padx=10)




 # =======================================================
F2 = LabelFrame(root, text="Python Value", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
F2.place(x=5, y=180, width=325, height=380)

My_label1=Label(F2, text="LENGTH (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label1.grid(row=0, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F2, text="FORCE (N)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=1, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F2, text="E (Mpa)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=2, column=0, padx=10, pady=10, sticky='W')

My_label3=Label(F2, text="Width (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label3.grid(row=3, column=0, padx=10, pady=10, sticky='W')

My_label4=Label(F2, text="Depth (mm)", font=('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
My_label4.grid(row=4, column=0, padx=10, pady=10, sticky='W')

My_label3=Label(F2, text="Mesh Elements", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label3.grid(row=5, column=0, padx=10, pady=10, sticky='W')


a=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
a.grid(row=0, column=1, padx=10, pady=10)


wb=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
wb.grid(row=1, column=1, padx=10, pady=10)


c=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
c.grid(row=2, column=1, padx=10, pady=10)

m=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
m.grid(row=3, column=1, padx=10, pady=10)

e=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
e.grid(row=4, column=1, padx=10, pady=10)

f=Entry(F2,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
f.grid(row=5, column=1, padx=10, pady=10)



F3 = LabelFrame(root, text="Experimental value", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
F3.place(x=340, y=180, width=325, height=380)

My_label1=Label(F3, text="LENGTH (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label1.grid(row=0, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F3, text="FORCE (N)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=1, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F3, text="E (Mpa)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=2, column=0, padx=10, pady=10, sticky='W')

My_label3=Label(F3, text="Width (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label3.grid(row=3, column=0, padx=10, pady=10, sticky='W')

My_label4=Label(F3, text="Guage Factor", font=('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
My_label4.grid(row=4, column=0, padx=10, pady=10, sticky='W')

My_label5=Label(F3, text="Input Volatge(V)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label5.grid(row=5, column=0, padx=10, pady=10, sticky='W')


My_label6=Label(F3, text="Output Volatge(V)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label6.grid(row=6, column=0, padx=10, pady=10, sticky='W')

#My_label7=Label(F3, text="", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
#My_label7.grid(row=7, column=0, padx=10, pady=10, sticky='W')

g=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
g.grid(row=0, column=1, padx=10, pady=10)


h=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
h.grid(row=1, column=1, padx=10, pady=10)


i=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
i.grid(row=2, column=1, padx=10, pady=10)

j=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
j.grid(row=3, column=1, padx=10, pady=10)

k=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
k.grid(row=4, column=1, padx=10, pady=10)

l=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
l.grid(row=5, column=1, padx=10, pady=10)

l1=Entry(F3,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
l1.grid(row=6, column=1, padx=10, pady=10)

#l2=Entry(F3,width=10)
#l2.grid(row=7, column=1, padx=10, pady=10)



F4 = LabelFrame(root, text="Ansys Value", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
F4.place(x=670, y=180, width=325, height=380)

My_label1=Label(F4, text="LENGTH (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label1.grid(row=0, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F4, text="FORCE (N)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=1, column=0, padx=10, pady=10, sticky='W')

My_label2=Label(F4, text="E (Mpa)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label2.grid(row=2, column=0, padx=10, pady=10, sticky='W')

My_label3=Label(F4, text="Width (mm)", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label3.grid(row=3, column=0, padx=10, pady=10, sticky='W')

My_label4=Label(F4, text="Depth (mm)", font=('times new roman', 16, 'bold'), bg = "#badc57", fg = "black")
My_label4.grid(row=4, column=0, padx=10, pady=10, sticky='W')

My_label3=Label(F4, text="Strain Value", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
My_label3.grid(row=5, column=0, padx=10, pady=10, sticky='W')


mo=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
mo.grid(row=0, column=1, padx=10, pady=10)

n5=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
n5.grid(row=1, column=1, padx=10, pady=10)


o=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
o.grid(row=2, column=1, padx=10, pady=10)

p5=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
p5.grid(row=3, column=1, padx=10, pady=10)

q5=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
q5.grid(row=4, column=1, padx=10, pady=10)

r=Entry(F4,width=10,font=('times new roman', 11, 'bold'), bd=5, relief=GROOVE)
r.grid(row=5, column=1, padx=10, pady=10)



F5 = Frame(root, bd=10, relief=GROOVE)
F5.place(x=1010, y=180, width=350, height=380)
 
bill_title = Label(F5, text="Results Area", font='arial 15 bold', bd=7, relief=GROOVE)
bill_title.pack(fill=X)
scroll_y = Scrollbar(F5, orient=VERTICAL)
txtarea = Text(F5, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH, expand=1)


F6 = LabelFrame(root, text="Strain Value Analysis", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#badc57")
F6.place(x=0, y=570, relwidth=1, height=140)
 
m1_lbl = Label(F6, text="Experimental Value", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
m1_txt = Entry(F6, width=18, textvariable=exp_value ,  font='arial 10 bold', bd=7, relief=GROOVE)
m1_txt.grid(row=0, column=1, padx=18, pady=1)
 
m2_lbl = Label(F6, text="Python Value", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
m2_txt = Entry(F6, width=18,textvariable=python_value,  font='arial 10 bold', bd=7, relief=GROOVE)
m2_txt.grid(row=1, column=1, padx=18, pady=1)
 
m3_lbl = Label(F6, text="Ansys Strain Value", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
m3_txt = Entry(F6, width=18, textvariable=ansys_value, font='arial 10 bold', bd=7, relief=GROOVE)
m3_txt.grid(row=2, column=1, padx=18, pady=1)
 
m4_lbl = Label(F6, text="Python & Exp diff", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
m4_txt = Entry(F6, width=18,textvariable=python_exp ,  font='arial 10 bold', bd=7, relief=GROOVE)
m4_txt.grid(row=0, column=3, padx=20, pady=1)
 
m5_lbl = Label(F6, text="Ansys & Exp diff", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
m5_txt = Entry(F6, width=18, textvariable=exp_ansys ,  font='arial 10 bold', bd=7, relief=GROOVE)
m5_txt.grid(row=1, column=3, padx=20, pady=1)
 
m6_lbl = Label(F6, text="Python & Ansys diff", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
m6_txt = Entry(F6, width=18, textvariable=python_ansys ,  font='arial 10 bold', bd=7, relief=GROOVE)
m6_txt.grid(row=2, column=3, padx=20, pady=1)


def create_graph():
    
    L=float(a.get())
    P=float(wb.get())
    E=float(c.get())
    b=float(m.get())
    d=float(e.get())
    n=int(f.get())
    el = float(L/n)
    ########------------Matrix formulation--------##########
    Force = np.array([[-P],[0]])
    F = np.zeros(2*n+2)
    F[2*n:1+2*n] = F[2*n:1+2*n]+Force[0]

    print("\nForce Matrix :")
    for i in F:
        print(i)



    kb = ((E*b*(d**3))/(12*(el**3)))*np.array([[12,6*el,-12,6*el],
                                    [6*el,4*el*el,-6*el,2*el*el],
                  [-12,-6*el,12,-6*el],[6*el,2*el*el,-6*el,4*el*el]])

    print("\nEliment stiffness matrix K = \n",kb)



    K = np.zeros((2+2*n,2+2*n))


    for i in range(4):
        for j in range(4):
            K[i,j]=kb[i,j]

    ##print(K)

    ###############-----------Assembly of stiffness matrix-----#########

    k=1
    while k<=2*n-2:
        p=k
        i=1
        while i<=4:
            j=1
            q=k
            while j<=4:
                K[p+1,q+1]=K[p+1,q+1]+kb[i-1,j-1]
                j=j+1
                q=q+1
            i=i+1
            p=p+1
        k=k+2

    ##print(K)

    #Matrix formulation


    Kinv = np.linalg.inv(K[2:2+2*n,2:2+2*n])
    ##print(Kinv)

    D = np.zeros((2+2*n))
    D[2:2+2*n] = np.dot(Kinv,F[2:2+2*n])

    print("\ndisp matrix : \n")
    for i in D:
        print(i)


    #########---------------Ploting------------$$$$$$$$$$$$%%%%

    x = np.arange(0,L+el,el)
    y = np.zeros((n+1))

    p=0
    for i in range(2+2*n):
        if i%2==0:
            y[p]=D[i]
            p=p+1


    plt.plot(x,y,"-r")
    plt.grid()
    plt.title("Deflection of cantilever beam with "+str(n)+" elements") 
    plt.xlabel("Length of Beam")
    plt.ylabel("Deflection")
    plt.savefig(""+str(n)+" Element.png")
    plt.show()
    slope,intercept = np.polyfit(x,y,1)
    print("The Value of Strain= " , slope)
    mt=slope
    python_value.set(slope)



def ansys_v():
    global mo
    L=float(mo.get())
    P=float(n5.get())
    E=float(o.get())
    b=float(p5.get())
    d=float(q5.get())
    n=float(r.get())
    
    ansys_value.set(n)

def exp_v():
    Vi=float(l.get())
    Vo=float(l1.get())
    gf=float(k.get())
    ip=gf*Vi
    strain_exp=(Vo/ip)
    exp_value.set(strain_exp)

def p_a():
    '''
    k1=str(python_value)
    k2=str(ansys_value)
    '''
    k1=float(m2_txt.get())
    k2=float(m3_txt.get())
    py_a=float(abs(k1-k2))
    python_ansys.set(py_a)
    
    
def p_e():
    k1=float(m2_txt.get())
    k2=float(m1_txt.get())
    py_e=abs(float(k1)-float(k2))
    python_exp.set(py_e)

def a_e():
    k1=float(m3_txt.get())
    k2=float(m1_txt.get())
    an_e=abs(float(k1)-float(k2))
    exp_ansys.set(an_e)

def results_area():
    k1=float(m2_txt.get())
    k2=float(m1_txt.get())
    k3=float(m3_txt.get())
    
    k4=float(m4_txt.get())
    k5=float(m5_txt.get())
    k6=float(m6_txt.get())
    
    txtarea.insert(END,f"\n Python Strain Value: {k1}")
    txtarea.insert(END,f"\n Exp Strain Value: {k2}")
    txtarea.insert(END,f"\n Ansys Strain Value: {k3}")
    
    if min(k4,k5)==k4:
        print("\n Min Value Diffrence is between python and exp")
        print(f"\n Min Diffrence:{k4}")
    
    elif min(k4,k5)==k5:
        print(f"\n Min Value Diffrence is between Ansys and exp")
        print(f"\n Min Diffrence:{k5}")

def welcome():
    m23=cname_txt.get()
    m33=c_bill_txt.get()
    m34=cphn_txt.get()
    
    txtarea.delete('1.0', END)
    txtarea.insert(END, "\tResults Of Strain Value")
    txtarea.insert(END, f"\nProject No.:{m33}")
    txtarea.insert(END, f"\nProject Name:{m23}")
    txtarea.insert(END, f"\nMaterial :{m34}")
    txtarea.insert(END, f"\n================================")


def exit_app():
     op = messagebox.askyesno("Exit", "Do you really want to exit?")
     if op > 0:
         root.destroy()

    

btn_f = Frame(F6, bd=7, relief=GROOVE)
btn_f.place(x=760, width=580, height=105)

total_btn = Button(btn_f, text="Submit",command=lambda:[create_graph(),ansys_v() ,exp_v(),p_a(),p_e(),a_e()] , bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
total_btn.grid(row=0, column=1, padx=5, pady=5)

generateBill_btn = Button(btn_f, text="Results",command=lambda:[create_graph(),results_area()], bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
generateBill_btn.grid(row=0, column=2, padx=5, pady=5)

clear_btn = Button(btn_f,  text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
clear_btn.grid(row=0, column=3, padx=5, pady=5)

exit_btn = Button(btn_f, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
exit_btn.grid(row=0, column=4, padx=5, pady=5)
bil_btn = Button(F1, text="Save", command=welcome(), width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
bil_btn.grid(row=0, column=6, pady=5, padx=10)
welcome()
'''
# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/SAFHAN/Downloads/beamwithstrainsensor.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=600, y=50)
'''


'''

b1=Button(root,text="Graph",padx=50,pady=10 , fg="White" ,bg="black",command=create_graph)
b1.grid(row=10,column=0)
    
'''

root.mainloop()
