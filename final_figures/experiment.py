#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:57:32 2020

@author: elijahsheridan
"""

settings = {'axes.labelsize': 32,
            'xtick.major.size': 10,
            'xtick.major.width': 1.5,
            'xtick.labelsize': 24,
            'ytick.major.size': 10,
            'ytick.major.width': 1.5,
            'ytick.labelsize': 24,
            'legend.fontsize': 24,
            'figure.figsize': (15, 10)}

m, L = [row for row in np.load('FIG13_contour_data.npy')]
m, L = [m, -np.log10(L)]
i, f = np.searchsorted(m, [-2, 3])
m, L = [np.append(m[i:f],[3.4]), np.append(L[i:f], [L[-1]])]

pix_vals = np.load('FIG13_small_image.npy')
w, h = list((7/pix_vals.shape[0]) * np.array(pix_vals.shape[:2]))
bounds = [0.00032480888972387324, 10048.799127736118, 0.00867122579786319,
          2732.3259558424825]
extent = [np.log10(b) for b in bounds]

with plt.rc_context(settings):
    plt.imshow(pix_vals, extent=extent, aspect='auto')

if gen:
    # min and max x-axis indices (mass indices) for our region
    imindex, fmindex = [val_to_index(m[0], extent[0], extent[1], len(pix_vals[0])),
                        val_to_index(m[-1], extent[0], extent[1], len(pix_vals[0]))]
    # set of all columns between min and max
    cols = np.linspace(imindex, fmindex, fmindex - imindex + 1)
    # indices in "m" associated with each column
    m_indices = np.searchsorted(
            m, [index_to_val(col, extent[0], extent[1], len(pix_vals[0]))
            for col in cols])
    # lowest row to shade for each relevant column
    bots = [val_to_index(L[m_index], extent[2], extent[3], len(pix_vals), True)
            for m_index in m_indices]
    # white, except for col indices in cols and above the line
    # [178/255, 34/255, 34/255, 1]
    #
#    new_region = [
#            [[178/255, 34/255, 34/255, 1]
#            if j in cols and (i < bots[np.where(cols==j)[0][0]])
#            and np.sum(pix_vals[i,j,:3]**2) > 3*240**2
#            else [1.,1.,1.,0.]
#            for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]
    new_region = [
            [[0,0,0,0.25]
            if j in cols and (i < bots[np.where(cols==j)[0][0]])
            else [1.,1.,1.,0.]
            for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]

    np.save('FIG13_shade_region', new_region)
else:
    new_region = np.load('FIG13_shade_region.npy')



with plt.rc_context(settings):
    plt.imshow(new_region, extent=extent, aspect='auto')

    #plt.plot(m, L, linewidth=3, color='firebrick')
    fig = plt.gcf()
    fig.set_size_inches(w*(12/7), h*(12/7))
    plt.xlabel(r'$m_a$ [Log$_{10}$ GeV]')
    plt.ylabel(r'$1/\Lambda$ [Log$_{10}$ TeV$^{-1}$]')
    plt.savefig('FIG13_subset_parameter_space_hashed', dpi=500, bbox_inches='tight')