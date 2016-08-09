
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
    """

    def __init__(self, name, bg = [0,0,0,0], fg = [1,1,1,1], box = 8):
        self.bg = bg
        self.fg = fg
        self.__box_size = box
        self.load(name)

    def create(self):
        """Create a High-Curvature Map usable for plotting
        """
        self.create_from_f(self.create_block)
