# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:33:42 2018

@author: ymamo
"""

from mesa import Agent
import random

class Resource(Agent): 
    
    def __init__(self, unique_id, model, value, owned): 
          super().__init__(unique_id, model)
          self.value = random.randint(0,5)
          self.owned = owned
          