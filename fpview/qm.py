
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
    """

    def __init__(self, name, bg = [0,0,0,0], fg = [1,1,1,1], box = 8, qmax = 4.):
        self.bg = bg
        self.fg = fg
        self.q_max = float(qmax)
        self.__box_size = box
        self.load(name)


    def create(self):
        """Create a High-Curvature Map usable for plotting
        """
        self.create_from_f(self.create_block_gradient_alpha)
