#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:24:59 2020

@author: elijahsheridan
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import opt_helper as opt

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
#    colors = colors or ['#698252', '#e8aa7a', '#4bd3bd', '#ec4738', '#7a8e99', '#9b8e82', '#a9935e']
    colors = colors or ['#698252', '#9b8e82', '#7a8e99', '#a9935e']
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
    fig = plt.figure(figsize=(12, 6), dpi=80)
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
#    for i, data in reversed(list(enumerate(comb_bg_data))): # reversed
    for i, data in enumerate(comb_bg_data):
        y_bg[i], _, __ = pad.hist(
            x=xData,
            bins=xBinning,
            weights=data, label=labels[i+len(y_sig)],
            histtype='stepfilled', rwidth=1.0, color=colors[i+len(y_sig)], edgecolor=colors[i+len(y_sig)],
            linewidth=4, bottom=None, cumulative=False, density=norm_one,
            align="mid", orientation="vertical", linestyle='solid')

    # Making plots
    for i, data in enumerate(comb_sig_data):
        y_sig[i], _, __ = pad.hist(
            x=xData,
            bins=xBinning,
            weights=data, label=labels[i],
            histtype='step', rwidth=1.0, color=colors[i], edgecolor=colors[i],
            linewidth=2, bottom=None, cumulative=False, density=norm_one,
            align="mid", orientation="vertical", linestyle='dotted')


    # Formatting plots
    plt.rc('text', usetex=False)
    plt.xlabel(xlabel, fontsize=16, color="black")
    plt.ylabel(ylabel, fontsize=16, color="black")
    ymax = np.array([elem.max() for elem in y_bg + y_sig]).max() * 1.1
    ymin = 0
    if logx:
        plt.gca().set_xscale("log", nonposy="clip")
    if logy:
        plt.gca().set_yscale("log", nonposy="clip")
        ymin = min([elem.min() for elem in y_bg + y_sig]) / 100
    plt.gca().set_ylim(ymin, ymax)
    plt.legend(bbox_to_anchor=(0.98, 0.98), loc='upper right',
               borderaxespad=0.)

    # Save figure
    if save:
        plt.savefig(out_file_name, dpi=300, bbox_inches='tight')


def on_discovery_contour_delta_eta_2():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta2'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta2', 'etaj1_deta2', 'phij1_deta2', 'ptj2_deta2',
             'etaj2_deta2', 'phij2_deta2', 'dRjj_deta2', 'mjj_deta2',
             'detajj_deta2', 'maa_deta2', 'pta1_deta2', 'pta2_deta2',
             'THT_deta2', 'MET_deta2', 'TET_deta2']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_2/'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=False)


def on_discovery_contour_delta_eta_2_log():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta2'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta2', 'etaj1_deta2', 'phij1_deta2', 'ptj2_deta2',
             'etaj2_deta2', 'phij2_deta2', 'dRjj_deta2', 'mjj_deta2',
             'detajj_deta2', 'maa_deta2', 'pta1_deta2', 'pta2_deta2',
             'THT_deta2', 'MET_deta2', 'TET_deta2']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_2/log_'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=True)


def on_discovery_contour_delta_eta_2pt6():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta2pt6'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta2pt6', 'etaj1_deta2pt6', 'phij1_deta2pt6',
             'ptj2_deta2pt6',
             'etaj2_deta2pt6', 'phij2_deta2pt6', 'dRjj_deta2pt6',
             'mjj_deta2pt6',
             'detajj_deta2pt6', 'maa_deta2pt6', 'pta1_deta2pt6',
             'pta2_deta2pt6',
             'THT_deta2pt6', 'MET_deta2pt6', 'TET_deta2pt6']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_2pt6/'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=False)


def on_discovery_contour_delta_eta_2pt6_log():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta2pt6'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta2pt6', 'etaj1_deta2pt6', 'phij1_deta2pt6',
             'ptj2_deta2pt6',
             'etaj2_deta2pt6', 'phij2_deta2pt6', 'dRjj_deta2pt6',
             'mjj_deta2pt6',
             'detajj_deta2pt6', 'maa_deta2pt6', 'pta1_deta2pt6',
             'pta2_deta2pt6',
             'THT_deta2pt6', 'MET_deta2pt6', 'TET_deta2pt6']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_2pt6/log_'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=True)


