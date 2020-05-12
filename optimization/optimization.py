#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:58:19 2020

@author: elijahsheridan
"""

import opt_helper as opt
import numpy as np


def sdEta_mjj_optimization_heatmap(smooth=False, contour=False):
    outer_path = './first_sdEta_mjj_optimization/analyses/analysis_deltaeta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    delta_eta_cuts = [2.6, 3.1, 3.6, 4.1, 4.6, 5.1, 5.6, 6.1]
    mmjj_cuts = [120, 500, 750, 1000, 1250, 1500, 1750, 2000]
    ratios = [0, 0.1, 0.15, 0.25]

    files = [[outer_path + str(ecut) + '_mmjj_' + str(mcut) + inner_path
              for mcut in mmjj_cuts] for ecut in delta_eta_cuts]

    signal, bg = opt.sig_heatmap_html_extract(files)

    sig = np.array([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                    for ratio in ratios])

    for array, r in zip(sig, ratios):
        label = r'$\frac{S}{\sqrt{S+B+(' + str(r) + r'\cdot B)^2}}$'
        file_name = (
                './first_sdEta_mjj_optimization/'
                + 'sdeta_mjj_optimization_heatmap_r' + str(r) + '.png')
        opt.heatmap(array, mmjj_cuts, delta_eta_cuts, label=label,
                    xlabel=r'$m^{jj}$ (GeV)', ylabel=r'$\Delta \eta^{jj}$',
                    file_name=file_name, save=True, smooth=smooth,
                    contour=contour)


def pta_maa_optimization_heatmap(smooth=False, contour=False):
    outer_path_loose = ('./pta_maa_optimization/loose_analyses/'
                        + 'analysis_loose_pta')
    outer_path_tight = ('./pta_maa_optimization/tight_analyses/'
                        + 'analysis_tight_pta')
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'

    ptacuts = [100, 150, 200, 250, 300, 350, 400, 450, 500]
    maacuts = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
    ratios = [0, 0.1, 0.15, 0.25]

    loose_files = [[outer_path_loose + str(pcut) + '_maa' + str(mcut)
                    + inner_path for mcut in maacuts] for pcut in ptacuts]
    tight_files = [[outer_path_tight + str(pcut) + '_maa' + str(mcut)
                    + inner_path for mcut in maacuts] for pcut in ptacuts]

    lsignal, lbg = opt.sig_heatmap_html_extract(loose_files)
    tsignal, tbg = opt.sig_heatmap_html_extract(tight_files)

    lsig = np.array([lsignal / np.sqrt(lsignal + lbg + (lbg * ratio)**2)
                    for ratio in ratios])
    tsig = np.array([tsignal / np.sqrt(tsignal + tbg + (tbg * ratio)**2)
                    for ratio in ratios])

    for array, r in zip(lsig, ratios):
        label = r'$\frac{S}{\sqrt{S+B+(' + str(r) + r'\cdot B)^2}}$'
        file_name = (
                './pta_maa_optimization/loose_pta_maa_optimization_heatmap_r'
                + str(r) + '.png')
        opt.heatmap(array, maacuts, ptacuts, label=label,
                    xlabel=r'$m^{\gamma\gamma}$ (GeV)',
                    ylabel=r'$p_T^{\gamma_1}$ (GeV)',
                    file_name=file_name, smooth=smooth, contour=contour,
                    save=True)

    for array, r in zip(tsig, ratios):
        label = r'$\frac{S}{\sqrt{S+B+(' + str(r) + r'\cdot B)^2}}$'
        file_name = (
                './pta_maa_optimization/tight_pta_maa_optimization_heatmap_r'
                + str(r) + '.png')
        opt.heatmap(array, maacuts, ptacuts, label=label,
                    xlabel=r'$m^{\gamma\gamma}$ (GeV)',
                    ylabel=r'$p_T^{\gamma_1}$ (GeV)',
                    file_name=file_name, smooth=smooth, contour=contour,
                    save=True)


def second_sdEta_mjj_optimization_heatmap(smooth=False, contour=False):
    outer_path = './second_sdEta_mjj_optimization'
    specific_folder_start = '/second_analysis_sdEta'
    inner_path = '/Output/HTML/MadAnalysis5job_0/index.html'
    folders = [
            outer_path + '/loose_r0.1_maa350_pta250',
            outer_path + '/loose_r0.25_maa400_pta350',
            outer_path + '/tight_r0.1_maa400_pta250',
            outer_path + '/tight_r0.25_maa500_pta300']

    delta_eta_cuts = [2.6, 3.1, 3.6, 4.1]
    mmjj_cuts = [750, 1000, 1250, 1500, 1750, 2000]
    ratios = [0, 0.1, 0.15, 0.25]

    files = [[[folder + specific_folder_start + str(ecut) + '_mjj' + str(mcut)
               + inner_path for mcut in mmjj_cuts] for ecut in delta_eta_cuts]
             for folder in folders]

    signal = [None for i in range(len(folders))]
    bg = [None for i in range(len(folders))]
    for i, file_set in enumerate(files):
        signal[i], bg[i] = opt.sig_heatmap_html_extract(file_set)

    signal = np.array(signal)
    bg = np.array(bg)

    sig = np.array([signal / np.sqrt(signal + bg + (bg * ratio)**2)
                    for ratio in ratios])

    for array, r in zip(sig, ratios):
        for i, dataset in enumerate(array):
            label = r'$\frac{S}{\sqrt{S+B+(' + str(r) + r'\cdot B)^2}}$'
            file_name = (
                    folders[i] + '/' + folders[i][-13:] +
                    'sdeta_mjj_optimization_heatmap_r'
                    + str(r) + '.png')
            opt.heatmap(dataset, mmjj_cuts, delta_eta_cuts, label=label,
                        xlabel=r'$m^{jj}$ (GeV)', ylabel=r'$\Delta \eta^{jj}$',
                        file_name=file_name, smooth=smooth, contour=contour,
                        save=True)


sdEta_mjj_optimization_heatmap()
sdEta_mjj_optimization_heatmap(smooth=True)
sdEta_mjj_optimization_heatmap(contour=True)
pta_maa_optimization_heatmap()
pta_maa_optimization_heatmap(smooth=True)
pta_maa_optimization_heatmap(contour=True)
second_sdEta_mjj_optimization_heatmap()
second_sdEta_mjj_optimization_heatmap(smooth=True)
second_sdEta_mjj_optimization_heatmap(contour=True)
