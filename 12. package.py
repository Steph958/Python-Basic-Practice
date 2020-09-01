# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:32:38 2020

@author: USER
"""

#主程式
import geometry.point as gp   #geometry封包中的point模組
result = gp.dis(1,10,100,1000)
print("距離:",result)


import geometry.line as gs   #geometry封包中的line模組
result = gs.slope(1,10,100,1000)
print("斜率:",result)

