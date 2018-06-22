# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:15:05 2018

@author: ymamo
"""

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import humanagent as ha
import countries

class NetworkModel(Model):
    
    '''
    Model to create human fractal network formation form first principles
    
    
    '''
    
    def __init__(self, N, C, width, height):
        self.schedule = RandomActivation(self)
        
        for i in range(C):
            a = countries.Countries(N, width, height, i)
            self.schedule.add(a)
            
        self.running = True
        #self.datacollector.collect(self)
        
        
    def step(self):
        self.schedule.step()