# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:09:09 2018

@author: ymamo
"""
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import humanagent as ha
import resource 
import random 
import math
import itertools



class Countries(Model):
    
    
    def __init__(self, N, width, height, i):
        
        self.grid = MultiGrid(height, width, False)
        self.num_agents = N
        self.countrysched = RandomActivation(self)
        self.resources = []
        
        #add population of agents
        for i in range(self.num_agents):
            a = ha.HumanAgent(i, self)
            self.countrysched.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            
        #add agricultural agents to grid
        size_r = int(width/5)
        self.pos_res = self.make_resources(height, width, size_r)
              
        
        for i in range(size_r):
            a = resource.Resource(i, self, random.randint(2,11))
            self.resources.append([a,self.pos_res[i]])
            self.grid.place_agent(a,self.pos_res[i])
        
        
        
    def make_resources(self, height, width, size_r):
        pos = []
        
        coords = list(itertools.combinations([x for x in range((size_r*-1), size_r+1)],2))
        midpoint = [int(width//2), int(height//2)]
        for i in range(len(coords)):
            p = (midpoint[0]+coords[i][0], midpoint[1]+coords[i][1])    
            pos.append(p)
            
        return pos
            
        #for x in len(coords):
            
            
            
        
        
     
        