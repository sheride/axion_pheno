#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:14:42 2020

@author: elijahsheridan
"""

import matplotlib.pyplot as plt


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


cross_sec_vs_mass_plot()