def on_discovery_contour_delta_eta_3pt6():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta3pt6'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta3pt6', 'etaj1_deta3pt6', 'phij1_deta3pt6',
             'ptj2_deta3pt6',
             'etaj2_deta3pt6', 'phij2_deta3pt6', 'dRjj_deta3pt6',
             'mjj_deta3pt6',
             'detajj_deta3pt6', 'maa_deta3pt6', 'pta1_deta3pt6',
             'pta2_deta3pt6',
             'THT_deta3pt6', 'MET_deta3pt6', 'TET_deta3pt6']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_3pt6/'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=False)


def on_discovery_contour_delta_eta_3pt6_log():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + 'ma100MeV_L1pt8-2pt4TeV_deta3pt6'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_deta3pt6', 'etaj1_deta3pt6', 'phij1_deta3pt6',
             'ptj2_deta3pt6',
             'etaj2_deta3pt6', 'phij2_deta3pt6', 'dRjj_deta3pt6',
             'mjj_deta3pt6',
             'detajj_deta3pt6', 'maa_deta3pt6', 'pta1_deta3pt6',
             'pta2_deta3pt6',
             'THT_deta3pt6', 'MET_deta3pt6', 'TET_deta3pt6']
    stacked_file_names = [
            './kins/on_discovery_contour_delta_eta_3pt6/log_'
            + name for name in names]
    ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 1.8$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.0$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.2$ TeV $)$',
              r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma) \; (\Lambda = 2.4$ TeV $)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0,1,2,3]
        bg_divs = [4, 12]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      xlabel=label, stacked=True, logy=True)



def pre_select():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/new_pre_select'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    names = ['ptj1_pre', 'etaj1_pre', 'phij1_pre',
             'ptj2_pre',
             'etaj2_pre', 'phij2_pre', 'dRjj_pre',
             'mjj_pre',
             'detajj_pre', 'maa_pre', 'pta1_pre',
             'pta2_pre',
             'THT_pre', 'MET_pre', 'TET_pre']
    stacked_file_names = [
            './kins/pre_select/' + 'log_' + name for name in names]
    ylabel = r'a.u.'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    for file_name, s_file, label in zip(
            file_names, stacked_file_names, xlabels):
        sig_divs = [0]
        bg_divs = [1, 9]
        kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                      out_file_name=s_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=True,
                      xlabel=label, stacked=True, logy=True,
                      stack_bg=False)

def pre_select_no_gg():
    file_name = (
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/pre_select_no_gg'
            + '/Output/Histos/MadAnalysis5job_0/selection_0.py')
    out_file_name = (
            './kins/pre_select/deta_no_ggs.png')
    ylabel = r'a.u.'

    labels = [r"$qq' \; \to \; jj + ax \; (\to \; \gamma\gamma)$",
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabel = r'$\Delta \eta^{jj}$ (GeV)'

    sig_divs = [0]
    bg_divs = [1, 9]
    kin_histo_sig_bg(file_name, sig_divs, bg_divs,
                  out_file_name=out_file_name, labels=labels,
                  ylabel=ylabel, save=True, norm_one=True,
                  xlabel=xlabel, stack_bg=False)


def old_style_four_cuts():
    file_names = [
            './mad_analyses/four_cuts_eff_flow_chart'
            + '/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(17)]
    names = ['ptj1', 'etaj1', 'phij1',
             'ptj2',
             'etaj2', 'phij2', 'dRjj',
             'mjj',
             'detajj', 'maa', 'pta1',
             'pta2',
             'THT', 'MET', 'TET', 'dRaa', 'detaaa']
    norm_one_file_names = [
            './kins/four_cuts_eff_flow/'
            + name for name in names]
    norm_one_ylabel = r'a.u.'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)',
               r'$\Delta R^{\gamma\gamma}$', r'$\Delta \eta^{\gamma\gamma}$']

    for file_name, n_file, label in zip(
            file_names, norm_one_file_names, xlabels):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label)

#new_kin_plots()
#on_discovery_contour_delta_eta_2()
#on_discovery_contour_delta_eta_2_log()
#on_discovery_contour_delta_eta_2pt6()
#on_discovery_contour_delta_eta_2pt6_log()
#on_discovery_contour_delta_eta_3pt6()
#on_discovery_contour_delta_eta_3pt6_log()
#pre_select()
#pre_select_no_gg()
old_style_four_cuts()
