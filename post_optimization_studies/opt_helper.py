#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 00:15:17 2020

@author: elijahsheridan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from lxml import html
import pandas as pd
import seaborn as sb
import plotly.graph_objs as go
import matplotlib.patches as mpatches
import os


def gen_histo(file_name, divisions, out_file_name=None, norm_one=True,
              labels=None, ylabel=None, colors=None, logx=False, logy=False,
              save=False, bins=None, binResize=False, xlabel=None, min_x=None,
              max_x=None):
    """
    Takes a histogram-generating .py file returned by a MadAnalysis analysis
    and converts the plot with custom groupings of data files such that each
    group is normed to one.

    file_name - string, path to python file to extract data from
                    (e.g., .Output/Histos/ ... /selection_0.py)
    divisions - list of integers, each integer marking the beginning index of a
                    set of input files to combine
    plot_name - string, name of .png file containing saved plot
    labels    - list of strings (same length as divisions) giving names for the
                    histogram lines
    colors    - list of strings representing valid matplotlib colors with same
                length as number of divisions, giving colors for histogram
                lines
    logx      - boolean indicating whether a log scale should be used for x
                    axis
    logy      - boolean indicating whether a log scale should be used for y
                    axis
    save      - boolean indicating whether histogram should be saved
    bins      - number of bins in the histogram, if default not desired (should
                divide default?)
    binResize - boolean indicating if bins should be resized to 1/binsize
    xlabel    - label for histogram x axis
    min_x     - x value at which histogram is begun
    max_x     - x value at which histogram is ended
    """

    file_name = file_name
    out_file_name = out_file_name or 'plot'
    labels = labels or ['Plot ' + str(i) for i in range(len(divisions))]
    colors = colors or ['#698252', '#9b8e82', '#7a8e99', '#a9935e', '#c7aec5']

    # Variable setup
    xBinning = None
    xData = None
    take_bins = True
    data = []
    xlabel = xlabel or None

    # File parsing
    file = open(file_name, "r")
    for line in file:
        # Histogram binning
        if 'linspace' in line and not bins:
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
                xData = np.array(
                        list(map(float, line[start+1:end].split(','))))
                take_bins = False
            else:
                data.append(
                        np.array(list(map(float,
                                          line[start+1:end].split(',')))))

        # Plot axis labels
        if 'xlabel' in line and not xlabel:
            start = line.find('(')
            end = line.find('",')
            if '$' in line:
                xlabel = r'{}'.format(line[start+3:end])
            else:
                xlabel = r'${}$'.format(line[start+3:end])
    file.close()

    if bins:
        xBinning = bins

    if xlabel:
        xlabel = xlabel

    # Matplotlib plot setup
    fig = plt.figure(figsize=(12, 6), dpi=80)
    frame = gridspec.GridSpec(1, 1, right=0.7)
    pad = fig.add_subplot(frame[0])

    # Combining data
    divisions.append(len(data))
    combined_data = [np.sum(data[divisions[i]:divisions[i+1]], axis=0)
                     for i in range(len(divisions)-1)]

    if binResize:
        midpts_per_bin = np.histogram(xData, bins=bins)[0]
        scaling = np.array(
                [1/(bins[i+1] - bins[i])
                 for i, num in enumerate(midpts_per_bin) for j in range(num)])
        combined_data = np.array(combined_data) * scaling

    min_index = 0
    min_b_index = 0
    if min_x:
        min_index = next(i for i, val in enumerate(xData) if val >= min_x)
        min_b_index = next(i for i, val in enumerate(xBinning) if val >= min_x)

    max_index = len(xData)-1
    max_b_index = len(xBinning)-1
    if max_x:
        max_index = next(i for i, val in reversed(list(enumerate(xData)))
                         if val <= max_x)
        max_b_index = next(i for i, val in reversed(list(enumerate(xBinning)))
                           if val <= max_x)

    # Making plots
    y = [None] * len(combined_data)
    for i, data in enumerate(combined_data):
        y[i], _, __ = pad.hist(
            x=xData[min_index:max_index],
            bins=xBinning[min_b_index:max_b_index],
            weights=data[min_index:max_index], label=labels[i],
            histtype="step", rwidth=1.0, color=colors[i], edgecolor=colors[i],
            linewidth=4, bottom=None, cumulative=False, density=norm_one,
            align="mid", orientation="vertical")

    # Formatting plots
    plt.rc('text', usetex=False)
    plt.xlabel(xlabel, fontsize=16, color="black")
    plt.ylabel(ylabel, fontsize=16, color="black")
    ymax = np.array([elem.max() for elem in y]).max() * 1.1
    ymin = 0
    if logx:
        plt.gca().set_xscale("log", nonposy="clip")
    if logy:
        plt.gca().set_yscale("log", nonposy="clip")
        ymin = min([elem.min() for elem in y]) / 100
    plt.gca().set_ylim(ymin, ymax)
    plt.legend(bbox_to_anchor=(0.98, 0.98), loc='upper right',
               borderaxespad=0.)

    # Save figure
    if save:
        plt.savefig(out_file_name, dpi=300, bbox_inches='tight')


