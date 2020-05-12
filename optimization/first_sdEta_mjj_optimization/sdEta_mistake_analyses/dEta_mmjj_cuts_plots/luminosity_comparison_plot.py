#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:47:50 2020

@author: elijahsheridan
"""

import matplotlib.pyplot as plt

lums = [40, 150, 3000]
tight = [6.847, 13.259, 59.30]
tight_sigma = [0.309, 0.309, 0.31]
loose = [12.592, 24.385, 109.05]
loose_sigma = [0.357, 0.358, 0.36]

plt.errorbar(lums, tight, yerr=tight_sigma, ls='none', marker='o', ms=10,
             label='Tight (sdEta > 3.6, mmjj > 1250)')
plt.errorbar(lums, loose, yerr=loose_sigma, ls='none', marker='o', ms=10,
             label='Loose (sdEta > 2.6, mmjj > 1250)')
plt.xlabel('Luminosity $\mathcal{L}$')
plt.ylabel(r'Significance $\frac{S}{\sqrt{S+B}}$')
plt.legend()
plt.savefig('luminosity_comparison', dpi=300)
# plt.yscale('log')
