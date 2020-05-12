#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:47:50 2020

@author: elijahsheridan
"""

import opt_helper as opt
import numpy as np


def full_luminosity_comp_plot_sdEta_mjj():
    outer_path = './first_sdEta_mjj_optimization/analyses/analysis_deltaeta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [2.6, 3.6]
    delta_eta_cut_names = ['Loose', 'Tight']
    lums = [40, 150, 3000]
    ratios = [0, 0.1, 0.15, 0.25]
    file_name = './first_sdEta_mjj_optimization/lum_comparison_plot.png'

    files = [[outer_path + str(ecut) + '_lumi_' + str(lum) + inner_path
              for lum in lums] for ecut in delta_eta_cuts]
    labels = [[r'{} ($\Delta\eta > {}$, $m[j_1, j_2] > 1250$, $r={}$)'.format(
            name, cut, r) for cut, name in
            zip(delta_eta_cuts, delta_eta_cut_names)] for r in ratios]

    signal = [[None for j in range(len(files[0]))] for i in range(len(files))]
    bg = [[None for j in range(len(files[0]))] for i in range(len(files))]

    for i, file_row in enumerate(files):
        for j, file in enumerate(file_row):
            signal[i][j], _, bg[i][j], __ = opt.sig_and_bg_from_html(file)

    signal, bg = [np.array(signal), np.array(bg)]
    sig = np.array([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                    for ratio in ratios])

    opt.curve_comparison_2d(
            lums, sig, labels=labels,  xlabel=r'Luminosity $\mathcal{L}$',
            ylabel=r'Significance $\frac{S}{\sqrt{S+B+(r\cdot B)^2}}$',
            file_name=file_name, logy=True, save=True)


def full_luminosity_comp_plot_second_sdEta_mjj():
    outer_path = ('./second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum')
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    lums = [40, 150, 1000, 2000, 3000]
    ratios = [0, 0.1, 0.15, 0.25]
    file_name = ('./second_sdEta_mjj_optimization/lumi_and_kin_plots'
                 + '/second_lum_comparison_plot.png')

    files = [outer_path + str(lum) + inner_path for lum in lums]
    labels = [r'{}% Sys. Uncertainty ($r={}$)'.format(int(r*100), r)
              for r in ratios]

    signal = [None for i in range(len(files))]
    bg = [None for i in range(len(files))]

    for i, file in enumerate(files):
        signal[i], _, bg[i], __ = opt.sig_and_bg_from_html(file)

    signal, bg = [np.array(signal), np.array(bg)]
    sig = np.array([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                    for ratio in ratios])

    opt.curve_comparison_1d(
            lums, sig, labels=labels,  xlabel=r'Luminosity $\mathcal{L}$',
            ylabel=r'Significance $\frac{S}{\sqrt{S+B+(r\cdot B)^2}}$',
            file_name=file_name, logy=False, save=True)


full_luminosity_comp_plot_sdEta_mjj()
full_luminosity_comp_plot_second_sdEta_mjj()