def curve_comparison_1d(x, y, labels=None, xlabel=None, ylabel=None,
                        markers=None, colors=None, file_name=None, logy=False,
                        save=False):
    """
    Takes a 1d array of x values and a 2d array of y values and produces a
    plot comparing the data sets contained in y such that similar rows have the
    same color

    x         - 1d array of x values
    y         - 2d array, or 2d array where each 'element' is a dataset
    labels    - 2d array of strings such that each element provides a name for
                the data set located in the same location in y
    xlabel    - string giving a label for the x axis
    ylabel    - string giving a label for the y axis
    colors    - list of strings representing valid matplotlib colors with same
                length as number of rows in y
    file_name - name of file the plot should be saved as
    logy      - boolean denoting whether y-axis should have log scale
    save      - boolean denoting whether plot should be saved
    """

    labels = labels or [
            ['Line {}'.format(i * len(y) + j) for j in range(len(y[i]))]
            for i in range(len(y))]
    xlabel = xlabel or 'x axis'
    ylabel = ylabel or 'y axis'
    colors = colors or ['#9b8e82', '#7a8e99', '#698252', '#a9935e', '#c7aec5']
    file_name = file_name or 'comparison_plot'

    # Set up figure
    fig = plt.figure(figsize=(12, 6), dpi=80)
    frame = gridspec.GridSpec(1, 1, right=0.7)
    fig.add_subplot(frame[0])

    # Plotting
    for data, color, label in zip(y, colors, labels):
        plt.plot(x, data, '-'+'x', label=label, color=color)

    # Formatting plots
    if logy:
        plt.yscale('log')
    plt.xlabel(r'{}'.format(xlabel))
    plt.ylabel(r'{}'.format(ylabel))
    plt.legend()
    plt.legend(bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)

    # Save figure
    if save:
        plt.savefig(file_name, dpi=300, bbox_inches='tight')


def curve_comparison_2d(x, y, labels=None, xlabel=None, ylabel=None,
                        markers=None, colors=None, file_name=None, logy=False,
                        save=False):
    """
    Takes a 1d array of x values and a 3d array of y values and produces a
    plot comparing the data sets contained in y such that similar rows have the
    same color and similar columns have the same marker

    x         - 1d array of x values
    y         - 3d array, or 2d array where each 'element' is a dataset
    labels    - 2d array of strings such that each element provides a name for
                the data set located in the same location in y
    xlabel    - string giving a label for the x axis
    ylabel    - string giving a label for the y axis
    markers   - list of strings representing matplotlib markers with same
                length as number of rows in y
    colors    - list of strings representing valid matplotlib colors with same
                length as number of columns in y
    file_name - name of file the plot should be saved as
    logy      - boolean denoting whether y-axis should have log scale
    save      - boolean denoting whether plot should be saved
    """

    labels = labels or [
            ['Line {}'.format(i * len(y) + j) for j in range(len(y[i]))]
            for i in range(len(y))]
    xlabel = xlabel or 'x axis'
    ylabel = ylabel or 'y axis'
    markers = markers or ['o', '^', 's', 'p']
    colors = colors or ['#9b8e82', '#7a8e99', ]
    file_name = file_name or 'comparison_plot'

    # Set up figure
    fig = plt.figure(figsize=(12, 6), dpi=80)
    frame = gridspec.GridSpec(1, 1, right=0.7)
    fig.add_subplot(frame[0])

    # Plotting
    for category, marker, label_set in zip(y, markers, labels):
        for data, color, label in zip(category, colors, label_set):
            plt.plot(x, data, '-'+marker, label=label, color=color)

    # Formatting plots
    if logy:
        plt.yscale('log')
    plt.xlabel(r'{}'.format(xlabel))
    plt.ylabel(r'{}'.format(ylabel))
    plt.legend()
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    # Save figure
    if save:
        plt.savefig(file_name, dpi=300, bbox_inches='tight')


