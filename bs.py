# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:19:10 2020

@author: 1613098
"""


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
        self.size = abs((tr[1] - bl[1])*(tr[0] - bl[0]))
        
    def is_other_box_inside(self, other):
        inside_bl = other.bl[0] >= self.bl[0] and other.bl[1] >= self.bl[1]
        inside_tr = other.tr[0] <= self.tr[0] and other.tr[1] <= self.tr[1]
        
        return inside_bl and inside_tr
              
            
class Boxes():
    
    def __init__(self):
        self.land = list()
        self.all = list()
    def add(self, new_box):
        insides = [bi.is_other_box_inside(new_box) for bi in self.all]
        if sum(insides) % 2 == 0:
            self.land.append(new_box)
        
        self.all.append(new_box)
        
                
        
        
boxes = list(
            map(
                    lambda bi : Box(bl = (bi[0], bi[1]), tr = (bi[2], bi[3])), 
                    in_boxes
                    )
            )

boxes_by_size = sorted(boxes, key = lambda bi: -bi.size)

b = Boxes()

for boxi in boxes_by_size:
    b.add(boxi)


print(len(b.land))