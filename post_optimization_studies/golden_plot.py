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


def lum40_axion_f1(L):
    return (-2.5154211907209363 + (23.912381315486634) * L**-1
            + (-57.71296126961569) * L**-2 + (93.46113396524179) * L**-3
            + (-32.90611649159172) * L**-4)
def lum40_axion_f2(L):
    return (-0.5572149118125576 + (5.067942761770328) * L**-1
            + (5.251320167043338) * L**-2 + (6.086989211221611) * L**-3
            + (8.389716388585496) * L**-4)
def lum40_axion_f3(L):
    return (-0.5187186981843829 + (4.854734812156504) * L**-1
            + (2.565114151442829) * L**-2 + (7.8062331568407) * L**-3
            + (9.531380284984223) * L**-4)
def lum40_axion_f1_signal(L):
    return (-22.24417839 + 165.7363162 * L**-1 + 20.29382796 * L**-2 -
            335.10514762 * L**-3  + 938.32431817 * L**-4)


def lum150_axion_f1(L):
    return (-3.257142568307139 + (30.260474427228775) * L**-1
            + (-72.99760882930345) * L**-2 + (107.31521384412297) * L**-3
            + (-22.947204324862472) * L**-4)
def lum150_axion_f2(L):
    return (-0.28324777181465166 + (1.660021385486594) * L**-1
            + (22.87599671780342) * L**-2 + (-26.04363327447632) * L**-3
            + (40.16425274864981) * L**-4)
def lum150_axion_f3(L):
    return (-0.0749510483272785 + (-0.3538643392576636) * L**-1
            + (27.01501103088837) * L**-2 + (-36.96211990246441) * L**-3
            + (48.74929845709839) * L**-4)
def lum150_axion_f1_signal(L):
    return (-83.41683795170161 + (621.5229566609216) * L**-1
            + (76.03297794654094) * L**-2 + (-1256.5393382227044) * L**-3
            + (3518.619501166621) * L**-4)


def lum1000_axion_f1(L):
    return (-2.294476049006856 + (19.217424006594676) * L**-1
            + (-25.661310955705353) * L**-2 + (21.137821929926293) * L**-3
            + (40.10519212530763) * L**-4)

def lum1000_axion_f2(L):
    return (1.3783060640517535 + (-16.12443506001423) * L**-1
            + (93.08090007653298) * L**-2 + (-144.29138923334872) * L**-3
            + (118.46088112187395) * L**-4)
def lum1000_axion_f3(L):
    return (1.8412163018880618 + (-20.761920739113734) * L**-1
            + (106.88728516260039) * L**-2 + (-170.82431305953347) * L**-3
            + (135.36197221922728) * L**-4)
def lum1000_axion_f1_signal(L):
    return (-556.0560424016213 + (4143.024542960473) * L**-1
            + (507.8196172653814) * L**-2 + (-8377.80729108513) * L**-3
            + (23457.147584419014) * L**-4)


def lum3000_axion_f1(L):
    return (-1.9024208712179056 + (14.983500618273148) * L**-1
            + (-8.887453119978936) * L**-2 + (-7.4077928218671385) * L**-3
            + (58.639826094525446) * L**-4)
def lum3000_axion_f2(L):
    return (2203.098316453475 + (-24829.696074598978) * L**-1
            + (126772.58523253431) * L**-2 + (-199690.23485826558) * L**-3
            + (153068.23124810663) * L**-4)
def lum3000_axion_f3(L):
    return (1.8808574908538214 + (-21.425914662781086) * L**-1
            + (113.48315916875043) * L**-2 + (-177.9314070089787) * L**-3
            + (139.41857013882938) * L**-4)
def lum3000_axion_f1_signal(L):
    return (2.393069519236476 + (-26.56735676892952) * L**-1
            + (129.12825109501418) * L**-2 + (-207.35477124887493) * L**-3
            + (157.82604799331523) * L**-4)

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


def lum40_axion_sigs():
    m = [1e-3, 1, 100, 500]
    L = [1, 4]
    f = [[lum40_axion_f1], [lum40_axion_f2], [lum40_axion_f3]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap'
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


def lum40_axion_sigs_scaling():
    m = [1 * 10**-3, 1 * 10**-1]
    L = [1, 4]
    f = [[lum40_axion_f1_signal]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_small_new'
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig_scale',
                                  [], [], [],
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=False, savefile=savefile,
                                  log_mode=True, scaling=ax_scaling,
                                  xres=500, yres=500)


def lum150_axion_sigs():
    m = [1e-3, 1, 100, 500]
    L = [1, 4]
    f = [[lum150_axion_f1], [lum150_axion_f2], [lum150_axion_f3]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_lum150'
    bannedlabels = [r'$\Lambda < 2m_\chi$', 'Axions Escape']
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig_lum150',
                                  ['ax_unitarity_ban', 'ax_lifetime_ban'],
                                  [cond_ax_unitarity, cond_axion_lifetime],
                                  bannedlabels,
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=True, savefile=savefile,
                                  log_mode=True, save_contour=True)


def lum1000_axion_sigs():
    m = [1e-3, 1, 100, 500]
    L = [1, 4]
    f = [[lum1000_axion_f1], [lum1000_axion_f2], [lum1000_axion_f3]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_lum1000'
    bannedlabels = [r'$\Lambda < 2m_\chi$', 'Axions Escape']
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig_lum1000',
                                  ['ax_unitarity_ban', 'ax_lifetime_ban'],
                                  [cond_ax_unitarity, cond_axion_lifetime],
                                  bannedlabels,
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=True, savefile=savefile,
                                  log_mode=True, save_contour=True)


def lum3000_axion_sigs():
    m = [1e-3, 1, 100, 500]
    L = [1, 4]
    f = [[lum1000_axion_f1], [lum1000_axion_f2], [lum1000_axion_f3]]
    xlabel = '$m_a$ [log$_{10}$(GeV)]'
    ylabel = '$\Lambda$ [TeV]'
    savefile = 'axion_heatmap_lum3000'
    bannedlabels = [r'$\Lambda < 2m_\chi$', 'Axions Escape']
    opt.coupling_mass_sig_heatmap(m, L, f, 'axion_sig_lum3000',
                                  ['ax_unitarity_ban', 'ax_lifetime_ban'],
                                  [cond_ax_unitarity, cond_axion_lifetime],
                                  bannedlabels,
                                  xlabel=xlabel, ylabel=ylabel,
                                  force_assemble=True, savefile=savefile,
                                  log_mode=True, save_contour=True)


#anapole_sigs()
#fig = plt.gcf()
#fig.clf()
#lum40_axion_sigs()
#fig = plt.gcf()
#fig.clf()
#lum40_axion_sigs_scaling()
#lum150_axion_sigs()
#lum1000_axion_sigs()
#lum3000_axion_sigs()
#lum40_axion_sigs()
