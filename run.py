# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:41:08 2018

@author: ymamo
"""

from mesa.batchrunner import BatchRunner
from IR import SocialDyn


'''

    TO RUN the model with batch runner type in anything but "single"
    else it will run 4 countries for 60 step in a 10 X 10 grid for 1000
    runs
'''


def run_model(method): 
    if method == "single": 
        total_results = []
        for x in range(1000):
            test = SocialDyn(4, 60, 10)
            #results = None
            print ("RUN ", x)
            for i in range(20): 
                #print ("STEP " ,  i,  "\n\n\n")
                test.step()
        #
            results = test.datacollector.get_agent_vars_dataframe()
            total_results.append(results)
            
        res2 = pd.concat(total_results)
        res2.to_csv("single_results.csv")


    else: 

        variable_params = {"width": range(10, 25, 5), "N": range(10, 50, 10), "R": range(10,50,10)}
        
        batch_run = BatchRunner(SocialDyn,
                                fixed_parameters=None,
                                variable_parameters=variable_params,
                                iterations=5,
                                max_steps=100,
                                agent_reporters = {"Scaling A": 'scaling_a' ,\
                                                   "Scaling B" : 'scaling_b', \
                                                    "Capacity": 'capacity', \
                                                    "Land Owned": 'land_owned', \
                                                    "Conquered": 'conquered'})
        batch_run.run_all()

        
        results = batch_run.get_agent_vars_dataframe()
        results.to_csv("results.csv")


'''
EXECUTION FUNCTION TO RUN THE MODEL
'''      
        
        
run_model("single")