def sig_and_bg_from_html(file_name):
    """
    Extracts the signal yield, signal yield uncertainty, background yield, and
    background yield uncertainty from an index.html file generated by
    MadAnalysis; the cut(s) of interest should be the last thing done in the
    analysis

    file_name - name of html file to extract from
    """

    tds = None
    with open(file_name, "r") as f:
        tds = html.fromstring(f.read()).xpath('//td')
    return [float(tds[index].text.strip().split()[elem]) for index in [-3, -2]
            for elem in [0, 2]]


def heatmap(y, cols, rows, label=None, xlabel=None, ylabel=None, smooth=False,
            contour=False, file_name=None, save=False):
    """
    Take a 2d list of values and produces a heatmap

    y         - 2d array of values
    cols      - numeric labels for x-axis
    rows      - numeric labels for y-axis
    label     - label for color scale on side of heatmap
    xlabel    - string giving a label for the x axis
    ylabel    - string giving a label for the y axis
    file_name - name of file the plot should be saved as
    save      - boolean denoting whether plot should be saved
    """

    label = label or 'Title'
    xlabel = xlabel or 'x axis'
    ylabel = ylabel or 'y axis'
    file_name = file_name or 'heatmap'

    if smooth:
        # Plotly, smooth, not all settings figured out
        fig = go.Figure(
            data=go.Heatmap(z=y, x=cols, y=rows, zsmooth='best',
                            colorbar={"title": {'text': label,
                                                'side': 'right'},
                                      'bgcolor': 'white'}))
        fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
        fig.write_image(file_name[:-4]+'smooth.png', scale=10)
    elif contour:
        # Plotly, contour, not all settings figured out
        fig = go.Figure(
            data=go.Contour(z=y, x=cols, y=rows,
                            colorbar={"title":
                                      {'text': label, 'side': 'right'}}))
        fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)
        fig.write_image(file_name[:-4]+'contour.png', scale=10)
    else:
        # Matplotlib, not smooth
        # Set up data frame
        frame = pd.DataFrame(y, index=rows, columns=cols)
        frame = frame.iloc[::-1]  # invert y-axis order

        # Set up figure
        ax = sb.heatmap(frame, cmap='YlGnBu',
                        cbar_kws={'label': r'{}'.format(label)})
        ax.set_xlabel(r'{}'.format(xlabel))
        ax.set_ylabel(r'{}'.format(ylabel))

        # Save figure
        if save:
            plt.tight_layout()
            plt.savefig(file_name, dpi=300, quality=95, bbox_inches='tight')
            plt.clf()


def sig_heatmap_html_extract(files):
    """
    Extracts signal and background values from a 2d array of .index html files

    files     - 2d array of .index html files returned by MadAnalysis analysis
                    that are to be used for heatmap of significance
    """

    signal = [[None for j in range(len(files[0]))] for i in range(len(files))]
    bg = [[None for j in range(len(files[0]))] for i in range(len(files))]

    for i, file_row in enumerate(files):
        for j, file in enumerate(file_row):
            signal[i][j], _, bg[i][j], __ = sig_and_bg_from_html(file)

    return [np.array(signal), np.array(bg)]

# CMSH = Coupling (vs) Mass Signal Heatmap


def assemble_sig_data_CMSH(M, L, f, filename, xres, yres, log_mode=False,
                           scaling=None):
    if log_mode:
        M_pts = np.logspace(
                np.log10(M[0]), np.log10(M[-1]), xres, endpoint=False)
        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
    else:
        M_pts = np.linspace(M[0], M[-1], xres, endpoint=False)
        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
    M_indices = np.searchsorted(M, M_pts, side='right') - 1
    L_indices = np.searchsorted(L, L_pts, side='right') - 1

    if scaling:
        # hard coded, yikes
        ratio = 0.25
        path = ('../optimization/second_sdEta_mjj_optimization/'
                + 'lumi_and_kin_plots/'
                + 'four_cuts_lum40/Output/HTML/MadAnalysis5job_0/index.html')
        bg = sig_and_bg_from_html(path)[2]
        signals = np.array([[
                f[i][j](y) for x, i in zip(M_pts, M_indices)]
                for y, j in zip(L_pts, L_indices)])
        scalings = np.array([[scaling(x, y) for x in M_pts] for y in L_pts])
        signals_scaled = signals * scalings
        sigs = signals_scaled / np.sqrt(signals_scaled + bg + (bg * ratio)**2)
        sigs = np.minimum(50, sigs)
    else:
        sigs = [[
                f[i][j](y) if f[i][j](y) < 50 else 50 for i in M_indices]
                for y, j in zip(L_pts, L_indices)]

    np.save(filename, sigs)

