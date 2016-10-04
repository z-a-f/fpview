
import numpy as np

from .map import Map
from .imgtools import ImgTools

class LowFlowMap(Map,ImgTools):
    """Manipulate the 'Low Flow Map' file

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

    Usage:
        LowFlowMap(name, [bg], [fg], [box])

        name:   
            Name of the file to open, name of the file pointer, or name of the 
            variable with the loaded map
        bg:
            RGBA Background color to use (default=[0,0,0,0])
        fg: 
            RGBA Foreground color to use (default=[1,1,1,1])
        box:
            Box size (default=8)

    Methods:
        create():
            Creates the `img_data` variable from the `raw_data`

    Internal variables:
        bg, fg:
            Background and foreground

    Inherited variables and methods:
        raw_data:   
            Initially loaded raw_data
        img_data:   
            Converted data
        load():
            Loads the file/variable (Called in the __init__)
        plot(ax):   
            Plots the current img_data and attaches it to `ax`. Returns `ax`
        set_box_size(num):
            Setter for the single block size (default=8)
        get_box_size():
            Getter for the single block size
    """

    def __init__(self, name, bg = None, fg = None, box = 8):
        if bg is None:
            bg = [0,0,0,0]
        if fg is None:
            fg = [1,1,1,1]
        self.bg = bg
        self.fg = fg
        self.__box_size = box
        self.load(name)

    def create(self):
        """Create a Low-Flow Map usable for plotting"""
        self.create_from_f(self.create_block)




