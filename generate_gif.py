import numpy as np
import matplotlib.pyplot as plt
from utils import CPA
from matplotlib import cm

from PIL import Image # Use pillow to save all frames as an animation in a gif file


### Computations
x_v_CPA,d_c_CPA = CPA(np.array([0.8,1.2,1e-6]),10**4)

def f(x, y): #exponential cone definition
    return y*np.exp(x/y)

u, v = np.mgrid[-4:1e-4:200j, 0:1.2:200j]
x = u
y = v
z = f(x, y)

u2, v2 = np.mgrid[-4:4:200j, 0:1.28:200j]
x2 = u2
y2 = v2
z2 = np.zeros_like(x2)


### Display

# The amount of frames in the animation
frames = 71
c=0
c0=1
# Generate each frame
for n in range(frames//2 -10):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(azim=110 + frames//2 -c0, elev=20)
    ax.plot_surface(x, y, z,cmap = cm.Wistia,alpha=0.5,label='Exponential cone')
    ax.plot_surface(x2, y2, z2,cmap = cm.gray,alpha=0.5,label=r'Plane $z=0$')
    ax.scatter(np.array(x_v_CPA)[0,2],np.array(x_v_CPA)[0,1],np.array(x_v_CPA)[0,0],color='red',label ="CPA iterates",lw=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlim(-4,4)
    ax.set_ylim(0,1.3)
    ax.set_zlim(0,1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"gif_saves/{n}.png")
    plt.close()
    c0+=1

for n in range(-10 + frames//2,frames):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(azim=109 +10-c, elev=20)
    ax.plot_surface(x, y, z,cmap = cm.Wistia,alpha=0.5,label='Exponential cone')
    ax.plot_surface(x2, y2, z2,cmap = cm.gray,alpha=0.5,label=r'Plane $z=0$')
    ax.scatter(np.array(x_v_CPA)[0,2],np.array(x_v_CPA)[0,1],np.array(x_v_CPA)[0,0],color='red',label ="CPA iterates",lw=3)
    ax.plot(np.array(x_v_CPA)[:c//2,2],np.array(x_v_CPA)[:c//2,1],np.array(x_v_CPA)[:c//2,0],color='black')
    ax.scatter(np.array(x_v_CPA)[:c//2,2],np.array(x_v_CPA)[:c//2,1],np.array(x_v_CPA)[:c//2,0],color='red',lw=3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlim(-4,4)
    ax.set_ylim(0,1.3)
    ax.set_zlim(0,1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"gif_saves/{n}.png")
    plt.close()

    # Add 1 to the x so the sphere moves right by 1
    c += 1


images = [Image.open(f"gif_saves/{n}.png") for n in range(frames)]
images[0].save('gif_saves/render.gif', save_all=True, append_images=images[1:], duration=100, loop=0)