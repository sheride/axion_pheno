#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:35:06 2020

@author: elijahsheridan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Editables
file_name = 'selection_6.py'
divisions = [0, 1, 9]
labels = ['Signal', 'VBF BG', 'Double ISR BG']
colors = ['#698252', '#9b8e82', '#7a8e99']

# Variable setup
xBinning = None
xData = None
take_bins = True
data = []
xScale = None
yScale = None

# File parsing
file = open(file_name, "r")
for line in file:
    # Histogram binning
    if 'linspace' in line:
        start = line.find('(')
        end = line.find('d')
        vals = list(map(float, line[start+1:end-3].split(',')))
        a, b, c = vals
        c = int(c)
        xBinning = np.linspace(a, b, c, endpoint=True)
    # Middle of each bin (xData) and histogram heights (data)
    if 'array' in line:
        start = line.find('[')
        end = line.find(']')
        if take_bins:
            xData = np.array(list(map(float, line[start+1:end].split(','))))
            take_bins = False
        else:
            data.append(
                    np.array(list(map(float, line[start+1:end].split(',')))))
    # Plot axis labels
    if 'xlabel' in line:
        start = line.find('(')
        end = line.find(',')
        if '$' in line:
            xlabel = r'{}'.format(line[start+3:end-1])
        else:
            xlabel = r'${}$'.format(line[start+3:end-1])
    if 'ylabel' in line:
        start = line.find('(')
        end = line.find(',')
        ylabel = r'{}'.format(line[start+3:end-1])
    # x/y axis scales
    if 'set_xscale' in line and '#' not in line:
        if 'linear' in line:
            xScale = 'lin'
        else:
            xScale = 'log'
    if 'set_yscale' in line and '#' not in line:
        if 'linear' in line:
            yScale = 'lin'
        else:
            yScale = 'log'
file.close()

# Matplotlib plot setup
fig = plt.figure(figsize=(12, 6), dpi=80)
frame = gridspec.GridSpec(1, 1, right=0.7)
pad = fig.add_subplot(frame[0])

# Making plots
divisions.append(len(data))
for i in range(len(divisions) - 1):
    pad.hist(x=xData, bins=xBinning,
             weights=np.sum(data[divisions[i]:divisions[i+1]], axis=0),
             label=labels[i], histtype="step", rwidth=1.0, color=colors[i],
             edgecolor=colors[i], linewidth=4, bottom=None, cumulative=False,
             density=True, align="mid", orientation="vertical")

# Formatting plots
plt.rc('text', usetex=False)
plt.xlabel(xlabel, fontsize=16, color="black")
plt.ylabel(ylabel, fontsize=16, color="black")
if xScale == 'lin':
    plt.gca().set_xscale("linear")
else:
    plt.gca().set_xscale("log", nonposx="clip")
if yScale == 'lin':
    plt.gca().set_yscale("linear")
else:
    plt.gca().set_yscale("log", nonposy="clip")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
