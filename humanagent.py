# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:22:09 2018

@author: ymamo
"""

from mesa import Agent


class HumanAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


    def step(self):
        self.move()
        