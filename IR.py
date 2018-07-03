# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 12:59:49 2018

@author: ymamo
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import country as c
import resource as r
import random 


class SocialDyn(Model):
    
    def __init__(self, N, R, height, width):
        
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(height, width, True)
        for i in range(N): 
            a = c.Country(i, self)
            self.schedule.add(a)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        self.area_owned = R    
        for i in range(R): 
            res = r.Resource(i, self, random.randint(1,6), "")
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(res, (x, y))
            
    def step(self): 
        
        self.schedule.step()
        
        
        
test = SocialDyn(20, 20, 10, 10)


for i in range(1): 
    test.step()
            
        
        