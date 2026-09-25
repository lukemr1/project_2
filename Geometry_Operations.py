#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:25:01 2021

@author: kendrick shepherd
"""

import math
import numpy as np
import sys

# length of the beam
def Length(bar):
    vector = BarNodeToVector(bar.init_node,bar)
    length = VectorTwoNorm(vector)

    return length

# Find two norm (magnitude) of a vector
def VectorTwoNorm(vector):
    value = 0
    for val in vector:
        value += val**2
    return math.sqrt(value)

# Find a shared node between two bars
def FindSharedNode(bar_1,bar_2):
    return

# Given a bar and a node on that bar, find the other node
def FindOtherNode(node,bar):
    if bar.end_node == node:
        return bar.init_node
    elif bar.init_node == node:
        return bar.end_node
    else:
        sys.exit("The input node is not on the input bar.")

# Find a vector from input node (of the input bar) in the direction of the bar
def BarNodeToVector(origin_node,bar):
    [origin_x, origin_y] = origin_node.location
    other_node = FindOtherNode(origin_node,bar)
    [other_x, other_y] = other_node.location

    vec = [other_x - origin_x, other_y - origin_y]
    return vec

# Convert to bars that meet at a node into vectors pointing away from that node
def BarsToVectors(bar_1,bar_2):
    return

# Cross product of two vectors
def TwoDCrossProduct(vec1,vec2):
    return vec1[0] * vec2[1] - vec1[1] * vec2[0]


# Dot product of two vectors
def DotProduct(vec1,vec2):
    value = 0
    for i in range(0, len(vec1)):
        value += vec1[i] * vec2[i]
    return value

# Cosine of angle from local x vector direction to other vector
def CosineVectors(local_x_vec,other_vec):
    return DotProduct(local_x_vec,other_vec) / (VectorTwoNorm(local_x_vec) * VectorTwoNorm(other_vec))


# Sine of angle from local x vector direction to other vector
def SineVectors(local_x_vec,other_vec):
    return TwoDCrossProduct(local_x_vec,other_vec) / (VectorTwoNorm(local_x_vec) * VectorTwoNorm(other_vec))

# Cosine of angle from local x bar to the other bar
def CosineBars(local_x_bar,other_bar):
    return

# Sine of angle from local x bar to the other bar
def SineBars(local_x_bar,other_bar):
    return
