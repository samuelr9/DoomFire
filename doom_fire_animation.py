# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:21:19 2019
@author: Samuel Rocha
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Animation(object):
    def __init__(self):
        self.res = (80,50)
        self.initAnimationData()
        self.fig = plt.figure("Doom Fire",figsize=self.res)
        self.axe = self.fig.add_axes([0, 0, 1, 1], frameon=True)
        self.axe.set_xlim(0.5, self.res[1]-0.5), self.axe.set_xticks([])
        self.axe.set_ylim(0.5,self.res[0]-0.5), self.axe.set_yticks([])
        
    def runAnimation(self):
        self.renderAnimation()
        self.animation = FuncAnimation(self.fig,self.updateAnimationData,interval=10)
        plt.show()

    def renderAnimation(self):
        self.doom_fire_render = self.axe.imshow(self.doom_fire,interpolation='none',cmap=plt.cm.hot,vmin=self.fire_min,vmax=self.fire_max)

    def initAnimationData(self):
        np.random.seed(0)
        self.fire_min = 0
        self.fire_max = self.res[0]
        self.doom_fire = np.zeros(self.res,dtype=np.float32)
        self.doom_fire[0] = self.fire_max

    def updateAnimationData(self,frame):
        for i in range(self.res[0]-1,0,-1):
            fire_decay = np.zeros((1,self.res[1]),dtype=np.float32)
            for j in range(0,self.res[1]):
                fire_decay[0][j] = 3*np.random.random(1)[0]
                move_flame = np.random.randint(0,3)
                self.doom_fire[i][j-move_flame] = self.doom_fire[i-1][j] - fire_decay[0][j]
        self.doom_fire_render.set_data(self.doom_fire)
                
if __name__ == '__main__':
    doom_fire = Animation()
    doom_fire.runAnimation()
