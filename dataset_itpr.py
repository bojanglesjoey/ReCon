#!/usr/bin/env python

# Reformats nc files for graphical representations

from StringIO import StringIO
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
    def __init__(self, gases):
        os.chdir("ACEFTS_L2_v3p6")
        cwd = os.getcwd()
        files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
        self.d_names = {}

        for file in files:
            if file.endswith('.nc'):
                gas_name = file.split("_")
                self.d_names.update( {re.sub('\.nc$', '', gas_name[3]) : file} )

        for gas in gases:
            self._read_nc_files(gas)
        plt.show()

    def _read_nc_files(self, gas):
        dataset = Dataset(self.d_names[gas], mode='r')
        print gas
        print dataset.variables
        alt = dataset.variables['altitude'][:]
        sunset_sunrise = dataset.variables['sunset_sunrise'][:]
        orbit = dataset.variables['orbit'][:]
        year = dataset.variables['year'][:]
        month = dataset.variables['month'][:]
        day = dataset.variables['day'][:]
        hour = dataset.variables['hour'][:]
        latitude = dataset.variables['latitude'][:]
        longitude = dataset.variables['longitude'][:]
        beta_angle = dataset.variables['beta_angle'][:]
        gas_conc = dataset.variables[gas][:,75] #gas conc at alt 75
        gas_error = dataset.variables[gas+"_error"][:]
        quality_flag = dataset.variables['quality_flag'][:,75]
        temp = dataset.variables['temperature'][:]
        temp_fit = dataset.variables['temperature_fit'][:]
        pressure = dataset.variables['pressure'][:]

        for i in range(0,len(gas_conc)):
            if gas_conc[i] > 880 or gas_conc[i] < -880:
                gas_conc[i] = gas_conc[i-1]

        time = np.linspace(2004, 2018, 68791)
        self.plot_chart(gas, time, gas_conc)
        dataset.close()

    def plot_chart(self, gas, dfx, dfy):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(gas)
        ax.scatter(dfx, dfy, s=2)

if __name__ == '__main__':
    gases = []
    if len(sys.argv) < 2:
        print "Enter some gases!"
    else:
        for i in range(1,len(sys.argv)):
            gases.append(sys.argv[i])
        FormatNC(gases)
