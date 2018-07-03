# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:02:26 2018

@author: ymamo
"""

from mesa import Agent
import numpy as np
import resource as r
import random

class Country(Agent):
    
    def __init__(self, unique_id, model):
      
        super().__init__(unique_id, model) 
        self.scaling_a = 1
        self.scaling_b = 1
        self.capacity = np.random.randint(1,100)
        
       
    def negotiate(self, foreigner):
        
        #Foreigner 1 = [((x,y), object)]
        #Foreigner 2 = [(x,y), object, country_id on grid)]
        
        if len(foreigner[0]) == 2: 
            a = foreigner[0][1].unique_id
            
        elif len(foreigner[0]) == 3: 
            a = foreigner[0][2]
        
        other = self.model.schedule._agents[a]
        
        
        
        '''
        AVOID THE THRE PERSON FIGHT
        
        elif len(foreigner[0]) > 3:
        
            for i in foreigner[0][2:]:
                other = self.model.schedule._agents[i]
                print (other)
                print ("MORE THEN ONE TO FIGHT")
            
        '''
        
            
    
    
    def move(self): 
        
        
        best_move = [[],[]]
        
        
        neighbors = self.model.grid.get_neighborhood(self.pos, True)
        
        for cell in neighbors: 
            contents =  self.model.grid.get_cell_list_contents(cell)
            
            if len(contents) == 1 and isinstance(contents[0], r.Resource):
                    # Grid is not owned
                    if contents[0].owned == "":
                        if len(best_move[0]) == 0: 
                            best_move[0].append((cell, contents[0]))
                        else: 
                            if best_move[0][0][1].value < contents[0].value: 
                                best_move[0][0] = (cell, contents[0])
                                #print ("best replaced")
                    #grid cell is owned by you
                    elif contents[0].owned == self.unique_id:
                        pass
                    #grid cell is owned by someone else
                    elif contents[0].owned != self.unique_id: 
                        if len(best_move[1]) > 0: 
                            if best_move[1][0][1].value < item.value:
                                best_move[1][0] = (cell, contents[0])
                        else: 
                            best_move[1].append((cell, contents[0]))
            #if contents > 1 must be another country            
            if len(contents) > 1: 
                #account for situation where foreigner is on grid
                better = None
                country = False
                res = False
                for item in contents:                     
                    if type(item) is type(self):
                        #print (type(self))
                        #print (item.unique_id)
                        better = (item.unique_id,)
                        country = True
                    if isinstance(item, r.Resource):
                        res = True
                        if len(best_move[1]) > 0: 
                            #print (best_move[1][0])
                            if best_move[1][0][1].value < item.value:
                                best_move[1][0] = (cell, item)
                        else: 
                            best_move[1].append((cell,item))
                #to prevent issues of two countries being on same grid
                if country == True and res ==True: 
                    best_move[1][0] += better
                
        if len(best_move[0]) > 0: 
            #claim thy land
            best_move[0][0][1].owned = self.unique_id
            #move to new spot
            self.model.grid.move_agent(self, best_move[0][0][0])
            print ("Agent has seized resource ", best_move[0][0][1].value )
        elif len(best_move[1]) > 0 and len(best_move[1][0]) < 4:
            print (best_move[1])
            self.negotiate(best_move[1])
            print ("Too War!")
        else: 
            new_position = random.choice(neighbors)
            self.model.grid.move_agent(self, new_position)
            res = r.Resource(self.model.area_owned + 1, self.model, 0, self.unique_id)
            #iterate up the unique_id for resources
            self.model.area_owned += 1
            self.model.grid.place_agent(res, new_position)          
            print ("Agent has claimed ", new_position )
            
                    
                    
            
    
    def step(self): 
        self.move()
        #print (self.unique_id, " ", self.capacity)