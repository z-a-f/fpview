#!/usr/bin/env python

from fpview import (DirectionMap, LowFlowMap, HighCurvatureMap, QualityMap)
# from fpview import (Map,ImgTools)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptch

from PIL import Image
from mpl_toolkits.axes_grid.anchored_artists import AnchoredDrawingArea


# Set the location of the test data
from os import sys, path
test_dir = path.dirname(path.abspath(__file__)) + '/fpview/tests/data/'

# Create a figure
fig, ax = plt.subplots(1,2)
# ax = plt.gca()
for axes in ax:
    axes.set_frame_on(False)
    axes.set_axis_off()


plt.hold(True)

# Show Direction Map
dm = DirectionMap(test_dir+'test.dm', fg = [0,0,0,1], bg = [1,1,1,1])
dm.create()
dm.plot(ax=ax[1])

# Highlight 'Low-Flow' regions as red
lfm = LowFlowMap(test_dir+'test.lfm', fg = [1,0,0,1])
lfm.create()
lfm.plot(ax=ax[1], alpha=.5)

# Highlight 'High-Curvature' regions as blue
hcm = HighCurvatureMap(test_dir+'test.hcm', fg = [0,0,1,1])
hcm.create()
hcm.plot(ax=ax[1], alpha=.5)

# Highlight the quality as green - the brighter, the higher
qm = QualityMap(test_dir+'test.qm', fg = [0,1,0,1])
qm.create()
qm.plot(ax=ax[1], alpha=.3)

# plt.hold(False)

# Show processed fingerprint:
processed_image = bytearray(open(test_dir+'test.brw', 'rb').read())
dim = (len(dm.raw_data)*8, len(dm.raw_data[0])*8)
# print dim[0]*dim[1], len(processed_image)
processed_image = np.reshape(processed_image, dim)
ax[0].imshow(processed_image, cmap='gray')

# Show minutia:
# minutia_color = (0,1,0,.8)
minutia_list = np.loadtxt(test_dir+'test.xyt')
for minutia in minutia_list:
    quality = minutia[3] / 100.
    minutia_color = (0, 1, 0, quality )
    # minutia_color = (1 - quality, quality, 0, .8)
    crcl = ptch.Circle((minutia[0], minutia[1]), radius = 3, axes = ax[0], edgecolor='none', facecolor = minutia_color)
    ax[0].add_patch(crcl)

    #arc = ptch.Arc((minutia[0], minutia[1]), angle = minutia[2], width = 0, height = 5, edgecolor=minutia_color)
    #ax[0].add_patch(arc)

# Show the plot
plt.show()
