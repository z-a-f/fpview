
import abc

import matplotlib.pyplot as plt

class Map(object):
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
        return self.__doc__

    def get_box_size(self):
        return self.__box_size

    def set_box_size(self, num):
        self.__box_size = num
        self.img_data = None

    def load(self, name):
        """Load '... Map' of the fingerprint ridges.

        Args:
            name: Name of the file, filehandler, or variable to be loaded
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
        """
        Create a Direction Map usable for plotting 
        """
        pass

    def plot(self, ax = None, *args, **kwargs):
        """
        Plot and create/attach axes
        """

        if ax is None:
            fig, ax = plt.subplots()
        ax.imshow(self.img_data, cmap='gray', *args, **kwargs)

        return ax

