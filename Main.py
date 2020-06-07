from math import sqrt, sin, cos, tan, pi, asin
import matplotlib.pyplot as plt



g = 9.81
Dt=0.1

p0x = 0
p0y = 0

v0 = 500
angle = 90

v0x = 0           #remplacer par cos de l'angle
v0y = 500            #remplacer par sin de l'angle

ax = 0
ay = -g

x = [p0x]
y = [p0y]

i=0

for n in range(0,300):
    vtx = v0x
    vty = v0y - g*Dt

    ptx = p0x + v0x*Dt
    pty = p0y + v0y*Dt - (g*Dt**2)/2

    p0x = ptx
    p0y = pty
    v0x = vtx
    v0y = vty
    i+=1

    x.append(ptx)
    y.append(pty)

    
        
    print (" ")
    print ("Temps en s = ", i*Dt)
    print ("ax= ",ax)
    print ("ay = ",ay)
    print ("vtx = ",vtx)
    print ("vty = ",vty)
    print ("ptx = ",ptx)
    print ("pty = ",pty)
    print (" ")

plt.plot(x,y)
plt.axhline(y=0, color = 'r')
plt.grid()


plt.show()
    




    

