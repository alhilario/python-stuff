#! /usr/bin/env python
# -*- coding: utf-8 -*-

def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
    else:
        return 0

def rental_car_cost(days):
    cost = days * 40
    if(days >= 7):
        return cost - 50
    elif(days >= 3 and days < 7):
        return cost - 20
    else:
        return cost

def trip_cost(city, days, spending_money):
    return plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days) + spending_money
    
print trip_cost("Los Angeles", 5, 600)
