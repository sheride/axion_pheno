#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 13:06:07 2020

@author: elijahsheridan
"""

import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import opt_helper as opt
import matplotlib.patches as mpatches

import time

def ax_to_aa_Gamma(m_a=1e6, Lambda=1e12):
    alpha = 1/137
    return (4 * np.pi * alpha**2 * m_a**3) / Lambda**2

def ax_scaling(m, l):
    eta_filename = (
        '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
        + 'post_optimization_studies/mad_analyses/1MeV_axion_rapidity/Output/'
        + 'Histos/MadAnalysis5job_0/selection_0.py')
    thetas = opt.theta_monte_carlo(eta_filename, 500)

    lengths = np.sort(
            np.sin(thetas) * (3e8 / ax_to_aa_Gamma(m, l)) * 6.582119e-16)
    percent = np.searchsorted(lengths, 1.25, side='right') / len(lengths)
    return percent

def cond(percent): return percent < 0.95

for lumi in [40, 150, 1000, 3000]:
    start = time.time()

    # prelim vars
    ratio = 0.25
    res = 1000


    path = ('../optimization/second_sdEta_mjj_optimization/lumi_and_kin_plots/'
                  + 'four_cuts_lum{}/Output/HTML/MadAnalysis5job_0/index.html'.format(lumi))

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
            [[cs/cross_sec[0] for cs in cross_sec] for cross_sec in cross_secs])

    # importing a single signal, background data point
    signal, _, bg, __ = opt.sig_and_bg_from_html(path)

    # scaling signal, finding significance
    signals = signal * scalings
    sigs = signals / np.sqrt(signals + bg + (bg * ratio)**2)
    flat_sigs = sigs.flatten()

    # interpolation
    grid = np.array(
            [[[x,y] for x in np.linspace(ext[0], ext[1], res)]
            for y in np.linspace(ext[2], ext[3], res)])
    interp = scipy.interpolate.griddata(mL_pairs_flat, flat_sigs, grid)

    # heatmap
    plt.imshow(interp, cmap='plasma', origin='lower', extent=ext,
               aspect='auto')
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
    curve = plt.plot(cms, cLs, linewidth=3, linestyle='dashed', color='gray')

    # lifetime ban
    #percent = [
    #        [ax_scaling(10**item[0] * 1e9, item[1] * 1e12) for item in row]
    #        for row in grid]
    #np.save('new_heatmap_lifetime_percents', percent)
    percent = np.load(
            './new_heatmap_lifetime_percents.npy')
    banned = [[[0,0,0,0.5] if cond(item) else [1,1,1,0] for item in row]
              for row in percent]

    plt.imshow(banned, origin='lower', extent=ext, aspect='auto')
    zone = mpatches.Patch(color=[0,0,0,0.5])


    labels = ['Discovery Contour', 'Axions Escape Collider']
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    plt.legend(handles=[curve[0], zone], labels=labels,
                   bbox_to_anchor=(0.98, 0.98), loc=1, borderaxespad=0.)
    plt.ylabel(r'{}'.format(ylabel))
    plt.xlabel(r'{}'.format(xlabel))
    cbar.set_label('Signal Significance', rotation=90)
    cbar.ax.get_yaxis().labelpad = 8

    fig = plt.gcf()
    fig.set_size_inches(12, 8)
    plt.savefig('./sept_2020_plots/sig_vs_ma-L/sig_ma_L_lum'+str(lumi),
                dpi=300, bbox_inches='tight')

    end = time.time()
    plt.clf()
    print(end - start)
