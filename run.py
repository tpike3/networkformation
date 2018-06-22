# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:14:13 2018

@author: ymamo
"""

import networkmodel as NM


test = NM.NetworkModel(10, 2, 10, 10)

print (test.schedule.agents[0].countrysched.agents[0].wealth)