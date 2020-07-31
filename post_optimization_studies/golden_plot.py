#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:12:40 2020

@author: elijahsheridan
"""

import numpy as np
import opt_helper as opt
import matplotlib.pyplot as plt

# first index m_a bin, second index Lambda bin (< or > 1000 1 TeV)
def f11(Lambda): return np.exp(8.73082 - (0.00562036 * Lambda))
def f12(Lambda): return np.exp(5.59300 - (0.00248254 * Lambda))
def f21(Lambda): return np.exp(8.75042 - (0.00564871 * Lambda))
def f22(Lambda): return np.exp(5.60075 - (0.00249904 * Lambda))
def f31(Lambda): return np.exp(8.75322 - (0.00565945 * Lambda))
def f32(Lambda): return np.exp(5.57084 - (0.00247707 * Lambda))
def f41(Lambda): return np.exp(8.63390 - (0.00558681 * Lambda))
def f42(Lambda): return np.exp(5.59985 - (0.00255277 * Lambda))
def f51(Lambda): return np.exp(8.32984 - (0.00546720 * Lambda))
def f52(Lambda): return np.exp(5.52377 - (0.00266114 * Lambda))
def f61(Lambda): return np.exp(7.98429 - (0.00552884 * Lambda))
def f62(Lambda): return np.exp(5.17255 - (0.00271710 * Lambda))
def f71(Lambda): return np.exp(7.42313 - (0.00550587 * Lambda))
def f72(Lambda): return np.exp(4.68883 - (0.00277156 * Lambda))
def f81(Lambda): return np.exp(4.14728 - (0.00560839 * Lambda))
def f82(Lambda): return np.exp(1.29639 - (0.00275750 * Lambda))
def f91(Lambda): return np.exp(1.29639 - (0.00275750 * 1000))
def f92(Lambda): return np.exp(1.29639 - (0.00275750 * Lambda))


def axion_f1(L):
    return (-2.51542119 + 23.91238132 * L**-1 - 57.71296127 * L**-2 +
            93.46113397 * L**-3 - 32.90611649 * L**-4)
def axion_f2(L):
    return (-0.59296336 + 5.43685559 * L**-1 + 3.88050494 * L**-2 +
            8.25838152 * L**-3 + 7.15274859 * L**-4)
def axion_f3(L):
    return (-1.3918001 + 13.86465396 * L**-1 - 30.91413384 * L**-2 +
            60.83783977 * L**-3 - 20.67889376 * L**-4)

def axion_f1_signal(L):
    return (-22.24417839 + 165.7363162 * L**-1 + 20.29382796 * L**-2 -
            335.10514762 * L**-3  + 938.32431817 * L**-4)

def cond_unitarity(m, L): return L < 2 * m


def ax_to_aa_Gamma(m_a=1e6, Lambda=1e12):
    alpha = 1/137
    return (4 * np.pi * alpha**2 * m_a**3) / Lambda**2


def anapole_sigs():
    """broken"""
    m = [1,50,100,250,500,750,1000,2000,3000]
    L = [500,1000,2500]
    f = [[f11, f12], [f21, f22], [f31, f32], [f41, f42], [f51, f52],
         [f61, f62], [f71, f72], [f81, f82], [f91, f92]]
    xlabel = '$m_\chi$ [GeV]'
    ylabel = '$\Lambda$ [GeV]'
    savefile = 'anapole_heatmap_TEST'
    bannedlabels = [r'$\Lambda < 2m_\chi$']
    opt.coupling_mass_sig_heatmap(m, L, f, 'anapole_sig', ['anapole_banned'],
                                  [cond_unitarity], bannedlabels,
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=False, savefile=savefile,
                                  log_mode=True)


def cond_axion_lifetime(m, l):
    eta_filename = (
        '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
        + 'post_optimization_studies/mad_analyses/1MeV_axion_rapidity/Output/'
        + 'Histos/MadAnalysis5job_0/selection_0.py')
    thetas = opt.theta_monte_carlo(eta_filename, 500)

    m *= 1e9
    l *= 1e12

    lengths = np.sort(
            np.sin(thetas) * (3e8 / ax_to_aa_Gamma(m, l)) * 6.582119e-16)
    percent = np.searchsorted(lengths, 1.25, side='right') / len(lengths)
    return percent < 0.95


def cond_ax_unitarity(m, L): return L * 1000 < 2 * m


def axion_sigs():
    m = [1e-3, 1, 100, 500]
    L = [1, 4]
    f = [[axion_f1], [axion_f2], [axion_f3]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_LOG'
    bannedlabels = [r'$\Lambda < 2m_\chi$', 'Axions Escape']
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig',
                                  ['ax_unitarity_ban', 'ax_lifetime_ban'],
                                  [cond_ax_unitarity, cond_axion_lifetime],
                                  bannedlabels,
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=False, savefile=savefile,
                                  log_mode=True, save_contour=True)

def ax_scaling(m, l):
    eta_filename = (
        '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
        + 'post_optimization_studies/mad_analyses/1MeV_axion_rapidity/Output/'
        + 'Histos/MadAnalysis5job_0/selection_0.py')
    thetas = opt.theta_monte_carlo(eta_filename, 500)

    m *= 1e9
    l *= 1e12

    lengths = np.sort(
            np.sin(thetas) * (3e8 / ax_to_aa_Gamma(m, l)) * 6.582119e-16)
    percent = np.searchsorted(lengths, 1.25, side='right') / len(lengths)
    return percent

def axion_sigs_scaling():
    m = [1 * 10**-3, 1 * 10**-1]
    L = [1, 4]
    f = [[axion_f1_signal]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_small_new'
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig_scale',
                                  [], [], [],
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=False, savefile=savefile,
                                  log_mode=True, scaling=ax_scaling,
                                  xres=500, yres=500)


#anapole_sigs()
#fig = plt.gcf()
#fig.clf()
#axion_sigs()
#fig = plt.gcf()
#fig.clf()
axion_sigs_scaling()
