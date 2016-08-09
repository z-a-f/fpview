#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from fpview import (DirectionMap, LowFlowMap, HighCurvatureMap, QualityMap)
from fpview import (Map,ImgTools)


from os import sys, path
test_dir = path.dirname(path.abspath(__file__))+'/fpview/tests/'

# tt = ImgTools()
# tt.fg = [1,0,0,1]
# tt.bg = [0,0,0,0]
# tt.q_max = 4
# tt.get_box_size = lambda: 8

# print tt.create_block(1)
# print tt.create_block_gradient_alpha(3)

dm = DirectionMap(test_dir+'test.dm', fg = [0,0,0,1], bg = [1,1,1,1])
lfm = LowFlowMap(test_dir+'test.lfm', fg = [1,0,0,1])
hcm = HighCurvatureMap(test_dir+'test.hcm', fg = [0,0,1,1])
qm = QualityMap(test_dir+'test.qm', fg = [0,1,0,1])

dm.create()
lfm.create()
hcm.create()
qm.create()

fig = plt.figure()
ax = plt.gca()

ax.set_frame_on(False)
ax.set_axis_off()

plt.hold(True)
dm.plot(ax=ax)
lfm.plot(ax=ax, alpha=.5)
hcm.plot(ax=ax, alpha=.5)
qm.plot(ax=ax, alpha=.3)

plt.show()
