#!/usr/bin/env python

from fpview import (DirectionMap, LowFlowMap, HighCurvatureMap, QualityMap)
# from fpview import (Map,ImgTools)

import numpy as np
import matplotlib.pyplot as plt

# Set the location of the test data
from os import sys, path
test_dir = path.dirname(path.abspath(__file__)) + '/fpview/tests/data/'

# Create a figure
fig = plt.figure()
ax = plt.gca()
ax.set_frame_on(False)
ax.set_axis_off()
plt.hold(True)

# Show Direction Map
dm = DirectionMap(test_dir+'test.dm', fg = [0,0,0,1], bg = [1,1,1,1])
dm.create()
dm.plot(ax=ax)

# Highlight 'Low-Flow' regions as red
lfm = LowFlowMap(test_dir+'test.lfm', fg = [1,0,0,1])
lfm.create()
lfm.plot(ax=ax, alpha=.5)

# Highlight 'High-Curvature' regions as blue
hcm = HighCurvatureMap(test_dir+'test.hcm', fg = [0,0,1,1])
hcm.create()
hcm.plot(ax=ax, alpha=.5)

# Highlight the quality as green - the brighter, the higher
qm = QualityMap(test_dir+'test.qm', fg = [0,1,0,1])
qm.create()
qm.plot(ax=ax, alpha=.3)

# Show the plot
plt.show()
