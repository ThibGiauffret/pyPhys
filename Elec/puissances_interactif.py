#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modélisation de l'influence du déphasage entre courant et tension sur 
la puissance instantanée et active (version interactive)

Created on Thu Oct 22 13:18:43 2020
@author: Th. G, ensciences.fr
@license: Creative Commons CC-BY-NC-SA 4.0
"""

# Paquets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# Mise en forme et calcul des points
fig, (ax, ax1) = plt.subplots(2)
plt.subplots_adjust(bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s1 = a0 * np.sin(2 * np.pi * f0 * t)
l1, = ax.plot(t, s1, lw=2, color="tab:blue", label="Tension (en V)")

a1 = 1
f1 = 3

phi0 = 0.7
s2 = a1 * np.sin(2 * np.pi * f1 * t + phi0)
l2, = ax.plot(t, s2, lw=2, color="tab:green", label="Intensité (en A)")

s3=[]
moyenne = 0

for i in range(len(s1)):
    s3.append(s1[i]*s2[i])
    
l3, = ax1.plot(t, s3, lw=2, color="tab:red", label="Puissance instantannée")

s4 = []
moyenne = np.mean(s3)
s4 = [moyenne] * len(s1)
    
l4, = ax1.plot(t, s4, lw=2, color="tab:orange", label="Puissance active")

s5 = []
moy_apparente = np.mean(a0 * np.sin(2 * np.pi * f0 * t) * a1 * np.sin(2 * np.pi * f1 * t))
s5 = [moy_apparente] * len(s1) 
    
l5, = ax1.plot(t, s5, lw=2, label="Puissance apparente", color="tab:purple")

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


# Mise en forme des légendes
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5),
          fancybox=True, shadow=True, ncol=1)

ax1.legend(loc='center left', bbox_to_anchor=(1.02, 0.5),
          fancybox=True, shadow=True, ncol=1)



ax.margins(x=0)

# Slider déphasage

axcolor = 'lightgoldenrodyellow'
axdephasage = plt.axes([0.67, 0.65, 0.25, 0.03], facecolor=axcolor)


dephasage = Slider(axdephasage, '$\Delta \phi$', 0, 10.0, valinit=phi0)


def update(val):
    phi = dephasage.val
    s1 = a0*np.sin(2*np.pi*f0*t)
    s2 = a1*np.sin(2*np.pi*f0*t+phi)
    s3 = s1*s2
    moyenne = np.mean(s3)
    s4 = [moyenne] * len(s1)
    l1.set_ydata(s1)
    l2.set_ydata(s2)
    l3.set_ydata(s3)
    l4.set_ydata(s4)
    fig.canvas.draw_idle()


dephasage.on_changed(update)

# Bouton Reset

resetax = plt.axes([0.67, 0.58, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    dephasage.reset()
button.on_clicked(reset)

fig.tight_layout()


plt.show()
