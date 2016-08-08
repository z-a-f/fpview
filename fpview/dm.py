# TODO: DOCUMENTATION

import numpy as np

from .map import Map
from .imgtools import ImgTools

class DirectionMap(Map,ImgTools):
    """
    Manipulate the 'Direction Map'.

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
        DirectionMap(name, bg)

        name:   Name of the .dm file to open, name of the file pointer, or name of the variable with the loaded map
        bg:     Background color to use (default=0). Note that the foreground is computed as `fg = 1 - bg`

    Internal variables:
        raw_data:   Initially loaded raw_data
        img_data:   Converted data
        bg, fg:     Background and foreground

    Getters and setters:
        get_box_size:   Returns the line box size
        set_box_size:   Sets the line box size

    Methods:
        create()
            Converts the loaded direction map to the image format
        plot(ax)
            Plots the current img_data and attaches it to `ax`. Returns `ax`

    """
    def __init__(self, name, bg = 0, box = 8):
        
        # self.raw_data, self.img_data = self.load(name, bg)
        self.bg = bg
        self.fg = 1 - self.bg
        self.load(name)

        self.__box_size = box

    def create(self):
        """
        Create a Direction Map usable for plotting 
        """
        assert len(self.raw_data) > 0
        assert len(self.raw_data[0]) > 0
        self.img_data = []
        for row in self.raw_data:
            line = [self.create_line(x) for x in row]
            line = np.hstack(line)
            for row in line:
                self.img_data.append(row)
        self.img_data = np.array(self.img_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    from os import sys, path
    test_dir = path.dirname(path.abspath(__file__))+'/tests/'

    fig, ax = plt.subplots(1,2)

    for a in ax:
        a.set_frame_on(False)
        a.set_axis_off()

    dm0 = DirectionMap(test_dir+'test.dm', 0)
    dm1 = DirectionMap(dm0.raw_data, 1)

    dm0.create()
    dm1.create()

    dm0.plot(ax[0])
    dm1.plot(ax[1])
    # plt.axis('off')
    plt.show()
    
