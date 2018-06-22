# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:55:18 2018

@author: ymamo
"""

from mesa import Agent

class Resource(Agent):
    
    def __init__(self, unique_id, model, energy):
        super().__init__(unique_id, model)
        self.energy = energy