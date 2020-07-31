#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:14:42 2020

@author: elijahsheridan
"""

import matplotlib.pyplot as plt
import numpy as np
import opt_helper as opt


def cross_sec_vs_mass_plot():
    mass = [1e-3, 1, 50, 100]
    cross_sec = [10.16, 10.09, 9.594, 8.523]
    sigma_cross_sec = [0.074, 0.072, 0.076, 0.076]

    plt.errorbar(mass, cross_sec, yerr=sigma_cross_sec, fmt='.',
                 color='#7a8e99')
    plt.scatter(mass, cross_sec, marker='.', s=200, color='#7a8e99')
    plt.xlabel(r'$m^A$ (GeV)')
    plt.ylabel(r'$\sigma$ (pb)')

    plt.savefig('./pre_optimization/cross_sec_vs_mass.png', dpi=300,
                bbox_inches='tight')


def sig_vs_lambda_with_decay_plot():
    lambdas = [1 + 0.5 * i for i in range(7)]
    cross_secs = [0.1024, 0.009209, 0.002332, 0.0008878, 0.0004189, 0.0002226,
                  0.0001306]
    scalings = np.array([1] + [
            cross_sec/cross_secs[0] for cross_sec in cross_secs[1:]])
    lums = [40, 150, 1000, 2000, 3000]
    ratio = 0.25

    outer_path = ('./second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum')
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'
    files = [outer_path + str(lum) + inner_path for lum in lums]

    signal = [None for i in range(len(files))]
    bg = [None for i in range(len(files))]
    for i, file in enumerate(files):
        signal[i], _, bg[i], __ = opt.sig_and_bg_from_html(file)
    signal, bg = [np.array(signal), np.array(bg)]
    signals = np.transpose([sig * scalings for sig in signal])
    sigs = np.transpose([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                         for signal in signals])

    labels = [r'Luminosity $\mathcal{L} = {}$' + str(lum) for lum in lums]
    file_name = '../post_optimization_studies/sig_vs_Lambda_with_decay.png'

    opt.curve_comparison_1d(
            lambdas, sigs, labels=labels, xlabel=r'$\Lambda$ (TeV)',
            ylabel=r'Significance $\frac{S}{\sqrt{S+B+(0.25 \cdot B)^2}}$',
            logy=True, save=False)

    plt.plot(lambdas, [5 for i in lambdas], color='black',
             label=r'Discovery Potential Boundary')
    plt.legend()
    plt.legend(bbox_to_anchor=(0.98, 0.98), loc=1, borderaxespad=0.)
    for line in plt.gca().lines:
        line.set_linewidth(3.)
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def sig_vs_lambda_no_decay_plot():
    lambdas = [1 + 0.5 * i for i in range(7)]
    cross_secs = [10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555]
    scalings = np.array([1] + [
            cross_sec/cross_secs[0] for cross_sec in cross_secs[1:]])
    lums = [40, 150, 1000, 2000, 3000]
    ratio = 0.25

    outer_path = ('./second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum')
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'
    files = [outer_path + str(lum) + inner_path for lum in lums]

    signal = [None for i in range(len(files))]
    bg = [None for i in range(len(files))]
    for i, file in enumerate(files):
        signal[i], _, bg[i], __ = opt.sig_and_bg_from_html(file)
    signal, bg = [np.array(signal), np.array(bg)]
    signals = np.transpose([sig * scalings for sig in signal])
    sigs = np.transpose([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                         for signal in signals])

    labels = [r'Luminosity $\mathcal{L} = {}$' + str(lum) for lum in lums]
    file_name = '../post_optimization_studies/sig_vs_Lambda_no_decay.png'

    opt.curve_comparison_1d(
            lambdas, sigs, labels=labels, xlabel=r'$\Lambda$ (TeV)',
            ylabel=r'Significance $\frac{S}{\sqrt{S+B+(0.25 \cdot B)^2}}$',
            logy=True, save=False)

    plt.plot(lambdas, [5 for i in lambdas], color='black',
             label=r'Discovery Potential Boundary')
    plt.legend()
    plt.legend(bbox_to_anchor=(0.98, 0.98), loc=1, borderaxespad=0.)
    for line in plt.gca().lines:
        line.set_linewidth(3.)
    plt.savefig(file_name, dpi=300, bbox_inches='tight')


def cross_sec_vs_lambda_no_decay_plot():
    lambdas = [1 + 0.5 * i for i in range(7)]
    cross_secs = [10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555]
    plt.plot(lambdas, cross_secs, '-'+'o', linewidth=3, markersize=10,
             color='#7a8e99')
    plt.xlabel(r'$\Lambda$ (TeV)')
    plt.ylabel(r'$\sigma$ (pb)')
    plt.savefig('../post_optimization_studies/cross_sec_vs_lambda.png',
                dpi=300, bbox_inches='tight')


# cross_sec_vs_mass_plot()
# sig_vs_lambda_with_decay_plot()
# sig_vs_lambda_no_decay_plot()
cross_sec_vs_lambda_no_decay_plot()
