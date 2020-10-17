#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:28:47 2020

@author: elijahsheridan
"""

import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import bisect as bs
import matplotlib.gridspec as gridspec
from lxml import html
import matplotlib.patches as mpatches
from PIL import Image

"""

**************************
**************************
***  HELPER FUNCTIONS  ***
**************************
**************************

"""

def smooth_heatmap_from_irreg_grid(xs, ys, data, xlabel, ylabel, clabel,
                                   res=1000, ext=None, save_file=None,
                                   minsig=None,maxsig=None):
    ext = ext or [xs[0], xs[-1], ys[0], ys[-1]]
    # look into order of "for" statements?
    pts = np.array([[x,y] for x in xs for y in ys])
    data = np.array(data).flatten()
    grid = np.array(
            [[[x,y] for x in np.linspace(ext[0], ext[1], res)]
            for y in np.linspace(ext[2], ext[3], res)])
    interp = scipy.interpolate.griddata(pts, data, grid)

    if minsig and maxsig:
        plt.imshow(interp, origin='lower', aspect='auto', extent=ext,
                   vmin=minsig, vmax=maxsig)
    else:
        plt.imshow(interp, origin='lower', aspect='auto', extent=ext)
    cbar = plt.colorbar()
    plt.xlabel(r'{}'.format(xlabel))
    plt.ylabel(r'{}'.format(ylabel))
    cbar.set_label(r'{}'.format(clabel), rotation=90)
    if save_file:
        plt.savefig(save_file, dpi=300, bbox_inches='tight')


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


def Gamma(m_a=1e6, Lambda=1e12):
    alpha = 1/137
    return (4 * np.pi * alpha**2 * m_a**3) / Lambda**2


def kin_histo_sig_bg(file_name, sig_divs, bg_divs, out_file_name=None, norm_one=True,
              labels=None, ylabel=None, colors=None, logx=False, logy=False,
              save=False, bins=None, binResize=False, xlabel=None, min_x=None,
              max_x=None, stacked=False, histtypes=None, linestyles=None,
              stack_bg=True):
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
    stacked
    shaded
    dashed
    """

    file_name = file_name
    out_file_name = out_file_name or 'plot'
    labels = labels or ['Plot ' + str(i) for i in range(len(sig_divs + bg_divs))]
    if stack_bg:
        colors = colors or ['#698252', '#e8aa7a', '#4bd3bd', '#ec4738', '#7a8e99', '#9b8e82', '#a9935e']
    else:
        colors = colors or ['#698252', '#4bd3bd', '#9b8e82', '#7a8e99', '#a9935e']
    histtypes = histtypes or ['step'] * len(sig_divs + bg_divs)
    linestyles = linestyles or ['solid'] * len(sig_divs + bg_divs)

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
    fig = plt.figure()
    frame = gridspec.GridSpec(1, 1, right=0.7)
    pad = fig.add_subplot(frame[0])

    # Combining data
    bg_divs.append(len(data))
    sig_divs.append(bg_divs[0])
    comb_sig_data = [np.sum(data[sig_divs[i]:sig_divs[i+1]], axis=0)
                     for i in range(len(sig_divs)-1)]
    comb_bg_data = [np.sum(data[bg_divs[i]:bg_divs[i+1]], axis=0)
                     for i in range(len(bg_divs)-1)]
    if stack_bg:
        for i in range(1,len(comb_bg_data)):
            comb_bg_data[i] += comb_bg_data[i-1]

    y_bg = [None] * len(comb_bg_data)
    y_sig = [None] * len(comb_sig_data)
    if stack_bg:
        for i, data in reversed(list(enumerate(comb_bg_data))): # reversed
            y_bg[i], _, __ = pad.hist(
                x=xData,
                bins=xBinning,
                weights=data, label=labels[i+len(y_sig)],
                histtype='stepfilled', rwidth=1.0, color=colors[i+len(y_sig)], edgecolor=colors[i+len(y_sig)],
                linewidth=4, bottom=None, cumulative=False, density=norm_one,
                align="mid", orientation="vertical", linestyle='solid')
    else:
        for i, data in enumerate(comb_bg_data):
            y_bg[i], _, __ = pad.hist(
                x=xData,
                bins=xBinning,
                weights=data, label=labels[i+len(y_sig)],
                rwidth=1.0, color=colors[i+len(y_sig)], edgecolor=colors[i+len(y_sig)],
                linewidth=4, bottom=None, cumulative=False, density=norm_one,
                align="mid", orientation="vertical", linestyle='solid',
                histtype='step')
            # histtype='stepfilled',

    # Making plots
    for i, data in enumerate(comb_sig_data):
        y_sig[i], _, __ = pad.hist(
            x=xData,
            bins=xBinning,
            weights=data, label=labels[i],
            histtype='step', rwidth=1.0, color=colors[i], edgecolor=colors[i],
            linewidth=6, bottom=None, cumulative=False, density=norm_one,
            align="mid", orientation="vertical", linestyle='dotted')



    # Formatting plots
    plt.rc('text', usetex=False)
    plt.xlabel(xlabel, color="black")
    plt.ylabel(ylabel, color="black")
    if logx:
        plt.gca().set_xscale("log", nonposy="clip")
    if logy:
        plt.gca().set_yscale("log", nonposy="clip")
