#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:50:03 2020

@author: elijahsheridan
"""

from __future__ import division
import opt_helper as opt
import numpy as np
import matplotlib.pyplot as plt
import bisect as bs

#file_name = (
#        '/Users/elijahsheridan/MG5_aMC_v2_6_5/axion_pheno/'
#        + 'post_optimization_studies/mad_analyses/1MeV_axion_rapidity/Output/'
#        + 'Histos/MadAnalysis5job_0/selection_0.py')

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

def Gamma(m_a=1e6, Lambda=1e12):
    alpha = 1/137
    return (4 * np.pi * alpha**2 * m_a**3) / Lambda**2

thetas = opt.theta_monte_carlo(no_select_file_name, 1000)

m_as = [x * 10**6 for x in range(2, 18)]
Lambdas = [(x/2) * 10**12 for x in range(2,9)]

#print(m_as)
#print(Lambdas)

#plt.figure(figsize=(20,20))
i = 1
percentages = []
for L in Lambdas:
    temp = []
    for m in m_as:
        data = np.sin(thetas) * (3e8 / Gamma(m, L)) * 6.582119e-16
#        plt.subplot(len(Lambdas), len(m_as), i)
#        plt.hist(data, 15)
#        plt.title(r'$m_a$ = {:.0e}, $\Lambda$ = {:.0e}'.format(m, L))
#        i += 1
        index = bs.bisect_left(np.sort(data), 1.25)
        temp.append(index/len(data))
    percentages.append(temp)

plt.imshow(percentages, origin='lower', aspect='auto')
#plt.imshow(percentages, origin='lower')
cbar = plt.colorbar()
plt.title('Axion Decay Length')
plt.ylabel(r'$\Lambda$ (TeV)')
plt.xlabel(r'$m_a$ (MeV)')
ax = plt.gca();
xticks = [x for x in range(2, 18)]
yticks = [(x/2) for x in range(2, 9)]
ax.set_xticks(np.arange(0, len(m_as), 1))
ax.set_yticks(np.arange(0, len(Lambdas), 1))
ax.set_xticklabels(xticks)
ax.set_yticklabels(yticks)
#plt.xscale('log')
cbar.set_label('Fraction of Axions Decaying Before 1.25 m', rotation=90)
cbar.ax.get_yaxis().labelpad = 8
fig = plt.gcf()
fig.set_size_inches(12, 8)
plt.savefig(plot_name, dpi=300, bbox_inches='tight')
