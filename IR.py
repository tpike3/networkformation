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
from itertools import product
from mesa.datacollection import DataCollector
import pandas as pd


class SocialDyn(Model):
    
    def __init__(self, N, R, width):
        
        ###################################
        # SET UP INFRASTRUCTURE
        ##################################
        self.running = True
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, width, True)
        self.positions = list(product([x for x in range(width)],repeat = 2))  
        ##########################################
        #  SET UP AGENTS - Resources and Countries
        #########################################
        for i in range(N): 
            a = c.Country(i, self)
            self.schedule.add(a)
            pos = self.get_position()
            self.grid.place_agent(a, pos)
        self.area_owned = R    
        for i in range(R): 
            res = r.Resource(i, self, random.randint(1,6), "")
            pos = self.get_position()
            self.grid.place_agent(res,pos)
        ##########################################
        # SET UP DATA COLLECTOR
        ###########################################
        self.datacollector = DataCollector(agent_reporters = {"Scaling A": "scaling_a" ,\
                                                              "Scaling B" : "scaling_b", \
                                                              "Capacity": "capacity", \
                                                              "Land Owned": "land_owned", \
                                                              "Conquered": "conquered"})
    
    def get_position(self):
        idx = random.randint(0, len(self.positions)-1)
        pos = self.positions[idx]
        if pos == None: 
            #print (idx, self.postions)
            stop
        self.positions.pop(idx)
        return pos
    
    def step(self): 
        #Make sure agents don't get too low
        for i in self.schedule.agents:
            if i.capacity < 50: 
                i.capacity = 50
        
        self.datacollector.collect(self)
        self.schedule.step()
        
           
'''
total_results = []
for x in range(1000):
    test = SocialDyn(4, 60, 10)
    #results = None
    print ("RUN ", x)
    for i in range(20): 
        #print ("STEP " ,  i,  "\n\n\n")
        test.step()
#
    results = test.datacollector.get_agent_vars_dataframe()
    total_results.append(results)
    
res2 = pd.concat(total_results)
res2.to_csv("single_results.csv")
'''    

            
       
        