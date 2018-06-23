# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:09:09 2018

@author: ymamo
"""
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import humanagent as ha
import resource as r 
import random 
import math
import itertools


'''
Creates instance of countries (society?)
country has a 
1. grid
2. N number of agents
3. An amount of resources
'''


class Countries(Model):
    
    
    def __init__(self, N, width, height, i):
        
        self.grid = MultiGrid(height, width, False)
        self.num_agents = N
        self.countrysched = RandomActivation(self)
        #to keep track of resources in an easier way may be unnecessary
        self.resources = []
        
        ####################################################
        #
        #  MAKES POPULATION FOR COUNTRY
        #
        ###################################################
        
        for i in range(self.num_agents):
            #creates instance of agent
            a = ha.HumanAgent(i, self)
            #adds agent to schedule of country
            self.countrysched.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            
        #################################################
        #
        # MAKES RESOURCES FOR COUNTRY
        #
        ###################################################
        
        #identify middle of grid
        size_r = int(width/2)
        #create an array of resources
        self.pos_res = self.make_resources(height, width, size_r)
              
        #creates instance of resources
        for i in range(size_r):
            # creates instance see resources module
            a = r.Resource(i, self, 5)
            # append to list in attirbutes (possibly unnecessary)
            self.resources.append([a,self.pos_res[i]])
            #place resource on grid
            self.grid.place_agent(a,self.pos_res[i])
        
        
    #Function to make locations of resources   
    def make_resources(self, height, width, size_r):
        pos = []   
        coords = list(itertools.combinations([x for x in range((size_r*-1), size_r+1)],2))
        midpoint = [int(width//2), int(height//2)]
        for i in range(len(coords)):
            p = (midpoint[0]+coords[i][0], midpoint[1]+coords[i][1])    
            pos.append(p)
            
        return pos
    
    
    # function which activates step function in Agent instance
    def step(self):
         self.countrysched.step()
        
            
            
            
        
        
     
        