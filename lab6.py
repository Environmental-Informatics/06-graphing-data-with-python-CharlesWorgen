#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2020/4/20
by Charles Huang

Lab6 - Graphing Data with Python
The program should accept command line options with both complete input and
output filenames, then import data from the given file, generating three plots
in one figure, then ouput it as a pdf file with given name. When the code is 
first written, the file Tippecanoe_River_at_Ora.Annual_Metrics.txt is used.
Therefore, variable TROA is named after it.
"""

import numpy as np
import matplotlib.pyplot as plt
import sys


#1. Import data from file with given name
TROA = np.genfromtxt(sys.argv[1],
                     skip_header=0, names = True, #Use the first line as header
                     # Define the data type so that it matches
                     # the original file
                     dtype=["int","float","float","float","float","float",
                            "float"])

#2. Generate a single page with three plots using matplotlib
plt.figure(1)
ax = plt.subplot(311) #top plot
#Three lines for mean, max and min daily streamflow
plt.plot(TROA["Mean"], color="black", label="mean")
plt.plot(TROA["Max"], color="red", label="maximum")
plt.plot(TROA["Min"], color="blue", label="minimum")
plt.ylabel('Streamflow (cfs)')
# labeled with the values for years
plt.xticks(range(0,54,8),TROA["Year"][range(0,54,8)]) 
plt.legend(loc='upper left', frameon=True) #legend for the three lines

ax = plt.subplot(312) #middle plot
#Annual values of Tqmean, multiplied by 100%
plt.plot(TROA["Tqmean"]*100, 'bo') # Use blue circle to represent it
plt.ylabel('Tqmean (%)') # Indicates it is %
plt.xticks(range(0,54,8),TROA["Year"][range(0,54,8)])

ax = plt.subplot(313) #bottom plot
#A bar plot of R-B index
plt.bar(TROA["Year"],TROA["RBindex"]) 
plt.ylabel('R-B Index (ratio)') 
plt.xlabel('Year')

# Output the plots as a PDF file with given file name
plt.savefig(sys.argv[2])