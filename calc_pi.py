#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate PI as 4 * sum of sqrt(1-x^2) between 0 and 1

Area of a quarter circle, using pythagoras to calculate size of strips of circle

Command line argument 

Created on Tue Mar 19 16:49:16 2019

@author: baz
"""

import sys, math

def run(width):
    x = 0.0
    sum = 0.0
    while x <= 1:
        sum += math.sqrt(1 - x*x) * width
        x += width
    return 4 * sum

if __name__ == "__main__":
    try:
        width = float(sys.argv[1])
        if width > 1:
            width = 1 / width
    except:
        width = 0.001
    print("PI = {}".format(run(width)))
    