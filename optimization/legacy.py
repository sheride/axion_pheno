#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:39:50 2020

@author: elijahsheridan
"""

import opt_helper as opt
import numpy as np

# Don't think I ever actually needed pta/maa optimization histos?


def pta_maa_norm_one_histos():
    file_names = ['./pta_maa_optimization/'
                  + 'loose_analysis_pta_maa_2.6_mjj_1250/Output/Histos/'
                  + 'MadAnalysis5job_0/selection_' + str(i) + '.py' for
                  i in range(16)]
    out_file_names = ['selection_'+str(i) for i in range(16)]
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

    for file_name, out_file_name, xlabel in zip(file_names, out_file_names,
                                                xlabels):
        divisions = [0, 1, 9]  # for some reason gen_norm_one_histo overwrites?
        opt.gen_histo(file_name, divisions,
                      out_file_name=out_file_name, labels=labels,
                      ylabel=ylabel, save=True, norm_one=False, xlabel=xlabel)
