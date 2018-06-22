# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent
import resource as r 
import random

class HumanAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        
        resource = False
        #check if agent is on resource
        contents = self.model.grid.get_cell_list_contents(self.pos)
        
        print (contents)           
        for c in contents:  
            #print (contents)
            if isinstance(c, r.Resource):
                print ("Agent on resource")
                resource = True
        if resource == True: 
            pass
        
        else: 
            next_move = []
            possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False, radius = 2)
            for cell in possible_steps: 
                if r.Resource in self.model.grid.get_cell_list_contents(cell):
                     self.model.grid.move_agent(self, cell)
                     print ("found food")
                else: 
                    new_position = random.choice(possible_steps)
                    self.model.grid.move_agent(self, new_position)
                                            
                     
        
    def step(self):
        self.move()
        