#        ymin = min([elem.min() for elem in y_bg + y_sig]) / 100
#    plt.gca().set_ylim(ymin, ymax)


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


def cond(percent): return percent < 0.95

def ax_scaling(m, l):
    eta_filename = (
        '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
        + 'post_optimization_studies/mad_analyses/1MeV_axion_rapidity/Output/'
        + 'Histos/MadAnalysis5job_0/selection_0.py')
    thetas = theta_monte_carlo(eta_filename, 500)

    lengths = np.sort(
            np.sin(thetas) * (3e8 / Gamma(m, l)) * 6.582119e-16)
    percent = np.searchsorted(lengths, 1.25, side='right') / len(lengths)
    return percent


def read_and_save_image(image, save_file):
    im = Image.open(image, 'r')
    width, height = im.size
    print(width, height)
    pix_list_1d = list(im.getdata())
    pix_array = np.array(
            [[pix_list_1d[x + width * y] for x in range(width)]
            for y in range(height)])

#    pix_array = []
#    for y in range(height):
#        temp = []
#        for x in range(width):
#            temp.append(pixel_values[x + width * y])
#        pix_array.append(temp)
#    pix_array = np.array(pix_array)

    np.save(save_file, pix_array)

#read_and_save_image('big_image.png', 'big_image.npy')
#read_and_save_image('small_image.png', 'small_image.npy')

def index_to_val(index, min_val, max_val, num_indices, y=False):
    if y:
        return min_val + ((max_val - min_val)/num_indices) * (
                num_indices - index - 1)
    else:
        return min_val + ((max_val - min_val)/num_indices) * index


def val_to_index(val, min_val, max_val, num_indices, y=False):
    index = int((val - min_val) * num_indices/(max_val - min_val))
    if y:
        return (num_indices - 1) - index
    else:
        return index


"""

*************************
*************************
******   FIGURES   ******
*************************
*************************

"""

# INSTANT
def FIG2_axion_cross_sec():
    ms = np.log10([1, 1e3, 1e5])
    Ls = np.array([i/2 for i in range(2,9)])
    # in picobarns
    cross_secs = np.array(
            [[10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555],
             [10.09, 2.291, 1.068, 0.6473, 0.4395, 0.32, 0.2446],
             [8.523, 1.777, 0.8011, 0.4779, 0.3227, 0.2344, 0.1788]])

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (12,8)}

    with plt.rc_context(settings):
        smooth_heatmap_from_irreg_grid(ms, Ls, cross_secs,
                                       '$m_a$ [$\log_{10}$ MeV]',
                                       '$\Lambda$ [TeV]',
                                       'Cross Section $\sigma$ [pb]',
                                       save_file='FIG2_axion_cross_sec')
        plt.clf()


