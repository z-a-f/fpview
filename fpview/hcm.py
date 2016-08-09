
import numpy as np

from .map import Map
from .imgtools import ImgTools

class HighCurvatureMap(Map,ImgTools):
    """
    Manipulate the 'High-Curvature Map'

    The High-Curvature Map represents areas in the image having high-curvature
    ridge flow. This is especially true of core and delta regions in the
    fingerprint image, but high-curvature is not limited to just these cases. 
    This is a bi-level map with same dimension as the Direction Map. Cell values
    of 1 represent 8x8 pixel neighborhoods in the fingerprint image that are
    located within a high-curvature region, otherwise cell values are set to 0.

    Usage:
        HighCurvatureMap(name, [bg], [fg], [box])

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

    def __init__(self, name, bg = [0,0,0,0], fg = [1,1,1,1], box = 8):
        self.bg = bg
        self.fg = fg
        self.__box_size = box
        self.load(name)

    def create(self):
        """Create a High-Curvature Map usable for plotting"""
        self.create_from_f(self.create_block)
