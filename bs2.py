# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:19:10 2020

@author: 1613098
"""
import numpy as np
'''
in_boxes = [
        (0,0,2,2),
        (0,0,1,2),
        (1,0,2,2),
        
        ]

'''

in_boxes = [
        (1,1,10,6),
        (1.5,1.5,6,5),
        (2,2,3,3),
        (2,3.5,3,4.5),
        (3.5,2,5.5,4.5),
        (4,3.5,5,4),
        (4,2.5,5,3),
        (7,3,9.5,5.5),
        (7.5,4,8,5),
        (8.5,3.5,9,4.5),
        (3,7,8,10),
        (5,7.5,7.5,9.5),
        (5.5,8,6,9),
        (6.5,8,7,9),
        ]

class Box():
    
    def __init__(self, 
                 bl,
                 tr):
        
        self.bl = bl
        self.tr = tr
              
            
class World():
    
    def __init__(self,
                 max_x,
                 max_y, 
                 unit):
        
        assert 1/unit == int(1/unit)
        
        self.inv_unit = int(1/unit)
        self.grid = np.zeros((int(max_x/unit), int(max_y/unit)))
        self.colour = 0
        
    def _get_new_colour(self):
        self.colour += 1
        return self.colour
        
    def add(self, new_box):
        x_range = range(int(self.inv_unit*new_box.bl[0]), int(self.inv_unit*new_box.tr[0]))
        y_range = range(int(self.inv_unit*new_box.bl[1]), int(self.inv_unit*new_box.tr[1]))
        
        new_box_colour = self._get_new_colour()
        
        for i in x_range:
            for j in y_range:
                self.grid[i, j] = new_box_colour if self.grid[i, j] == 0 else 0
                
        print(self.grid)
                
    def land_colours(self):
        out = set(self.grid.reshape(-1))
        out.discard(0)
        return out
        
                
        
        
boxes = list(
            map(
                    lambda bi : Box(bl = (bi[0], bi[1]), tr = (bi[2], bi[3])), 
                    in_boxes
                    )
            )

max_x = max(bi.tr[1] for bi in boxes)
max_y = max(bi.tr[0] for bi in boxes)
w = World(max_x = max_x,
          max_y = max_y, 
          unit = 0.5)

for boxi in boxes:
    w.add(new_box= boxi)


l = w.land_colours()
print(len(l))