# no gen - SECONDS; gen - 2 MINUTES
def FIG3_axion_decay_length(gen=False):
    num_thetas = 10000
    data_pts_per_row = 500

    select_file_name = (
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + '1MeV_axion_rapidity_with_selections/Output/'
            + 'Histos/MadAnalysis5job_0/selection_0.py')

    m_as = np.linspace(2, 17, data_pts_per_row) * 10**6
    Lambdas = np.linspace(1, 4, data_pts_per_row) * 10**12
    xticks = np.linspace(2, 17, data_pts_per_row)
    yticks = np.linspace(1, 4, data_pts_per_row)

    if gen:
        thetas = theta_monte_carlo(select_file_name, num_thetas)

        percentages = []
        for m in m_as:
            temp = []
            for L in Lambdas:
                data = np.sin(thetas) * (3e8 / Gamma(m, L)) * 6.582119e-16
                index = bs.bisect_left(np.sort(data), 1.25)
                temp.append(index/len(data))
            percentages.append(temp)

        np.save('FIG3_percentages', percentages)
    else:
        percentages = np.load('FIG3_percentages.npy')

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (12,8)}

    with plt.rc_context(settings):
        smooth_heatmap_from_irreg_grid(xticks, yticks, percentages,
                                       '$m_a$ [MeV]',
                                       '$\Lambda$ [TeV]',
                                       'Reconstruction Efficiency',
                                       save_file='FIG3_axion_decay_length')
        plt.clf()

def FIG4_log_deta_pre_no_gg():
    file_name = ('/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/pre_select_two_signal'
            + '/Output/Histos/MadAnalysis5job_0/selection_8.py')
    plot_name = 'FIG4_log_deta_pre_no_gg'
    ylabel = r'a.u.'
    xlabel = r'$\Delta \eta^{jj}$'
    labels = [r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^2\alpha_{QCD}^2$',
              r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^4\alpha_{QCD}^0$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 1$ MeV)',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 100$ MeV)']
    sig_divs = [0, 1]
    bg_divs = [2, 10]

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (15,8),
                'legend.framealpha': 0.3}

    with plt.rc_context(settings):
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                         out_file_name=plot_name, labels=labels,
                         ylabel=ylabel, save=True, norm_one=True,
                         xlabel=xlabel, stacked=True, logy=True,
                         stack_bg=False)
        handles = [plt.Line2D([0], [0], color='#7a8e99', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#9b8e82', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#698252', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#4bd3bd', linestyle='dotted', lw=6, label='Line')]
        plt.legend(handles, labels, bbox_to_anchor=(0.01, 0.02), loc='lower left',
                   borderaxespad=0.)
        plt.gca().set_ylim(10**-4.2, 10**0.1)
#        plt.gca().set_ylim(10**-8, 10**-1.3)
        plt.gca().set_xlim(2.4, 8)
        plt.savefig(plot_name, dpi=300, bbox_inches='tight')
        plt.clf()


def FIG5_log_mjj_pre_2sig():
    file_name = ('/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/pre_select_two_signal'
            + '/Output/Histos/MadAnalysis5job_0/selection_7.py')
    plot_name = 'FIG5_log_mjj_pre_2sig'
    ylabel = r'a.u.'
    xlabel = r'$m^{jj}$ [GeV]'
    labels = [r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^2\alpha_{QCD}^2$',
              r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^4\alpha_{QCD}^0$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 1$ MeV)',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 100$ MeV)']
    sig_divs = [0, 1]
    bg_divs = [2, 10]

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (15,8),
                'legend.framealpha': 0.3}

    with plt.rc_context(settings):
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                         out_file_name=plot_name, labels=labels,
                         ylabel=ylabel, save=True, norm_one=True,
                         xlabel=xlabel, stacked=True, logy=True,
                         stack_bg=False)
        handles = [plt.Line2D([0], [0], color='#7a8e99', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#9b8e82', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#698252', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#4bd3bd', linestyle='dotted', lw=6, label='Line')]
        plt.legend(handles, labels, bbox_to_anchor=(0.01, 0.02), loc='lower left',
                   borderaxespad=0.)
        plt.gca().set_ylim(10**-8, 10**-1.3)
        plt.gca().set_xlim(120, 2000)
        plt.savefig(plot_name, dpi=300, bbox_inches='tight')
        plt.clf()


def FIG6_log_maa_pre_2sig():
    file_name = ('/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/pre_select_two_signal'
            + '/Output/Histos/MadAnalysis5job_0/selection_9.py')
    plot_name = 'FIG6_log_maa_pre_2sig'
    ylabel = r'a.u.'
    xlabel = r'$m^{\gamma\gamma}$ [GeV]'
    labels = [r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^2\alpha_{QCD}^2$',
              r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^4\alpha_{QCD}^0$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 1$ MeV)',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 100$ MeV)']
    sig_divs = [0, 1]
    bg_divs = [2, 10]

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (15,8),
                'legend.framealpha': 0.3}

    with plt.rc_context(settings):
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                         out_file_name=plot_name, labels=labels,
                         ylabel=ylabel, save=True, norm_one=True,
                         xlabel=xlabel, stacked=True, logy=True,
                         stack_bg=False)
        handles = [plt.Line2D([0], [0], color='#7a8e99', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#9b8e82', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#698252', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#4bd3bd', linestyle='dotted', lw=6, label='Line')]
        plt.legend(handles, labels, bbox_to_anchor=(0.01, 0.02), loc='lower left',
                   borderaxespad=0.)
        plt.gca().set_ylim(10**-8, 10**-1.3)
        plt.gca().set_xlim(0, 1000)
        plt.savefig(plot_name, dpi=300, bbox_inches='tight')
        plt.clf()


def FIG7_log_pta1_pre_2sig():
    file_name = ('/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/pre_select_two_signal'
            + '/Output/Histos/MadAnalysis5job_0/selection_10.py')
    plot_name = 'FIG7_log_pta1_pre_2sig'
    ylabel = r'a.u.'
    xlabel = r'$p_T^{\gamma_1}$ [GeV]'
    labels = [r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^2\alpha_{QCD}^2$',
              r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^4\alpha_{QCD}^0$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 1$ MeV)',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (m_a = 100$ MeV)']

    sig_divs = [0, 1]
    bg_divs = [2, 10]

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (15,8),
                'legend.framealpha': 0.3}

    with plt.rc_context(settings):
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                         out_file_name=plot_name, labels=labels,
                         ylabel=ylabel, save=True, norm_one=True,
                         xlabel=xlabel, stacked=True, logy=True,
                         stack_bg=False)
        handles = [plt.Line2D([0], [0], color='#7a8e99', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#9b8e82', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#698252', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#4bd3bd', linestyle='dotted', lw=6, label='Line')]
        plt.legend(handles, labels, bbox_to_anchor=(0.01, 0.02), loc='lower left',
                   borderaxespad=0.)
        plt.gca().set_ylim(10**-8, 10**-1.3)
        plt.gca().set_xlim(0, 1000)
        plt.savefig(plot_name, dpi=300, bbox_inches='tight')
        plt.clf()


def FIG8_axion_significance_vs_selection_photons():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/pta_maa_optimization/tight_analyses'
    specific_folder_start = '/analysis_tight_pta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    pta_cuts = [100 + 50 * i for i in range(9)]
    maa_cuts = [200 + 50 * i for i in range(11)]
    r = 0.25

    minsig, maxsig = [6.068202884263891, 24.23872089868384]

#    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[outer_path + specific_folder_start + str(pta_cut) + '_maa'
              + str(maa_cut) + inner_path
              for maa_cut in maa_cuts] for pta_cut in pta_cuts]

    signal, bg = sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    clabel = r'Signal Significance'

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (12, 9.6)}

    with plt.rc_context(settings):
        smooth_heatmap_from_irreg_grid(maa_cuts, pta_cuts,
                                       np.transpose(sig),
                                       '$m^{\gamma\gamma}$ [GeV]',
                                       '$p_T^\gamma$ [GeV]',
                                       clabel,
                                       save_file='FIG8_axion_significance_vs_selection_photons',
                                       minsig=minsig,
                                       maxsig=maxsig)
    plt.clf()


