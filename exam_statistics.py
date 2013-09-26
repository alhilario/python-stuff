#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

def grades_variance(scores, average):
    variance = 0
    for s in scores:
        variance += (average - s)**2
    return variance / len(scores)
   
vari = grades_variance(grades, grades_average(grades))

def grades_std_deviation(variance):
    hi = 0
    hi = math.sqrt(variance)
    return hi

print print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades, grades_average(grades))
print grades_std_deviation(vari)
