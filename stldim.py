#!/usr/bin/python

# stldim.py taken from
# https://www.reddit.com/r/3Dprinting/comments/7ehlfc/python_script_to_find_stl_dimensions/

# Python script to find STL dimensions
# Requrements: sudo pip install numpy-stl

import math
import stl
from stl import mesh
import numpy

import os
import sys

def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz

def get_z_height(filepath):
    main_body = mesh.Mesh.from_file(filepath)
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(main_body)

    return int(maxz - minz)