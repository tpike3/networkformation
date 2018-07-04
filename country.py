# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:02:26 2018

@author: ymamo
"""

from mesa import Agent
import numpy as np
import resource as r
import numpy as np
import random 

class Country(Agent):
    
    def __init__(self, unique_id, model):
      
        super().__init__(unique_id, model) 
        self.scaling_a = 1
        self.scaling_b = 1
        self.capacity = np.random.randint(50,100)
        self.land_owned = []
        self.conquered = []
        
       
    def move_loser(self):
        
        if self.pos in self.land_owned: 
            self.land_owned.remove(self.pos)
        neighbors = self.model.grid.get_neighborhood(self.pos, True)
        
        for cell in neighbors: 
            moved = False
            contents =  self.model.grid.get_cell_list_contents(cell)
            
            if len(contents) == 1 and isinstance(contents[0], r.Resource):
                if contents[0].owned == self.unique_id: 
                    self.model.grid.move_agent(self, cell)
                    moved = True
                elif contents[0].owned == "":
                    self.model.grid.move_agent(self, cell)
                    moved = True
                    contents[0].owned = self.unique_id
                    self.land_owned.append(cell)
            
            elif len(contents) == 0: 
                self.model.grid.move_agent(self, cell)
                moved = True
                res = r.Resource(self.model.area_owned + 1, self.model, 0, self.unique_id)
                #iterate up the unique_id for resources
                self.model.area_owned += 1
                self.model.grid.place_agent(res, cell)  
                self.land_owned.append(cell)
                
        if moved == False: 
            #print ("NOWHERE TO GO I SURRENDER")
            #conquered --remove form schedule
            #self.model.schedule.remove(self)
            #remove from grid
            #self.model.grid.remove_agent(self)
            self.conquered.append(cell)
            #pass
            
         
    
    
    def negotiate(self, foreigner):
        
        #Data Structures
        #Foreigner 1 = [((x,y), object)]
        #Foreigner 2 = [(x,y), object, country_id on grid)]
        defect1 = 0
        defect2 = 0
        
        if len(foreigner[0]) == 2: 
            res = foreigner[0][1]
            a = foreigner[0][1].owned
            pos = foreigner[0][0]
            
        elif len(foreigner[0]) >= 3: 
            a = foreigner[0][2]
            pos = foreigner[0][0]
            res = foreigner[0][1]
            
        #print (foreigner)
        other = self.model.schedule._agents[a]
        
        #Engage in negotiations
        if np.random.uniform(0,1) > np.random.beta(self.scaling_a, self.scaling_b):
            defect1 = 1
        if np.random.uniform(0,1) > np.random.beta(other.scaling_a, other.scaling_b):
            defect2 = 1
        
        #####################################################################
        #
        #  If  both defect
        #
        ####################################################################
        
        if defect1 == 1 and defect2 == 1: 
            fight1 = np.random.randint(1,self.capacity)
            fight2 = np.random.randint(1,other.capacity)
            self.scaling_b += 1
            other.scaling_b += 1
            if fight1 >= fight2:
                #update agents
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                #update resources
                res.owned= self.unique_id
                #take over land
                self.land_owned.append(pos)
                self.model.grid.move_agent(self, pos)
                #reduce loser holdings
                other.move_loser()
            else: 
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                res.owned = other.unique_id
        
        ##################################################################
        #
        # If initiator defects and recipient cooperates
        #
        ##################################################################
        
        elif defect1 == 1 and defect2 == 0:
            fight1 = np.random.randint(1,self.capacity)
            fight2 = np.random.randint(1,other.capacity) * 0.9
            self.scaling_b += 1
            other.scaling_b += 1
            if fight1 >= fight2:
                #update agents
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                #update resources
                if a is type(r.Resource): 
                    a.owned = self.unique_id
                self.model.grid.move_agent(self, pos)
                other.move_loser()
            else: 
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                if a is type(r.Resource): 
                    a.owned = other.unique_id
        
        ##################################################################
        #
        # If initiator cooperates and recipient defects
        #
        ##################################################################            
        
        
        elif defect1 == 0 and defect2 == 1:
            fight1 = np.random.randint(1,self.capacity) * 0.9
            fight2 = np.random.randint(1,other.capacity)
            self.scaling_b += 1
            other.scaling_b += 1
            if fight1 >= fight2:
                #update agents
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                #update resources
                if a is type(r.Resource): 
                    a.owned = self.unique_id
                self.model.grid.move_agent(self, pos)
                other.move_loser()
            else: 
                self.capacity += random.randint(-5, 5)
                other.capacity += random.randint(-5,5)
                if a is type(r.Resource): 
                    a.owned = other.unique_id
        
        ##################################################################
        #
        # If both cooperate
        #
        ################################################################## 
        
        elif defect1 == 0 and defect2 == 0:
            self.capacity += random.randint(1, 4)
            other.capacity += random.randint(1,4)
            self.scaling_a += 1
            other.scaling_a += 1
                
                    
     
    
    def move(self): 
        
        
        best_move = [[],[], [], []]
        
        
        neighbors = self.model.grid.get_neighborhood(self.pos, True)
        
        for cell in neighbors: 
            contents =  self.model.grid.get_cell_list_contents(cell)
            
            #get list of possible moves with no one
            if len(contents) == 0: 
                best_move[2].append(cell)
            
            elif len(contents) == 1 and isinstance(contents[0], r.Resource):
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
                        best_move[3].append((cell, contents[0]))
                    #grid cell is owned by someone else
                    elif contents[0].owned != self.unique_id and contents[0].owned != "": 
                        if len(best_move[1]) > 0: 
                            if best_move[1][0][1].value < contents[0].value:
                                best_move[1][0] = (cell, contents[0])
                        else: 
                            best_move[1].append((cell, contents[0]))
            #if contents > 1 must be another country            
            elif len(contents) > 1: 
                #print (len(contents), contents)
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
                else: 
                    print ("ISSUES ", contents)
                
        if len(best_move[0]) > 0: 
            #claim thy land
            best_move[0][0][1].owned = self.unique_id
            #move to new spot
            self.model.grid.move_agent(self, best_move[0][0][0])
            #print ("Agent has seized resource ", best_move[0][0][1].value )
            self.land_owned.append(best_move[0][0][0])
        
        elif len(best_move[1]) > 0 and len(best_move[0]) == 0: 
            #print (best_move[1])
            self.negotiate(best_move[1])
            #print ("Too War!")
                            
        elif len(best_move[2]) > 0: 
            self.model.grid.move_agent(self, best_move[2][0])
            res = r.Resource(self.model.area_owned + 1, self.model, 0, self.unique_id)
            #iterate up the unique_id for resources
            self.model.area_owned += 1
            self.model.grid.place_agent(res, best_move[2][0])  
            self.land_owned.append(best_move[2][0])
            #print ("Agent has claimed ", best_move[2][0] )
        else: 
            self.model.grid.move_agent(self, best_move[3][0][0])
            #print ("Agent has moved in own territory ", best_move[3][0] )
            
                    
                    
            
    
    def step(self): 
        #print (type(self), self.pos)
        self.move()
        
        #print (self.unique_id, " ", self.capacity)