def assemble_banned_region_CMSH(M, L, filename, xres, yres, cond,
                                log_mode=False):
    if log_mode:
        M_pts = np.logspace(
                np.log10(M[0]), np.log10(M[-1]), xres, endpoint=False)
        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
    else:
        M_pts = np.linspace(M[0], M[-1], xres, endpoint=False)
        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
    banned = [
            [[0,0,0,0.5] if cond(m,l) else [1,1,1,0] for m in M_pts]
            for l in L_pts]
    np.save(filename, banned)


#def assemble_unitarity_banned_region_CMSH(M, L, filename, xres, yres, cond,
#                                          log_mode=False):
#    if log_mode:
#        M_pts = np.logspace(
#                np.log10(M[0]), np.log10(M[-1]), xres, endpoint=False)
#        L_pts = np.logspace(
#                np.log10(L[0]), np.log10(L[-1]), yres, endpoint=False)
#    else:
#        M_pts = np.linspace(M[0], M[-1], xres, endpoint=False)
#        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
#    banned = [
#            [[0,0,0,0.5] if cond(m,l) else [1,1,1,0] for m in M_pts]
#            for l in L_pts]
#    np.save(filename, banned)


#def assemble_lifetime_banned_region_CMSH(M, L, eta_filename, out_filename,
#                                         xres, yres, log_mode=False):
#    thetas = theta_monte_carlo(eta_filename)
#
#    if log_mode:
#        M_pts = np.logspace(M[0], M[-1], xres, endpoint=False)
#        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
#    else:
#        M_pts = np.linspace(M[0], M[-1], xres, endpoint=False)
#        L_pts = np.linspace(L[0], L[-1], yres, endpoint=False)
#    lengths = [[np.sort(
#            np.sin(thetas) * (3e8 / ax_to_aa_Gamma(m, l)) * 6.582119e-16)
#            for m in M_pts] for l in L_pts]
#    percents = [
#            [bs.bisect_left(length, 1.25) / len(length) for length in row]
#            for row in lengths]
#    banned = [
#            [[0,0,0,0.5] if percent < 0.95 else [1,1,1,0] for percent in row]
#            for row in percents]
#    np.save(out_filename, banned)

#    banned = []
#    for l in range(1000):
#        print(l)
#        temp = []
#        for m in range(1000):
#            x = (M[0] + ((M[-1] - M[0]) / xres) * m) * 10**9
#            y = (L[0] + ((L[-1] - L[0]) / yres) * l) * 10**12
#            lengths = np.sort(np.sin(thetas) * (3e8 / ax_to_aa_Gamma(x, y))
#                              * 6.582119e-16)
#            percent = bs.bisect_left(lengths, 1.25) / len(lengths)
#            temp.append([0,0,0,0.5] if percent < 0.95 else [1,1,1,0])
#        banned.append(temp)
#
#    np.save(out_filename, banned)


