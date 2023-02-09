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

# Set the window background color
root.configure(bg="light blue")


root.title("FEA ANALYSIS OF CANTILEVER BEAM USING PYTHON GUI")

My_label1=Label(root,text="CANTILEVER BEAM ANALYSIS BY FEA" ,  font=("Arial", 15 ) ,fg="white", bg="Black")
My_label1.grid(row=2,column=3)
root.geometry("1000x500")


My_label1=Label(root,text="LENGTH (mm)")
My_label1.grid(row=3,column=0)

My_label2=Label(root,text="FORCE (N)")
My_label2.grid(row=4,column=0)

My_label2=Label(root,text="Modulus Of Elasticity (N/mm²)")
My_label2.grid(row=5,column=0)

My_label3=Label(root,text="Width Of Beam (mm)")
My_label3.grid(row=6,column=0)

My_label4=Label(root,text="Depth Of Beam (mm)")
My_label4.grid(row=7,column=0)

My_label3=Label(root,text="Number Of Mesh Element")
My_label3.grid(row=8,column=0)


a=Entry(root,width=50,borderwidth=6)
a.grid(row=3,column=1, columnspan=3, padx=10,pady=10)


b=Entry(root,width=50,borderwidth=6)
b.grid(row=4,column=1, columnspan=3, padx=10,pady=10)


c=Entry(root,width=50,borderwidth=6)
c.grid(row=5,column=1, columnspan=3, padx=10,pady=10)


m=Entry(root,width=50,borderwidth=6)
m.grid(row=6,column=1, columnspan=3, padx=10,pady=10)

e=Entry(root,width=50,borderwidth=6)
e.grid(row=7,column=1, columnspan=3, padx=10,pady=10)

f=Entry(root,width=50,borderwidth=6)
f.grid(row=8,column=1, columnspan=3, padx=10,pady=10)

# Create a photoimage object of the image in the path
image1 = Image.open("C:/Users/SAFHAN/Downloads/beamwithstrainsensor.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=600, y=50)


def create_graph():
    global b
    L=float(a.get())
    P=float(b.get())
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



b1=Button(root,text="Graph",padx=50,pady=10 , fg="White" ,bg="black",command=create_graph)
b1.grid(row=10,column=0)
    

root.mainloop()
