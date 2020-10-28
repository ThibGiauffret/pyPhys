#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modélisation de l'influence du déphasage entre courant et tension sur 
la puissance instantanée et active (version animée)

Created on Thu Oct 22 13:17:35 2020
@author: Th. G, ensciences.fr
@license: Creative Commons CC-BY-NC-SA 4.0
"""

# Paquets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML, Image

# Mise en forme
rc('animation', html='html5')

fig, (ax, ax1) = plt.subplots(2)

l1, = ax.plot([], [], lw=2, label="Tension (en V)", color="tab:blue")
l2, = ax.plot([], [], lw=2, label="Intensité (en A)", color="tab:green")
l3, = ax1.plot([], [], lw=2, label="Puissance instantannée", color="tab:red")
l4, = ax1.plot([], [], lw=2, label="Puissance active", color="tab:orange")
l5, = ax1.plot([], [], lw=2, label="Puissance apparente", color="tab:purple")

ax.set_xlim(0, 1)
ax.set_ylim(-6,6)

ax1.set_xlim(0, 1)
ax1.set_ylim(-6,6)

ax1.set_xlabel("Temps (en s)")
ax1.set_ylabel("Puissance (W)")
ax1.grid()

ax.set_xlabel("Temps (en s)")
ax.set_ylabel("Amplitude")
ax.grid()

# Mise en forme de la légende
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5),
          fancybox=True, shadow=True, ncol=1)

ax1.legend(loc='center left', bbox_to_anchor=(1.02, 0.5),
          fancybox=True, shadow=True, ncol=1)


# Initialisation
def init():
    l1.set_data([], [])
    l2.set_data([], [])
    l3.set_data([], [])
    l4.set_data([], [])
    l5.set_data([], [])
    return (l1,l2,l3,l4,l5)

# Animation
def animate(i):
    t = np.arange(0.0, 1.0, 0.001)
    a0 = 5
    f0 = 3
    s1 = a0 * np.sin(2 * np.pi * f0 * t)
    l1.set_data(t, s1)
    
    a1 = 1
    f1 = 3
    
    phi = i*0.1
    s2 = a1 * np.sin(2 * np.pi * f1 * t + phi)
    l2.set_data(t, s2)
    
    s3=[]
    moyenne = 0
    
    for i in range(len(s1)):
        s3.append(s1[i]*s2[i])
        
    l3.set_data(t, s3)
    
    s4 = []
    moyenne = np.mean(s3)
    s4 = [moyenne] * len(s1)
        
    l4.set_data(t, s4)
    
    s5 = []
    moy_apparente = np.mean(a0 * np.sin(2 * np.pi * f0 * t) * a1 * np.sin(2 * np.pi * f1 * t))
    s5 = [moy_apparente] * len(s1) 
    
    l5.set_data(t, s5)

    return (l1,l2,l3,l4,l5)



# Sauvegarde de l'animation
fig.tight_layout()
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=100,
                              save_count=64, blit=True)
anim.save('./animation.gif', writer='imagemagick', fps=25, dpi=150)
plt.show()
