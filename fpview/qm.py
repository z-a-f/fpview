
import numpy as np

from .map import Map
from .imgtools import ImgTools

class QualityMap(Map,ImgTools):
    """
    Manipulate the 'Quality Map'

    The Quality Map represents regions in the image having varying levels of
    quality. The maps above are combined heuristically to form 5 discrete levels
    of quality. This map has the same dimension as the Direction Map, with each
    value in the map representing an 8x8 pixel neighborhood in the fingerprint
    image. A cell value of 4 represents highest quality, while a cell value of 0
    represent lowest possible quality.

    Usage:
        LowFlowMap(name, [bg], [fg], [box], [qmax])

        name:   
            Name of the file to open, name of the file pointer, or name of the 
            variable with the loaded map
        bg:
            RGBA Background color to use (default=[0,0,0,0])
        fg: 
            RGBA Foreground color to use (default=[1,1,1,1])
        box:
            Box size (default=8)
        qmax:
            Maximum quality (default=4)

    Methods:
        create():
            Creates the `img_data` variable from the `raw_data`

    Internal variables:
        bg, fg:
            Background and foreground
        q_max:
            Maximum quality

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

    def __init__(self, name, bg = [0,0,0,0], fg = [1,1,1,1], box = 8, qmax = 4.):
        self.bg = bg
        self.fg = fg
        self.q_max = float(qmax)
        self.__box_size = box
        self.load(name)


    def create(self):
        """Create a High-Curvature Map usable for plotting"""
        self.create_from_f(self.create_block_gradient_alpha)
