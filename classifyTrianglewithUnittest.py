#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tonya Thompson - SSW567-NBA
Assignment - HW 01: Testing triangle classification 02/12/21:
Attemp at unit testing 

"""

import unittest

try:

    def classify_triangle(side1, side2, side3):
        if side1 == side2 == side3:
            #print("\nEquilateral Triangle") 
            return ('Equilateral Triangle')
        elif ((side1**2 + side2**2) == side3**2):
            #print("\nRight Triangle")
            return('Right Triangle')
        elif side1==side2 or side2==side3 or side3==side1:
            #print("Isosceles Triangle")
            return('Isosceles Triangle')
        else:
            #print("Scalene Triangle")
            return('Scalene Triangle')
         
   # side1,side2,side3 = map(int,input("Enter three sides of an triangle: ").split())
   # classify_triangle(side1,side2,side3) 

except ValueError as err:
    print("ERROR: " +str(err))

class TestTriangle(unittest.TestCase):

    def test1(self):
        #print("\nEquilateral Triangle") 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral Triangle','1,1,1 is a Equilateral triangle')
        #print("\nRight Triangle")
        self.assertEqual(classify_triangle(3,4,5),'Right Triangle','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(3,5,5),'Isosceles Triangle','3,5,5 is a Isosceles triangle')
        

if __name__ == '__main__':
   unittest.main()