def FIG9_axion_significance_vs_selection_jets_3pt6():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/second_sdEta_mjj_optimization'
    specific_folder_start = '/second_analysis_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    r = 0.25

    minsig, maxsig = [6.068202884263891, 24.23872089868384]

    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[folder + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    clabel = r'Signal Significance'

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (12, 9.6)}

    with plt.rc_context(settings):
        smooth_heatmap_from_irreg_grid(mmjj_cuts, delta_eta_cuts, np.transpose(sig),
                                       '$m^{jj}$ [GeV]',
                                       '$\Delta \eta^{jj}$',
                                       clabel,
                                       save_file='FIG9_axion_significance_vs_selection_jets_3pt6',
                                       minsig=minsig,
                                       maxsig=maxsig)
    plt.clf()


def FIG10_post_log_mjj():
    file_name = ('/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_binsize'
            + '/Output/Histos/MadAnalysis5job_0/selection_7.py')
    plot_name = 'FIG10_post_log_mjj'
    ylabel = r'Events ($\mathcal{L}_{int} = 3000$ fb$^{-1}$)'
    xlabel = r'$m^{jj}$ [GeV]'
    labels = [r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^2\alpha_{QCD}^2$',
              r'$pp \; \to \; jj + \gamma\gamma, \; \alpha_{QED}^4\alpha_{QCD}^0$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (\Lambda = 1.8$ TeV$)$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (\Lambda = 2.0$ TeV$)$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (\Lambda = 2.2$ TeV$)$',
              r'$pp \; \to \; jj + a \; (\to \; \gamma\gamma), \; \alpha_{QED}^4\alpha_{QCD}^0 \; (\Lambda = 2.4$ TeV$)$']
    sig_divs = [0,1,2,3]
    bg_divs = [4, 12]

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 18,
                'figure.figsize': (15,8),
                'legend.framealpha': 0.3}

    with plt.rc_context(settings):
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                         out_file_name=plot_name, labels=labels,
                         ylabel=ylabel, save=True, norm_one=False,
                         xlabel=xlabel, stacked=True, logy=True, stack_bg=True)
        handles = [plt.Line2D([0], [0], color='#7a8e99', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#9b8e82', lw=4, label='Line'),
                   plt.Line2D([0], [0], color='#698252', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#e8aa7a', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#4bd3bd', linestyle='dotted', lw=6, label='Line'),
                   plt.Line2D([0], [0], color='#ec4738', linestyle='dotted', lw=6, label='Line')]
        plt.legend(handles, labels, bbox_to_anchor=(0.01, 0.02), loc='lower left',
                   borderaxespad=0.)
        plt.gca().set_ylim(10**-2, 10**3.2)
        plt.gca().set_xlim(750, 6000)
        plt.savefig(plot_name, dpi=300, bbox_inches='tight')
        plt.clf()


# SECONDS
def FIG11_sig_ma_L_lum150(gen=False):
    # prelim vars
    ratio = 0.25
    res = 1000


    path = ('../optimization/second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum{}/Output/HTML/MadAnalysis5job_0/index.html'.format(str(150)))

    # masses, couplings considered
    Ls = [1, 1.5, 2, 2.5, 3, 3.5, 4] # TeV
    ms = [-3, 0, 2] # Log10(GeV)
    ext = [ms[0], ms[-1], Ls[0], Ls[-1]]
    mL_pairs_flat = np.array([[m,L] for L in Ls for m in ms])

    # cross sections, used to scale signal yield
    cross_secs = [[10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555],
                  [10.09, 2.291, 1.068, 0.6473, 0.4395, 0.32, 0.2446],
                  [8.523, 1.777, 0.8011, 0.4779, 0.3227, 0.2344, 0.1788]]
    scalings = np.transpose(
            [[cs/cross_secs[0][0] for cs in cross_sec] for cross_sec in cross_secs])

    # importing a single signal, background data point
    signal, _, bg, __ = sig_and_bg_from_html(path)

    # scaling signal, finding significance
    signals = signal * scalings
    sigs = signals / np.sqrt(signals + bg + (bg * ratio)**2)
    flat_sigs = sigs.flatten()

    # interpolation
    grid = np.array(
            [[[x,y] for x in np.linspace(ext[0], ext[1], res)]
            for y in np.linspace(ext[2], ext[3], res)])
    interp = scipy.interpolate.griddata(mL_pairs_flat, flat_sigs, grid)

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 24,
                'figure.figsize': (15, 10)}

    with plt.rc_context(settings):
        # heatmap
        plt.imshow(interp, cmap='plasma', origin='lower', extent=ext,
                   aspect='auto', vmin=0, vmax=55.42527413498376)
        cbar = plt.colorbar()

    # 5 sigma curve
    xs = np.linspace(0, res-1, 100, dtype=int)
    ys = []
    for x in xs:
        for y in range(0, res, int(res/100)):
            if interp[y][x] < 5:
                ys.append(y)
                break
    ys = np.array(ys)
    cms = ms[0] + xs * (ms[-1] - ms[0]) / res
    cLs = Ls[0] + ys * (Ls[-1] - Ls[0]) / res
    curve = plt.plot(cms, cLs, linewidth=6 , linestyle='dashed', color='gray')

    # lifetime ban
    if gen:
        percent = [
                [ax_scaling(10**item[0] * 1e9, item[1] * 1e12) for item in row]
                for row in grid]
        np.save('new_heatmap_lifetime_percents', percent)
    else:
        percent = np.load('FIG11_lifetime_percents.npy')

    banned = [[[0,0,0,0.5] if cond(item) else [1,1,1,0] for item in row]
              for row in percent]

    with plt.rc_context(settings):
        plt.imshow(banned, origin='lower', extent=ext, aspect='auto')
        zone = mpatches.Patch(color=[0,0,0,0.5])


        labels = ['Discovery Contour', 'Axions Escape CMS Detector']
        xlabel = '$m_a$ [log$_{10}$(GeV)]'
        ylabel = '$\Lambda$ [TeV]'
        plt.legend(handles=[curve[0], zone], labels=labels,
                       bbox_to_anchor=(0.98, 0.98), loc=1, borderaxespad=0.)
        plt.ylabel(r'{}'.format(ylabel))
        plt.xlabel(r'{}'.format(xlabel))
        cbar.set_label('Signal Significance', rotation=90)
        cbar.ax.get_yaxis().labelpad = 8

        plt.savefig('FIG11_sig_ma_L_lum150',
                    dpi=300, bbox_inches='tight')

        plt.clf()


# SECONDS
def FIG12_sig_ma_L_lum3000(gen=False):
    # prelim vars
    ratio = 0.25
    res = 1000


    path = ('../optimization/second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum{}/Output/HTML/MadAnalysis5job_0/index.html'.format(str(3000)))

    # masses, couplings considered
    Ls = [1, 1.5, 2, 2.5, 3, 3.5, 4] # TeV
    ms = [-3, 0, 2] # Log10(GeV)
    ext = [ms[0], ms[-1], Ls[0], Ls[-1]]
    mL_pairs_flat = np.array([[m,L] for L in Ls for m in ms])

    # cross sections, used to scale signal yield
    cross_secs = [[10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555],
                  [10.09, 2.291, 1.068, 0.6473, 0.4395, 0.32, 0.2446],
                  [8.523, 1.777, 0.8011, 0.4779, 0.3227, 0.2344, 0.1788]]
    scalings = np.transpose(
            [[cs/cross_secs[0][0] for cs in cross_sec] for cross_sec in cross_secs])

    # importing a single signal, background data point
    signal, _, bg, __ = sig_and_bg_from_html(path)

    # scaling signal, finding significance
    signals = signal * scalings
    sigs = signals / np.sqrt(signals + bg + (bg * ratio)**2)
    flat_sigs = sigs.flatten()

    # interpolation
    grid = np.array(
            [[[x,y] for x in np.linspace(ext[0], ext[1], res)]
            for y in np.linspace(ext[2], ext[3], res)])
    interp = scipy.interpolate.griddata(mL_pairs_flat, flat_sigs, grid)

    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 24,
                'figure.figsize': (15, 10)}

    with plt.rc_context(settings):
        # heatmap
        plt.imshow(interp, cmap='plasma', origin='lower', extent=ext,
                   aspect='auto', vmin=0, vmax=55.42527413498376)
        cbar = plt.colorbar()

    # 5 sigma curve
    xs = np.linspace(0, res-1, 100, dtype=int)
    ys = []
    for x in xs:
        for y in range(0, res, int(res/100)):
            if interp[y][x] < 5:
                ys.append(y)
                break
    ys = np.array(ys)
    cms = ms[0] + xs * (ms[-1] - ms[0]) / res
    cLs = Ls[0] + ys * (Ls[-1] - Ls[0]) / res
    curve = plt.plot(cms, cLs, linewidth=6, linestyle='dashed', color='gray')

    # lifetime ban
    if gen:
        percent = [
                [ax_scaling(10**item[0] * 1e9, item[1] * 1e12) for item in row]
                for row in grid]
        np.save('new_heatmap_lifetime_percents', percent)
    else:
        percent = np.load('FIG11_lifetime_percents.npy')

    banned = [[[0,0,0,0.5] if cond(item) else [1,1,1,0] for item in row]
              for row in percent]

    with plt.rc_context(settings):
        plt.imshow(banned, origin='lower', extent=ext, aspect='auto')
        zone = mpatches.Patch(color=[0,0,0,0.5])


        labels = ['Discovery Contour', 'Axions Escape CMS Detector']
        xlabel = '$m_a$ [log$_{10}$(GeV)]'
        ylabel = '$\Lambda$ [TeV]'
        plt.legend(handles=[curve[0], zone], labels=labels,
                       bbox_to_anchor=(0.98, 0.98), loc=1, borderaxespad=0.)
        plt.ylabel(r'{}'.format(ylabel))
        plt.xlabel(r'{}'.format(xlabel))
        cbar.set_label('Signal Significance', rotation=90)
        cbar.ax.get_yaxis().labelpad = 8

        plt.savefig('FIG12_sig_ma_L_lum3000',
                    dpi=300, bbox_inches='tight')

        plt.clf()


