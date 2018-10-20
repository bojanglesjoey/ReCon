#!/usr/bin/env python

# Reformats nc files for graphical representations
#
from StringIO import StringIO
from netCDF4 import Dataset
import os
from os import listdir
from os.path import isfile, join
import re
import csv

os.chdir("ACEFTS_L2_v3p6")
cwd = os.getcwd()
files = [f for f in listdir(cwd) if isfile(join(cwd, f))]

dataset = {}
for file in files:
    if file.endswith('.nc'):
        dataset = Dataset(file)
        print dataset.file_format
