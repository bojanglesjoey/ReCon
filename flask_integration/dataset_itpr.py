#!/usr/bin/env python

# Reformats nc files for graphical representations

from io import StringIO
from netCDF4 import Dataset
import os
from os import listdir
from os.path import isfile, join
import sys
import re
import csv
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

class FormatNC():
    def __init__(self):
        # change dir and get all nc files
        os.chdir("/home/yukun/Projects/Hackathons/Data/ACEFTS_L2_v3p6")
        cwd = os.getcwd()
        files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
        self.d_names = {}
        for file in files:
            if file.endswith('.nc'):
                gas_name = file.split("_")
                self.d_names.update( {re.sub('\.nc$', '', gas_name[3]) : file} )

    def _read_nc_files(self, gas, *args):
        self.dataset = Dataset(self.d_names[gas], mode='r')
        
        #mask outliers
        output = []
        #print(self.dataset.variables)
        for i in args:
            if not i == "concentration":
                data = self.dataset.variables[i]
                if len(data.shape) == 2:
                    output.append(data[:100,:100])
                else:
                    output.append(data[:100])
            else:
                gas_conc = self.dataset.variables[gas][:100,:100]
                quality_flag = self.dataset.variables['quality_flag'][:100,:100]
                output.append(np.where(quality_flag != 0, None, gas_conc))
        return output


if __name__ == '__main__':
    obj = FormatNC()
    obj.init()
    d, p, l = obj._read_nc_files("CO2")
    print(d)
    print(p)
    print(l)