def coupling_mass_sig_heatmap(m, L, f, datafile, bannedfiles,
                              bannedconds, bannedlabels, xlabel, ylabel,
                              cmap='plasma',
                              force_assemble=False, xres=1000, yres=1000,
                              savefile='heatmap', log_mode=False,
                              scaling=None, save_contour=False):
    """
    Produces a heatmap similar to Fig. 12 in "Anapole Dark Matter via Vector
    Boson Fusion Processes at the LHC" and Figs. 14, 15 in "Probing heavy
    spin-2 bosons with γγ final states from vector boson fusion processes at
    the LHC" (modeled after the former)

    m           - strictly increasing list, boundaries of mass "columns" being
                  considered separately (i.e., have function(s) for each mass
                  "bin" established by list). first and last entries define
                  x-axis bounds of plot
    L           - strictly increasing list, boundaries of coupling "columns"
                  being considered separately (i.e., have function(s) for each
                  coupling "bin"  established by list). first and last entries
                  define y-axis bounds of plot
    f           - list of lists of functions with dimension
                  [len(m) - 1] x [len(L) - 1] (i.e., function for each m-bin,
                  L-bin pair). these are the functions for significance in
                  terms of coupling for a given mass (vertical slices of
                  significance)
    datafile    - name of file containing significance data to be created/used
    bannedfiles - list of strings containing file names for saved numpy arrays
                  contain "banned regions" to be visualized with imshow
                  (generated by )
    bannedconds - list of functions with same length as bannedfiles accepting
                  arguments m, l and returning a boolean: true if that (m,l)
                  pair is banned, false otherwise
    bannedlabels- names for banned regions in heatmap
    xlabel      - label for x axis
    ylabel      - label for y axis
    cmap        - string, valid matplotlib color map name to be used for the
                  heatmap
    force_assemble - boolean indicating if reproduction of datafile,
                  bannedfiles using assemble_sig_data_CMSH,
                  assemble_banned_region_CMSH should be performed
    xres        - int, number of pixels per row
    yres        - int, number of pixels per column
    savefile    - string, name of file to save plot to
    log_mode    - boolean indicating if pixels should be spaced logarithmically
                  (as compared to linear spacing then using log scale axes
                  through matplotlib) - RECOMMENDED
    scaling     - function with arguments m, l, returning a float
                  indicating how that pixel's signal should be scaled in
                  assemble_sig_data_CMSH (only has effect if force_assemble is
                  true)
    save_contour- boolean indicating if 5-sigma discovery contour data should
                  be saved as a numpy array (typically to apply contour to
                  plot of excluded regions on mass-coupling parameter space)
    """

    labels = ['Discovery Contour'] + bannedlabels

    # fetching/making significance data/banned region files
    if not os.path.isfile(datafile + '.npy') or force_assemble:
        assemble_sig_data_CMSH(m, L, f, datafile, xres, yres, log_mode,
                               scaling)
    for cond, bannedfile in zip(bannedconds, bannedfiles):
        if not os.path.isfile(bannedfile + '.npy') or force_assemble:
            assemble_banned_region_CMSH(m, L, bannedfile, xres, yres, cond,
                                        log_mode)

    sigs = np.load(datafile + '.npy')
    banneds = [np.load(bannedfile + '.npy') for bannedfile in bannedfiles]

    if log_mode:
        extent = (np.log10(m[0]), np.log10(m[-1]), L[0], L[-1])
    else:
        extent = (m[0], m[-1], L[0], L[-1])

    # heatmap
    plt.imshow(sigs, cmap='plasma', origin='lower', extent=extent,
               aspect='auto')
    cbar = plt.colorbar()

    m, L = [np.array(m), np.array(L)]

    # 5 sigma curve
    xs = np.linspace(0, xres-1, 100, dtype=int)
    ys = []
    for x in xs:
        for y in range(0, yres, int(yres/100)):
            if sigs[y][x] < 5:
                ys.append(y)
                break

    ys = np.array(ys)
    ms = np.log10(m[0]) + xs * (np.log10(m[-1]) - np.log10(m[0])) / xres
    Ls = L[0] + ys * (L[-1] - L[0]) / yres
    curve = plt.plot(ms, Ls, linewidth=3, linestyle='dashed', color='gray')
    if save_contour:
        contour_data = np.array([ms, Ls])
        np.save('contour_data', contour_data)

    # banned regions
    zones = []
    for banned in banneds:
        plt.imshow(banned, origin='lower', extent=extent, aspect='auto')
        zones.append(mpatches.Patch(color=[0,0,0,0.5]))

    # figure settings
    if not log_mode:
        plt.xscale('log')
    plt.legend(handles=[curve[0]] + zones, labels=labels,
               bbox_to_anchor=(0.02, 0.98), loc=2, borderaxespad=0.)
    plt.ylabel(r'{}'.format(ylabel))
    plt.xlabel(r'{}'.format(xlabel))
    cbar.set_label('Signal Significance', rotation=90)
    cbar.ax.get_yaxis().labelpad = 8
    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    plt.savefig(savefile, dpi=300, bbox_inches='tight')


def get_histo(file_name):
    file_name = file_name

    # Variable setup
    xData = None
    take_bins = True
    data = []

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
                xData = np.array(
                        list(map(float, line[start+1:end].split(','))))
                take_bins = False
            else:
                data.append(
                        np.array(list(map(float,
                                          line[start+1:end].split(',')))))
    file.close()

    histo, bins = np.histogram(a=xData, bins=xBinning, weights=data[0])

    return [xData, bins, histo]

def theta_monte_carlo(file_name, size):
    midpoints, bins, eta_histo = get_histo(file_name)

    eta_cdf = np.cumsum(eta_histo)
    eta_cdf = eta_cdf / eta_cdf[-1]
    values = np.random.rand(size)
    value_probs = np.searchsorted(eta_cdf, values)
    etas = midpoints[value_probs]

    return 2 * np.arctan(np.exp(-etas))

#    USED FOR ANAPOLE PLOT, LINEAR MODE
#    x = ((m - m[0]) * (len(sigs[0])/(m[-1] - m[0]))).astype(int)
#    y = []
#    for i in x:
#        i = i if i < 1000 else 999
#        for j in range(yres):
#            if sigs[j][i] < 5:
#                y.append(L[0] + ((L[-1] - L[0]) / yres) * j)
#                break
#    curve = plt.plot(m, y, linewidth=3, linestyle='dashed', color='gray')

