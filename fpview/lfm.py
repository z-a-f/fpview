
import numpy as np

from .map import Map
from .imgtools import ImgTools

class LowFlowMap(Map,ImgTools):
    """
    Manipulate the 'Low Flow Map' file

    The Low-Flow Map represents areas in the image having non-determinable 
        ridge flow. Ridge flow is determined using a set of discrete cosine wave 
        forms computed for a predetermined range of frequencies. These wave 
        forms are applied at 16 incremental orientations. At times none of the 
        wave forms at none of the orientations resonate sufficiently high within
        the region in the image to satisfactorily determine a dominant 
        directional frequency. This is a bi-level map with same dimension as the
        Direction Map. Cell values of 1 represent 8x8 pixel neighborhoods in the
        fingerprint image that are located within a region where a dominant 
        directional frequency could not be determined, otherwise cell values are
        set to 0. The Direction Map also records cells with nondeterminable 
        ridge flow. The difference is that the Low-Flow Map records all cells 
        with nondeterminable ridge flow, while the Direction Map records only 
        those that remain non-determinable after extensive interpolation and 
        smoothing of neighboring ridge flow directions.

    """

    def __init__(self, name, bg = [0,0,0,0], fg = [1,1,1,1], box = 8):
        self.bg = bg
        self.fg = fg
        self.__box_size = box
        self.load(name)

    def create(self):
        """Create a Low-Flow Map usable for plotting
        """
        self.create_from_f(self.create_block)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from os import sys, path
    test_dir = path.dirname(path.abspath(__file__))+'/tests/'

    fig, ax = plt.subplots(1,2)

    for a in ax:
        a.set_frame_on(False)
        a.set_axis_off()

    lfm0 = LowFlowMap(test_dir+'test.lfm', 0)
    lfm1 = LowFlowMap(lfm0.raw_data, 1)

    lfm0.create()
    lfm1.create()

    lfm0.plot(ax[0], alpha=.9)
    lfm1.plot(ax[1])
    # plt.axis('off')
    plt.show()




