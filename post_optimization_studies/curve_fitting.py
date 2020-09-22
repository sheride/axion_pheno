#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:59:45 2020

@author: elijahsheridan
"""

import numpy as np
import opt_helper as opt
import scipy.optimize as op
#import matplotlib.pyplot as plt

def exp(x, p0, p1): return np.exp(p0 + p1 * x)

def poly(x, p0, p1, p2, p3, p4): return p0 + p1 * x**-1 + p2 * x**-2 + p3 * x**-3 + p4 * x**-4

def poly2(x, p0, p1): return p0 + p1 * x**-4

lambdas = [1 + 0.5 * i for i in range(7)]
cross_secs_1MeV = [10.16, 2.43, 1.083, 0.6791, 0.4453, 0.3285, 0.2555]
cross_secs_1GeV = [10.09, 2.291, 1.068, 0.6473, 0.4395, 0.32, 0.2446]
cross_secs_100GeV = [8.523, 1.777, 0.8011, 0.4779, 0.3227, 0.2344, 0.1788]
cross_secs = [cross_secs_1MeV, cross_secs_1GeV, cross_secs_100GeV]
#scalings = np.array([[cross_sec[0]/10.16] + [
#        cs/cross_sec[0] for cs in cross_sec[1:]] for cross_sec in cross_secs])

# only using one significance, so need to divide EVERYTHING
# by the cross sec for that sig? this is an error to be fixed I think
scalings = np.array([[cs/cross_sec[0] for cs in cross_sec] for cross_sec in cross_secs])

ratio = 0.25

path = ('../optimization/second_sdEta_mjj_optimization/lumi_and_kin_plots/'
              + 'four_cuts_lum3000/Output/HTML/MadAnalysis5job_0/index.html')

signal, _, bg, __ = opt.sig_and_bg_from_html(path)
signals = signal * scalings
sigs = signals / np.sqrt(signals + bg + (bg * ratio)**2)

print(np.transpose(sigs))

poly_result_1MeV = op.curve_fit(poly, lambdas, sigs[0])
poly_result_1GeV = op.curve_fit(poly, lambdas, sigs[1])
poly_result_100GeV = op.curve_fit(poly, lambdas, sigs[2])

results = [poly_result_1MeV, poly_result_1GeV, poly_result_100GeV]
return_lines = []
for result in results:
    params = result[0]
    return_line = 'return ({} + ({}) * L**-1 + ({}) * L**-2 + ({}) * L**-3 + ({}) * L**-4)'.format(*params)
    return_lines.append(return_line)

for return_line in return_lines:
    print(return_line)

#print(sigs.shape)
#print(sigs)

#exp_result = op.curve_fit(exp, lambdas, sigs[0])
#poly_result = op.curve_fit(poly, lambdas, sigs)
#poly2_result = op.curve_fit(poly2, lambdas, sigs)

#poly_result_1MeV = op.curve_fit(poly, lambdas, sigs[0])
#poly_result_1GeV = op.curve_fit(poly, lambdas, sigs[1])
#poly_result_100GeV = op.curve_fit(poly, lambdas, sigs[2])

#poly_result_1MeV = op.curve_fit(poly, lambdas, signals[0])
#poly_result_1GeV = op.curve_fit(poly, lambdas, signals[1])
#poly_result_100GeV = op.curve_fit(poly, lambdas, signals[2])
#
#print(signals)
#print(bg)
#print(poly_result_1MeV[0])
#print(poly_result_1GeV[0])
#print(poly_result_100GeV[0])

#poly_fits = np.array([
#        [poly(l, poly_result[0][0], poly_result[0][1], poly_result[0][2],
#              poly_result[0][3], poly_result[0][4]) for l in lambdas]
#         for poly_result in [poly_result_1MeV, poly_result_1GeV,
#                             poly_result_100GeV]])
#
#r_sq = [1 - (np.sum((sig - fit)**2)) / (np.sum((sig - np.mean(sig))**2))
#        for sig, fit in zip(signals, poly_fits)]
#
#print(r_sq)

#plt.plot(lambdas, poly_fits[0], label='Fit 1 MeV')
#plt.plot(lambdas, signals[0], label='Real 1 MeV')
#plt.legend()

#
#exp_fit = [exp(l, exp_result[0][0], exp_result[0][1]) for l in lambdas]
#poly_fit = [poly(l, poly_result[0][0], poly_result[0][1], poly_result[0][2],
#                  poly_result[0][3], poly_result[0][4]) for l in lambdas]
#poly2_fit = [poly2(l, poly2_result[0][0], poly2_result[0][1]) for l in lambdas]
#
##print(exp_result[1])
##print(poly_result[1])
##print(poly2_result[1])
#
#plt.plot(lambdas, exp_fit, label='exp')
#plt.plot(lambdas, poly_fit, label='poly')
#plt.plot(lambdas, poly2_fit, label='poly2')
#plt.plot(lambdas, sigs, label='real')
#plt.legend()
#fig = plt.gcf()
#fig.set_size_inches(12, 8)
#
#r_sq = [1 - (np.sum((sigs - fit)**2))/(np.sum((sigs - np.mean(sigs))**2))
#        for fit in [exp_fit, poly_fit, poly2_fit]]
#
#print(r_sq)

#xs = lambdas
#y1 = [axion_f1_signal(x) / np.sqrt(axion_f1_signal(x) + bg + (0.25 * bg)**2)
#      for x in xs]
#y2 = [axion_f1(x) for x in xs]
#plt.plot(xs, y1)
#plt.plot(xs, y2)
#print(y1)
#print(y2)