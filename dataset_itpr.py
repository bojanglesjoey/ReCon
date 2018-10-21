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
    def init(self):
        # change dir and get all nc files
        os.chdir("ACEFTS_L2_v3p6")
        cwd = os.getcwd()
        files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
        self.d_names = {}
        for file in files:
            if file.endswith('.nc'):
                gas_name = file.split("_")
                self.d_names.update( {re.sub('\.nc$', '', gas_name[3]) : file} )

    def _read_nc_files(self, gas):
        dataset = Dataset(self.d_names[gas], mode='r')

        alt = dataset.variables['altitude'][:]                  # 150

        sunset_sunrise = dataset.variables['sunset_sunrise'][:] # 68791
        orbit = dataset.variables['orbit'][:]
        year = dataset.variables['year'][:]
        month = dataset.variables['month'][:]
        day = dataset.variables['day'][:]
        hour = dataset.variables['hour'][:]
        latitude = dataset.variables['latitude'][:]
        longitude = dataset.variables['longitude'][:]
        beta_angle = dataset.variables['beta_angle'][:]

        gas_conc = dataset.variables[gas][:,:]                  # 68791 x 150
        gas_error = dataset.variables[gas+"_error"][:,:]
        quality_flag = dataset.variables['quality_flag'][:,:]
        temp = dataset.variables['temperature'][:,:]
        temp_fit = dataset.variables['temperature_fit'][:,:]
        pressure = dataset.variables['pressure'][:,:]

        #mask outliers
        gas_conc = np.where(quality_flag != 0, None, gas_conc)

        return gas_conc, pressure, latitude


if __name__ == '__main__':
    obj = FormatNC()
    obj.init()
    d, p, l = obj._read_nc_files("CO2")
    print(d)
    print(p)
    print(l)
