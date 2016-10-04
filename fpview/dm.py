# TODO: DOCUMENTATION

import numpy as np

from .map import Map
from .imgtools import ImgTools

class DirectionMap(Map,ImgTools):
    """Manipulate the 'Direction Map'.

    The Direction Map represents the direction of ridge flow within the 
    fingerprint image. The map contains a grid of integer directions, where 
    each cell in the grid represents an 8x8 pixel neighborhood in the image. 
    Ridge flow angles are quantized into 16 integer bi-directional units equally
    spaced on a semicircle. Starting with vertical direction 0, direction units
    increase clockwise and represent incremental jumps of 11.25 degrees,
    stopping at direction 15 which is 11.25 degrees shy of vertical. Using this
    scheme, direction 8 is horizontal. A value of -1 in this map represents a
    neighborhood where no valid ridge flow was determined.

    Usage:
        DirectionMap(name, [bg], [fg], [box])

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
        """Create a Direction Map usable for plotting"""
        self.create_from_f(self.create_line)
    
