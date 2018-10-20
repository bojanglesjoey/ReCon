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
            self.read_nc_files(gas)
        plt.show()

    def read_nc_files(self, gas):
        dataset = Dataset(self.d_names[gas], mode='r')
        print gas
        gas_conc = dataset.variables[gas][:]
        years = dataset.variables['year'][:]
        months = dataset.variables['month'][:]
        long = dataset.variables['longitude'][:]
        lat = dataset.variables['latitude'][:]
        self.plot_chart(gas, months, gas_conc)
        print "\n"
        dataset.close()
        
    def plot_chart(self, gas, dfx, dfy):
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(gas)
        ax.plot(dfx, dfy)

if __name__ == '__main__':
    gases = []
    if len(sys.argv) < 2:
        print len(sys.argv)
        print "Enter some gases!"
    else:
        for i in range(1,len(sys.argv)):
            gases.append(sys.argv[i])
        FormatNC(gases)
