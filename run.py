# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:14:13 2018

CSSS 2018

Project: 
Fractal Network Formation of Human Societies


Flow: 
    1. run creates an instance of the Network Model Class
    2. Network model creates 2 (2nd parameter) instances of the countries class (maybe rename society?)
    3. countries creates 10 (1st parameter) instances of agents and assigns them randomly to the 
        10 X 10 grid (3rd and 4th parameter)
    4. countries creates a grid of resources in center of grid base don input size

"""

import networkmodel as NM

# Paramters = Number of agents, number of countries, width and height of country
#create instance of NetworkModel class
test = NM.NetworkModel(10, 2, 10, 10)

#run instance of network model for N steps
for i in range(10):
    test.step()

#prints attribute of agent has to drill through all instances -
#to get the wealkth of one agent in one countries population in one country
# in the instance of the networkmodel 
print (test.schedule.agents[0].countrysched.agents[0].wealth)