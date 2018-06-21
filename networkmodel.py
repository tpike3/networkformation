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

class NetworkModel(Model):
    
    '''
    Model to create human fractal network formation form first principles
    
    
    '''
    
    def __init__(self, N, width, height):
        self.num_agents = N
        #self.grid = MultiGrid(height, width, True)
        #self.schedule = RandomActivation(self)
        #self.datacollector = DataCollector(
        #    model_reporters={"Gini": compute_gini},
        #    agent_reporters={"Wealth": "wealth"}
        #)
        # Create agents
        for i in range(self.num_agents):
            a = ha.HumanAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.running = True
        self.datacollector.collect(self)