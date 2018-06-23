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
    
    
    Instance of model creates N number of countries, with a population
    height and width and i (index in list of country instances)
    which will be used to specific what type of resources are in the country
    (i.e. hunter gather or agricultural)
    
    '''
    
    def __init__(self, N, C, width, height):
        #creates an instance of the activation schedule -- is just a list
        #which is reshuffled every time step
        self.schedule = RandomActivation(self)
        
        
        for i in range(C):
            #creates an instance of the country
            a = countries.Countries(N, width, height, i)
            #adds instance to schedule
            self.schedule.add(a)
            
        self.running = True
        #self.datacollector.collect(self)
        
    #Step function for network model instance    
    def step(self):
        
        self.schedule.step()