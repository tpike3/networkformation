# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent
import resource as r 
import random




'''
Creates a instance of human agent
1 attirbute - wealth
2 functions move and step
'''
class HumanAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        # move in search of two with a vision of 2 grid sqaures in 360 degrees
        resource = False
        ##########################
        #  CHECK IF ON RESOURCE
        #########################
        #get cell contents
        contents = self.model.grid.get_cell_list_contents(self.pos)
        # iterate through cell list
        for c in contents:  
            if isinstance(c, r.Resource):
                print ("Agent on resource")
                resource = True
        #if on resource stay, if not move
        if resource == True: 
            pass
        #########################################
        # NO RESOURCES
        ##########################################
        else: 
            ###########################################
            # CHECK ALL CELLS - 2 levels (radius out)
            ########################################
            #get locations of all surrounding cells 2 layers
            possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False, radius = 2)
            #get contents of each cell
            for cell in possible_steps: 
                contents =  self.model.grid.get_cell_list_contents(cell)
                #################################################
                # CHECK FOR FOOD
                ####################################################
                for c in contents: 
                    if isinstance(c, r.Resource):
                        self.model.grid.move_agent(self, cell)
                        print ("found food")
                        resource = True
                        break
        ##############################################
        # NO FOOD MOVE RANDOMLY
        ################################################
        if resource == True: 
            pass
        else: 
            new_position = random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)
            print ("still looking")
                                            
    # step function agent ---only thing it odes is move                 
    def step(self):
        self.move()
        