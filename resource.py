# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 14:55:18 2018

@author: ymamo
"""

from mesa import Agent

'''
Creates and instance of the resources class
currently the resources do not do anything
just hold onto energy
'''


class Resource(Agent):
    
    def __init__(self, unique_id, model, energy):
        super().__init__(unique_id, model)
        self.energy = energy