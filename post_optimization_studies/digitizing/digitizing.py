#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:12:22 2020

@author: elijahsheridan
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def read_and_save_image(image, save_file):
    im = Image.open(image, 'r')
    width, height = im.size
    print(width, height)
    pix_list_1d = list(im.getdata())
    pix_array = np.array(
            [[pix_list_1d[x + width * y] for x in range(width)]
            for y in range(height)])

#    pix_array = []
#    for y in range(height):
#        temp = []
#        for x in range(width):
#            temp.append(pixel_values[x + width * y])
#        pix_array.append(temp)
#    pix_array = np.array(pix_array)

    np.save(save_file, pix_array)

#read_and_save_image('big_image.png', 'big_image.npy')
#read_and_save_image('small_image.png', 'small_image.npy')

def index_to_val(index, min_val, max_val, num_indices, y=False):
    if y:
        return min_val + ((max_val - min_val)/num_indices) * (
                num_indices - index - 1)
    else:
        return min_val + ((max_val - min_val)/num_indices) * index


def val_to_index(val, min_val, max_val, num_indices, y=False):
    index = int((val - min_val) * num_indices/(max_val - min_val))
    if y:
        return (num_indices - 1) - index
    else:
        return index



m, L = [row for row in np.load('contour_data.npy')]
m, L = [m, -np.log10(L)]
i, f = np.searchsorted(m, [-2, 3])
m, L = [np.append(m[i:f],[3.4]), np.append(L[i:f], [L[-1]])]




# NUMBER 1
#new_region = [[[1., 1., 1., 1.] if i_index <= j <= f_index and  else [0.,0.,0.,0.,] ]]

pix_vals = np.load('big_image.npy')
w, h = list((7/pix_vals.shape[0]) * np.array(pix_vals.shape[:2]))
bounds = [10**-15, 10**4, 3.00 * 10**-10, 2.73 * 10**3]
extent = [np.log10(b) for b in bounds]
plt.imshow(pix_vals, extent=extent, aspect='auto')

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
new_region = [
        [[178/255, 34/255, 34/255, 1.]
        if j in cols and (i < bots[np.where(cols==j)[0][0]])
        and np.sum(pix_vals[i,j,:3]**2) > 3*250**2
        else [1.,1.,1.,0.]
        for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]
plt.imshow(new_region, extent=extent, aspect='auto')

#plt.plot(m, L, linewidth=1.5, color='firebrick')

fig = plt.gcf()
fig.set_size_inches(w, h)
plt.xlabel(r'$m_a$ [Log$_{10}$ GeV]')
plt.ylabel(r'$1/\Lambda$ [Log$_{10}$ TeV$^{-1}$]')
plt.savefig('big_final', dpi=500, bbox_inches='tight')

plt.clf()

# NUMBER 2

pix_vals = np.load('small_image.npy')
w, h = list((7/pix_vals.shape[0]) * np.array(pix_vals.shape[:2]))
bounds = [0.00032480888972387324, 10048.799127736118, 0.00867122579786319,
          2732.3259558424825]
extent = [np.log10(b) for b in bounds]
plt.imshow(pix_vals, extent=extent, aspect='auto')

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
new_region = [
        [[178/255, 34/255, 34/255, 1.]
        if j in cols and (i < bots[np.where(cols==j)[0][0]])
        and np.sum(pix_vals[i,j,:3]**2) > 3*250**2
        else [1.,1.,1.,0.]
        for j in range(len(pix_vals[0]))] for i in range(len(pix_vals))]
plt.imshow(new_region, extent=extent, aspect='auto')

#plt.plot(m, L, linewidth=3, color='firebrick')
fig = plt.gcf()
fig.set_size_inches(w, h)
plt.xlabel(r'$m_a$ [Log$_{10}$ GeV]')
plt.ylabel(r'$1/\Lambda$ [Log$_{10}$ TeV$^{-1}$]')
plt.savefig('small_final', dpi=500, bbox_inches='tight')

