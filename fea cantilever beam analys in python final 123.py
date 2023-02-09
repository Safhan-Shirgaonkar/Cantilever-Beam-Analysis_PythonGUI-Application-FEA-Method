

import numpy as np
from matplotlib import pyplot as plt


#Mini project group 12
#Group Members
#Saurabh Patil(2020116)
#Safhan Shirgaonkar(2020129)
#Mubeen Tambe(2020136)
#Samuel Freddy(2020156)

print("\n_____________  FEA Analysis of Cantilever Beam  ___________\n")
print('\n|               P\n|_______________\u2193\n|       L')



#Taking Input From User
L = float(input("\nEnter the length of the beam 'L' in mm: "))
P = float(input("Enter the magnitude of force 'P' in N: "))
E = float(input("Enter the modulous of elasticity 'E' of material in N/mm^2 :"))
print("\nRectangular Beam\n")
print("   Width\n ________\n|        |\n|        |\n|        |\
\n|        | Depth\n|        |\n|        |\n|        |\
\n|________|\n")

b = float(input("Enter the width of the beam in mm: "))
d = float(input("Enter the depth of the beam in mm: "))

print('\n|               P\n|_ _ _ _ _ _ _ _\u2193\n\
|\n  Number of pieces  \n    ')

n = int(input("Enter the number of mesh elements: "))

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