def FIG13_subset_parameter_space_hashed(gen=False):
    settings = {'axes.labelsize': 32,
                'xtick.major.size': 10,
                'xtick.major.width': 1.5,
                'xtick.labelsize': 24,
                'ytick.major.size': 10,
                'ytick.major.width': 1.5,
                'ytick.labelsize': 24,
                'legend.fontsize': 24,
                'figure.figsize': (15, 10)}

    m, L = [row for row in np.load('FIG13_contour_data.npy')]
    m, L = [m, -np.log10(L)]
    i, f = np.searchsorted(m, [-2, 3])
    m, L = [np.append(m[i:f],[3.4]), np.append(L[i:f], [L[-1]])]

    pix_vals = np.load('FIG13_small_image.npy')
    w, h = list((7/pix_vals.shape[0]) * np.array(pix_vals.shape[:2]))
    bounds = [0.00032480888972387324, 10048.799127736118, 0.00867122579786319,
              2732.3259558424825]
    extent = [np.log10(b) for b in bounds]

    with plt.rc_context(settings):
        plt.imshow(pix_vals, extent=extent, aspect='auto')

    if gen:

        # min and max x-axis indices (mass indices) for our region
        imindex, fmindex = [val_to_index(m[0], extent[0], extent[1], len(pix_vals[0])),
                            val_to_index(m[-1], extent[0], extent[1], len(pix_vals[0]))]
        # set of all columns between min and max
        cols = np.linspace(imindex, fmindex, fmindex - imindex + 1)
        # indices in "m" associated with each column
        m_indices = np.searchsorted(
                m, [index_to_val(col, extent[0], extent[1], len(pix_vals[0]))
                for col in cols])
        # lowest row to shade for each relevant column
        bots = [val_to_index(L[m_index], extent[2], extent[3], len(pix_vals), True)
                for m_index in m_indices]
        # white, except for col indices in cols and above the line
        # [178/255, 34/255, 34/255, 1]
        #
    #    new_region = [
    #            [[178/255, 34/255, 34/255, 1]
    #            if j in cols and (i < bots[np.where(cols==j)[0][0]])
    #            and np.sum(pix_vals[i,j,:3]**2) > 3*240**2
    #            else [1.,1.,1.,0.]
    #            for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]
        new_region = [
                [[0,0,0,0.25]
                if j in cols and (i < bots[np.where(cols==j)[0][0]])
                else [1.,1.,1.,0.]
                for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]

        np.save('FIG13_shade_region', new_region)
    else:
        new_region = np.load('FIG13_shade_region.npy')



    with plt.rc_context(settings):
        plt.imshow(new_region, extent=extent, aspect='auto')

        #plt.plot(m, L, linewidth=3, color='firebrick')
        fig = plt.gcf()
        fig.set_size_inches(w*(12/7), h*(12/7))
        plt.xlabel(r'$m_a$ [Log$_{10}$ GeV]')
        plt.ylabel(r'$1/\Lambda$ [Log$_{10}$ TeV$^{-1}$]')
        plt.savefig('FIG13_subset_parameter_space_hashed', dpi=500, bbox_inches='tight')


#FIG2_axion_cross_sec()
#FIG3_axion_decay_length()
#FIG4_log_deta_pre_no_gg()
#FIG5_log_mjj_pre_2sig()
#FIG6_log_maa_pre_2sig()
#FIG7_log_pta1_pre_2sig()
#FIG8_axion_significance_vs_selection_photons()
#FIG9_axion_significance_vs_selection_jets_3pt6()
#FIG10_post_log_mjj()
FIG11_sig_ma_L_lum150()
FIG12_sig_ma_L_lum3000()
#FIG13_subset_parameter_space_hashed(False)
