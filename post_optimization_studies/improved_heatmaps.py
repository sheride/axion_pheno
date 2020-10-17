#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:38:13 2020

@author: elijahsheridan
"""

import numpy as np
import opt_helper as opt
import bisect as bs
import scipy
import matplotlib.pyplot as plt

def cross_sec_heatmap():
    ms = np.log10([1, 1e3, 1e5])
    Ls = np.array([i/2 for i in range(2,9)])
    # in picobarns
    cross_secs = np.array([[10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555],
                           [10.09, 2.291, 1.068, 0.6473, 0.4395, 0.32, 0.2446],
                           [8.523, 1.777, 0.8011, 0.4779, 0.3227, 0.2344, 0.1788]])

    opt.smooth_heatmap_from_irreg_grid(ms, Ls, cross_secs,
                                       '$m_a$ [$\log_{10}$ MeV]',
                                       '$\Lambda$ [TeV]',
                                       'Cross Section $\sigma$ [pb]',
                                       save_file='cross_sec_new')


def Gamma(m_a=1e6, Lambda=1e12):
    alpha = 1/137
    return (4 * np.pi * alpha**2 * m_a**3) / Lambda**2


def decay_length_heatmap():
    num_thetas = 10000
    data_pts_per_row = 500

    no_select_file_name = (
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + '1MeV_axion_rapidity_full_data/Output/'
            + 'Histos/MadAnalysis5job_0/selection_0.py')
    select_file_name = (
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
            + 'post_optimization_studies/mad_analyses/'
            + '1MeV_axion_rapidity_with_selections/Output/'
            + 'Histos/MadAnalysis5job_0/selection_0.py')
    plot_name = 'axion_decay_length_fulldata'

    thetas = opt.theta_monte_carlo(select_file_name, num_thetas)

    m_as = np.linspace(2, 17, data_pts_per_row) * 10**6
    Lambdas = np.linspace(1, 4, data_pts_per_row) * 10**12
    xticks = np.linspace(2, 17, data_pts_per_row)
    yticks = np.linspace(1, 4, data_pts_per_row)

    percentages = []
    for m in m_as:
        temp = []
        for L in Lambdas:
            data = np.sin(thetas) * (3e8 / Gamma(m, L)) * 6.582119e-16
            index = bs.bisect_left(np.sort(data), 1.25)
            temp.append(index/len(data))
        percentages.append(temp)

    opt.smooth_heatmap_from_irreg_grid(xticks, yticks, percentages,
                                       '$m_a$ [MeV]',
                                       '$\Lambda$ [TeV]',
                                       'Fraction of Axions Decaying Before 1.25 m',
                                       save_file=plot_name+'_smooth')


def last_opt_heatmap():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/second_sdEta_mjj_optimization'
    specific_folder_start = '/second_analysis_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [2.6, 3.1, 3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    r = 0.25

    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[folder + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    clabel = r'$\frac{S}{\sqrt{S+B+(' + str(r) + '\cdot B)^2}}$'

    opt.smooth_heatmap_from_irreg_grid(mmjj_cuts, delta_eta_cuts, np.transpose(sig),
                                       '$m^{jj}$ [GeV]',
                                       '$\Delta \eta^{jj}$',
                                       clabel,
                                       save_file='final_opt')


def photon_opt_heatmap():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/pta_maa_optimization/tight_analyses'
    specific_folder_start = '/analysis_tight_pta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    pta_cuts = [100 + 50 * i for i in range(9)]
    maa_cuts = [200 + 50 * i for i in range(11)]
    r = 0.25

#    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[outer_path + specific_folder_start + str(pta_cut) + '_maa'
              + str(maa_cut) + inner_path
              for maa_cut in maa_cuts] for pta_cut in pta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    clabel = r'$\frac{S}{\sqrt{S+B+(' + str(r) + '\cdot B)^2}}$'

    opt.smooth_heatmap_from_irreg_grid(maa_cuts, pta_cuts,
                                       np.transpose(sig),
                                       '$m^{\gamma\gamma}$ [GeV]',
                                       '$p_T^\gamma$ [GeV]',
                                       clabel,
                                       save_file='second_opt')


def final_kin_plots():
    file_names = [
            '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/'
            + 'second_sdEta_mjj_optimization/lumi_and_kin_plots/'
            'four_cuts_lum40_fixed/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    stacked_file_names = [
            './kins/selection_' + str(i) + '_stacked' for i in range(16)]
#    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    # four cuts
    cut = [None, None, None, None, None, None, None, 750, 3.6, 500, 300,
           None, None, None, None]
    x_maxes = [None, None, None, None, None, None, None, 4000, None, None,
               None, None, None, None, None]

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ [GeV]', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ [GeV]', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ [GeV]',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ [GeV]',
               r'$p_T^{\gamma_1}$ [GeV]', r'$p_T^{\gamma_2}$ [GeV]',
               r'$THT$ [GeV]', r'$MET$ [GeV]', r'$TET$ [GeV]']

    histtypes = ['step', 'stepfilled', 'stepfilled']
    linestyles = ['dotted', 'solid', 'solid']


    for file_name, s_file, label, c, m in zip(
            file_names, stacked_file_names, xlabels, cut,
            x_maxes):
        divisions = [0, 1, 9]
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label, min_x=c, max_x=m, stacked=True,
                      histtypes=histtypes,
                      linestyles=linestyles)


def disc_contour_jet_opt():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/post_optimization_studies/disc_contour_jet_optimization/'
    specific_folder_start = 'disc_contour_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [2.6, 3.1, 3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    r = 0.25

    files = [[outer_path + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    print(signal)
    print(bg)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    print(sig)

    clabel = r'$\frac{S}{\sqrt{S+B+(' + str(r) + '\cdot B)^2}}$'

    opt.smooth_heatmap_from_irreg_grid(mmjj_cuts, delta_eta_cuts, np.transpose(sig),
                                       '$m^{jj}$ [GeV]',
                                       '$\Delta \eta^{jj}$',
                                       clabel,
                                       save_file='disc_contour_jet_opt')



def last_opt_heatmap_3pt6():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/second_sdEta_mjj_optimization'
    specific_folder_start = '/second_analysis_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    r = 0.25

    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[folder + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)

    clabel = r'$\frac{S}{\sqrt{S+B+(' + str(r) + '\cdot B)^2}}$'

    opt.smooth_heatmap_from_irreg_grid(mmjj_cuts, delta_eta_cuts, np.transpose(sig),
                                       '$m^{jj}$ [GeV]',
                                       '$\Delta \eta^{jj}$',
                                       clabel,
                                       save_file='axion_significance_vs_selection_jets_3pt6')


def last_opt_1d():
    outer_path = '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/optimization/second_sdEta_mjj_optimization'
    specific_folder_start = '/second_analysis_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    r = 0.25

    folder = outer_path + '/tight_r0.25_maa500_pta300'
    files = [[folder + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = signal / np.sqrt(signal + bg + (bg * r)**2)
    sig = sig[0]

    pts = np.linspace(mmjj_cuts[0], mmjj_cuts[-1], 100)
    f = scipy.interpolate.interp1d(mmjj_cuts, sig, kind='cubic')
    interp = [f(pt) for pt in pts]
    plt.plot(pts, interp)
#    plt.ylim(0, 5);
    plt.xlabel(r'$m^{jj}$ [GeV]');
    plt.ylabel(r'Significance $\frac{S}{\sqrt{S+B+(' + str(r) + '\cdot B)^2}}$')
    plt.savefig('deta3pt6_sig_jet_opt', dpi=300, bbox_inches='tight')


#last_opt_heatmap()
#final_kin_plots()
#photon_opt_heatmap()
#disc_contour_jet_opt()
#last_opt_heatmap_3pt6()
last_opt_1d()
