#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:35:06 2020

@author: elijahsheridan
"""

import opt_helper as opt


def no_mg_cuts_histos():
    file_names = ['./pre_optimization/no_mg_cuts/ma_files/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py'
                  for i in range(16)]
    norm_one_file_names = [
            './pre_optimization/no_mg_cuts/kin_norm_one/selection_'
            + str(i) for i in range(16)]
    stacked_file_names = [
            './pre_optimization/no_mg_cuts/kin_stacked/selection_'
            + str(i) for i in range(16)]
    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    x_mins = [None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None]
    x_maxes = [None, None, None, None, None, None, None, None, None, None,
               None, None, None, None, None]

    for file_name, n_file, s_file, label, x_min, x_max in zip(
            file_names, norm_one_file_names, stacked_file_names, xlabels,
            x_mins, x_maxes):
        divisions = [0]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label, max_x=x_max, min_x=x_min)
        divisions = [0]
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label, max_x=x_max, min_x=x_min)


def no_mg_cuts_no_gg_histos():
    file_names = ['./pre_optimization/no_mg_cuts_no_gg/ma_files/Output/'
                  + 'Histos/MadAnalysis5job_0/selection_' + str(i) + '.py'
                  for i in range(16)]
    norm_one_file_names = [
            './pre_optimization/no_mg_cuts_no_gg/kin_norm_one/selection_'
            + str(i) + '_larger' for i in range(16)]
    stacked_file_names = [
            './pre_optimization/no_mg_cuts_no_gg/kin_stacked/selection_'
            + str(i) + '_larger' for i in range(16)]
    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    for file_name, n_file, s_file, label in zip(
            file_names, norm_one_file_names, stacked_file_names, xlabels):
        divisions = [0]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label)
        divisions = [0]
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label)


def no_mg_cuts_mjj_zoom_histos():
    num_bins = [20, 40, 50, 80]

    file_names = ['./pre_optimization/no_ma_cuts_mjj_zoom/ma_' + str(num) +
                  '_bins/Output/Histos/MadAnalysis5job_0/selection_0.py'
                  for num in num_bins]
    out_file_names = [
            './pre_optimization/no_ma_cuts/kin_norm_one/mjj_zoom_' +
            str(num) + '_bins' for num in num_bins]
    ylabel = r'Arbitrary Units (Normalized to Unity)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabel = r'$m^{jj}$ (GeV)'

    for file_name, out_file_name in zip(file_names, out_file_names):
        divisions = [0]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=True,
                      xlabel=xlabel)


def no_mg_cuts_mjj_more_zoom_histos():
    file_name = ('./pre_optimization/no_ma_cuts_mjj_zoom/ma_more_zoom' +
                 '/Output/Histos/MadAnalysis5job_0/selection_0.py')
    out_file_name = (
            './pre_optimization/no_ma_cuts/kin_norm_one/mjj_more_zoom')
    ylabel = r'Arbitrary Units (Normalized to Unity)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabel = r'$m^{jj}$ (GeV)'

    divisions = [0]  # for some reason gen_norm_one_histo overwrites?
    opt.gen_histo(file_name, divisions,
                  out_file_name=out_file_name, labels=labels,
                  ylabel=ylabel, save=True, norm_one=True,
                  xlabel=xlabel)


def just_sdeta_cut_histos():
    file_names = ['./pre_optimization/just_sdeta_2.5_mg_cut/ma_files/Output/'
                  + 'Histos/MadAnalysis5job_0/selection_' + str(i) + '.py'
                  for i in range(16)]
    norm_one_file_names = [
            './pre_optimization/just_sdeta_2.5_mg_cut/kin_norm_one/selection_'
            + str(i) for i in range(16)]
    stacked_file_names = [
            './pre_optimization/just_sdeta_2.5_mg_cut/kin_stacked/selection_'
            + str(i) for i in range(16)]
    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    for file_name, n_file, s_file, label in zip(
            file_names, norm_one_file_names, stacked_file_names, xlabels):
        divisions = [0]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label)
        divisions = [0]
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label)


def ht_stitching_confirm():
    file_name = ('./pre_optimization/no_ma_cuts/ma_files/Output/Histos/'
                 + 'MadAnalysis5job_0/selection_12.py')
    plot_name = './pre_optimization/no_ma_cuts/kin_norm_one/THT_stitch'
    ylabel = r'Arbitrary Units (Normalized to Unity)'
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    xlabel = r'$THT$ (GeV)'
    divisions = [0, 1, 9]
    opt.gen_histo(file_name, divisions,
                  out_file_name=plot_name, labels=labels,
                  ylabel=ylabel, save=True, norm_one=False,
                  xlabel=xlabel, logy=True)


def no_ma_cuts_histos():
    file_names = ['./pre_optimization/no_ma_cuts/ma_files/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py'
                  for i in range(16)]
    norm_one_file_names = [
            './pre_optimization/no_ma_cuts/kin_norm_one/selection_'
            + str(i) for i in range(16)]
    stacked_file_names = [
            './pre_optimization/no_ma_cuts/kin_stacked/selection_'
            + str(i) for i in range(16)]
    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    x_mins = [None, None, None, None, None, None, None, None, 2.5, None, None,
              None, None, None, None]
    x_maxes = [None, None, None, None, None, None, None, 2000, 8, 800, 800,
               None, None, None, None]

    for file_name, n_file, s_file, label, x_min, x_max in zip(
            file_names, norm_one_file_names, stacked_file_names, xlabels,
            x_mins, x_maxes):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label, max_x=x_max, min_x=x_min)
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label, max_x=x_max, min_x=x_min)


def sdEta_mjj_loose_norm_one_histos():
    file_names = ['./first_sdEta_mjj_optimization/'
                  + 'loose_analysis_sdeta_2.6_mjj_1250/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py' for
                  i in range(16)]
    out_file_names = ['./first_sdEta_mjj_optimization/loose_kin_plots/'
                      + 'selection_' + str(i) for i in range(16)]
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    ylabel = r'Arbitrary Units (Normalized to Unity)'
    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']
    # four cuts
    cut = [None, None, None, None, None, None, None, 1250, 2.6, None, None,
           None, None, None, None]

    for file_name, out_file_name, xlabel, c in zip(file_names, out_file_names,
                                                   xlabels, cut):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=True, xlabel=xlabel,
                      min_x=c)


def sdEta_mjj_tight_norm_one_histos():
    file_names = ['./first_sdEta_mjj_optimization/'
                  + 'tight_analysis_sdeta_3.6_mjj_1250/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py' for
                  i in range(16)]
    out_file_names = ['./first_sdEta_mjj_optimization/tight_kin_plots/'
                      + 'selection_' + str(i) for i in range(16)]
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    ylabel = r'Arbitrary Units (Normalized to Unity)'
    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    # four cuts
    cut = [None, None, None, None, None, None, None, 1250, 3.6, None, None,
           None, None, None, None]
    maxes = [None, None, None, None, None, None, None, None, None, 2000, 1500,
             None, None, None, None]

    for file_name, out_file_name, xlabel, c, m in zip(file_names,
                                                      out_file_names,
                                                      xlabels, cut, maxes):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=True, xlabel=xlabel,
                      max_x=m, min_x=c)


def sdEta_mjj_tight_norm_one_log_histos():
    file_names = ['./first_sdEta_mjj_optimization/'
                  + 'tight_analysis_sdeta_3.6_mjj_1250/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py' for
                  i in range(16)]
    out_file_names = ['./first_sdEta_mjj_optimization/tight_kin_plots/'
                      + 'selection_' + str(i) + '_log' for i in range(16)]
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    ylabel = r'Arbitrary Units (Normalized to Unity)'
    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    # four cuts
    cut = [None, None, None, None, None, None, None, 1250, 3.6, None, None,
           None, None, None, None]
    maxes = [None, None, None, None, None, None, None, None, None, 2000, 1500,
             None, None, None, None]

    for file_name, out_file_name, xlabel, c, m in zip(file_names,
                                                      out_file_names,
                                                      xlabels, cut, maxes):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=True, xlabel=xlabel,
                      max_x=m, min_x=c, logy=True)


def sdEta_mjj_loose_histos():
    file_names = ['./first_sdEta_mjj_optimization/'
                  + 'loose_analysis_sdeta_2.6_mjj_1250/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py' for
                  i in range(16)]
    out_file_names = ['./first_sdEta_mjj_optimization/loose_kin_plots/'
                      + 'selection_' + str(i) + '_stacked' for i in range(16)]
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    ylabel = r'Arbitrary Units (Normalized to Unity)'
    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']
    # four cuts
    cut = [None, None, None, None, None, None, None, 1250, 2.6, None, None,
           None, None, None, None]

    for file_name, out_file_name, xlabel, c in zip(file_names, out_file_names,
                                                   xlabels, cut):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False, xlabel=xlabel,
                      min_x=c)


def four_cuts_histos():
    file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/'
            'four_cuts_lum40_fixed/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    norm_one_file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/kin_norm_one/'
            + 'selection_' + str(i) for i in range(16)]
    stacked_file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/kin_stacked/'
            + 'selection_' + str(i) + '_stacked' for i in range(16)]
    norm_one_ylabel = r'Arbitrary Units (Normalized to Unity)'
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    # four cuts
    cut = [None, None, None, None, None, None, None, 750, 3.6, 500, 300,
           None, None, None, None]
    x_maxes = [None, None, None, None, None, None, None, 4000, None, None,
               None, None, None, None, None]

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    for file_name, n_file, s_file, label, c, m in zip(
            file_names, norm_one_file_names, stacked_file_names, xlabels, cut,
            x_maxes):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=n_file, labels=labels,
                      ylabel=norm_one_ylabel, save=True, norm_one=True,
                      xlabel=label, min_x=c, max_x=m)
        divisions = [0, 1, 9]
        opt.gen_histo(file_name, divisions,
                      out_file_name=s_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      xlabel=label, min_x=c, max_x=m)


def four_cuts_stacked_log_histos():
    file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/'
            'four_cuts_lum40_fixed/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in range(15)]
    plot_file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/kin_stacked'
            + '_log/selection_' + str(i) + '_stacked_log' for i in range(16)]
    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    stacked_ylabel = r'Events ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']

    # four cuts
    cut = [None, None, None, None, None, None, None, 750, 3.6, 500, 300,
           None, None, None, None]
    x_maxes = [None, None, None, None, None, None, None, None, 2000, None,
               None, None, None, None, None]

    for file_name, plot_file, label, c, m in zip(file_names, plot_file_names,
                                                 xlabels, cut, x_maxes):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=plot_file, labels=labels,
                      ylabel=stacked_ylabel, save=True, norm_one=False,
                      logy=True, xlabel=label, min_x=c, max_x=m)


def four_cuts_stacked_histos_custom_bins():
    # consider = [0, 3, 7, 10, 11, 12, 13, 15]
    consider = [0, 3, 7, 9, 10, 11]

    bins_0 = ([10 * i for i in range(100)] + [1000 + 30 * i for i in range(25)]
              + [1750, 2000])
    bins_3 = ([10 * i for i in range(40)] + [400 + 50 * i for i in range(8)]
              + [1000])
    bins_7 = ([50 * i for i in range(80)] + [4000 + 200 * i for i in range(10)]
              + [6000, 6500, 7000, 7500, 8000])
    bins_9 = ([50 * i for i in range(30)] + [1500 + 100 * i for i in range(20)]
              + [3500, 4000])
    bins_10 = ([25 * i for i in range(50)] + [1250 + 100 * i for i in range(7)]
               + [1950, 2000])
    bins_11 = ([50 * i for i in range(5)] + [250 + 100 * i for i in range(7)]
               + [950, 1000, 1250, 1500, 1750, 2000])

    plot_bins = [bins_0, bins_3, bins_7, bins_9, bins_10, bins_11]

    file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/'
            'four_cuts_lum40_fixed/Output/Histos/MadAnalysis5job_0/selection_'
            + str(i) + '.py' for i in consider]
    plot_file_names = [
            './second_sdEta_mjj_optimization/lumi_and_kin_plots/kin_stacked'
            + '_log/selection_' + str(i) + '_stacked_log_mod'
            for i in consider]

    labels = [r'$pp \; \to \; jj + ax \; (\to \; \gamma\gamma)$',
              r'$pp \; \to \; jj + \gamma\gamma \; (QCD = 0)$',
              r'$pp \; \to \; jj + \gamma\gamma$']
    ylabel = r'Events Per Bin Width ($\mathcal{L}_{int} = 40$ fb$^{-1}$)'

    xlabels = [r'$p_T^{j_1}$ (GeV)', r'$\eta^{j_1}$', r'$\phi^{j_1}$',
               r'$p_T^{j_2}$ (GeV)', r'$\eta^{j_2}$', r'$\phi^{j_2}$',
               r'$\Delta R^{jj}$', r'$m^{jj}$ (GeV)',
               r'$\Delta \eta^{jj}$', r'$m^{\gamma\gamma}$ (GeV)',
               r'$p_T^{\gamma_1}$ (GeV)', r'$p_T^{\gamma_2}$ (GeV)',
               r'$THT$ (GeV)', r'$MET$ (GeV)', r'$TET$ (GeV)']
    xlabels = [xlabels[i] for i in consider]

    # four cuts
    cut = [None, None, None, None, None, None, None, 750, 3.6, 500, 300,
           None, None, None, None]
    cut = [cut[i] for i in consider]

    for file_name, plot_file, label, bins, c in zip(
            file_names, plot_file_names, xlabels, plot_bins, cut):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=plot_file, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False,
                      logy=True, xlabel=label, bins=bins, binResize=True,
                      min_x=c)


# no_mg_cuts_histos()
# no_mg_cuts_no_gg_histos()
# just_sdeta_cut_histos()
# no_ma_cuts_histos()
# sdEta_mjj_loose_norm_one_histos()
# sdEta_mjj_tight_norm_one_histos()
# sdEta_mjj_loose_histos()
# four_cuts_histos()
# four_cuts_stacked_log_histos()
# four_cuts_stacked_histos_custom_bins()
# ht_stitching_confirm()
# sdEta_mjj_tight_norm_one_log_histos()
# no_mg_cuts_mjj_zoom_histos()
no_mg_cuts_mjj_more_zoom_histos()
