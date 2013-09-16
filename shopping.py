#! /usr/bin/env python
# -*- coding: utf-8 -*-

shopping_list = ["banana", "orange", "apple"]

stock = { "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = { "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    
    for o in food:
        if stock[o] > 0:
            stock[o] = stock[o] - 1
            total = total + prices[o]
    return total
            
