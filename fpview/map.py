
import abc

import matplotlib.pyplot as plt

class Map(object):
    """
    This is an abstract class for all the map classes.

    The abstract methods are;
    	create -- Creates data for plotting. Can use `create_from_f()` declared in the ImgTools
    """
    __metaclass__ = abc.ABCMeta

    def __new__(cls, *args, **kwargs):
        """Factory method for base/subtype creation. Simply creates an
        (new-style class) object instance and sets a base property."""
        instance = object.__new__(cls)
        instance.bg = None
        instance.fg = None
        instance.img_data = None
        instance.raw_data = None
        instance.__box_size = 8
        return instance
    

    def help(self):
        """Help - just shows the `__doc__`"""
        return self.__doc__

    def get_box_size(self):
        """Getter for the __box_size"""
        return self.__box_size

    def set_box_size(self, num=8):
        """Setter for the __box_size.

        Args:
            num:
                New value for the `__box_size` (default=8)

        NOTE: 
            Resets `img_data`
        """
        self.__box_size = num
        self.img_data = None

    def load(self, name):
        """Loads '...Map' of the fingerprint ridges.

        Args:
            name: 
                Name of the file, filehandler, or variable to be loaded
        """
        self.raw_data = []
        if type(name) is str:
            with open(name, 'r') as f:
                for line in f:
                    self.raw_data.append(map(int, line.split()))
        elif type(name) is file:
            name.seek(0,0)
            for line in name:
                self.raw_data.append(map(int, line.split()))
        else:
            # It's not a file - must be loaded already
            self.raw_data = name

        self.img_data = None

    @abc.abstractmethod
    def create(self):
        """Create a ...Map usable for plotting"""
        pass

    def plot(self, ax = None, cmap='gray', *args, **kwargs):
        """Plot and create/attach axes

        Args:
            ax:
                Axes of a figure to be attached to. If `None`, a new 
                `matplotlib.pyplot.subplots()` is created (default=None)

        Returns:
            Axes of the plotted image

        NOTE:
            Any additional arguments passed to this function will be directly
            passed to the `ax.imshow()`
        """
        if ax is None:
            fig, ax = plt.subplots()
        ax.imshow(self.img_data,  *args, **kwargs)

        return ax

