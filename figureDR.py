import numpy as np
import matplotlib.pyplot as plt

from utils import DR

### Initialization

x_0 = np.array([1,1,1]) #format [z,y,x]

### Computations


#DR iterates
x_DR,d_DR,y_DR,d_y_DR = DR(x_0,10**2)

#Intersection C
u = np.linspace(-5,0)
x = u
y = [0]*len(u)
z = [0]*len(u)




### Display

#Figure 1
fig = plt.figure()
ax = plt.axes(projection='3d')


ax.plot3D(x, y, z,label=r'$C= K_{exp} \cap V_2$')
ax.scatter(x_0[2],x_0[1],x_0[0],color='black',label="Starting point")
ax.scatter(np.array(x_DR)[:,2],np.array(x_DR)[:,1],np.array(x_DR)[:,0],color='green',label =r'$x_k$')
ax.scatter(np.array(y_DR)[:,2],np.array(y_DR)[:,1],np.array(y_DR)[:,0],color='red',label =r'$y_k$')


# Can set your view from different angles
ax.view_init(azim=10, elev=10)
ax.set_zlim(-1,1)
ax.set_ylim(-0.25,1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.title("DR, starting (1,1,1)")
plt.legend()
plt.show()



#Figure 2
plt.figure()
k=np.linspace(1,len(d_DR)-1,len(d_DR)-1)

"""
plt.loglog(k,k**(-0.2),color='black',label=r"$k^{-0.2},k^{-0.3},k^{-0.4}, k^{-0.5}$")
plt.loglog(k,k**(-0.5),color='black')
plt.loglog(k,k**(-0.4),color='black')
plt.loglog(k,k**(-0.3),color='black')
"""
plt.semilogx(k[:len(d_DR)-1],d_DR[1:],color='green',label=r"$d_C(x_k)$")
plt.semilogx(k[:len(d_y_DR)-1],d_y_DR[1:],color='red',label=r"$d_C(y_k)$")


plt.xlabel("k")
plt.ylabel(r'$d_C(x_k),d_C(y_k)$')
plt.ylim(0,d_DR[0])
plt.title("DR, starting (1,1,1)")
plt.legend()
plt.show()
