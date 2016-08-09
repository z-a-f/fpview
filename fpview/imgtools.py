
import numpy as np
import math

class ImgTools():

    def create_from_f(self, f):
        """Create a Low-Flow Map usable for plotting
        """
        assert len(self.raw_data) > 0
        assert len(self.raw_data[0]) > 0
        self.img_data = []
        for row in self.raw_data:
            img = [f(x) for x in row]
            # print len(img), len(img[0])
            img = np.hstack(img)
            for r in img:
                self.img_data.append(r)
        self.img_data = np.array(self.img_data)

    def create_block(self, val):
        if val: return [[self.fg]*self.get_box_size() for _ in xrange(self.get_box_size())]
        else: return [[self.bg]*self.get_box_size() for _ in xrange(self.get_box_size())]
        # return self.__get_block(val)

    def create_block_gradient_alpha(self, val):
        color = self.fg[:]
        # self.q_max = float('inf')
        if type(color) is int or type(color) is float:
            color = [color]*4
        elif type(color) is list:
            while len(color) < 4:
                color = color + [0]
        color[3] = val*1. / self.q_max
        return [[color]*self.get_box_size() for _ in xrange(self.get_box_size())]


    def create_line(self, rot=0):
        """
        Create a line on a 8x8 grid

        Args:
            rot:    Rotation of the line. 0 represents vertical line (range 0-15)
            bg: Background value
        fg:     Foreground value

        Returns:
            8x8 np.array() with the line

        The rotation is in the increments of 11.25 degrees clockwise
        """
        if rot == -1:
            return [[self.bg]*self.get_box_size() for _ in xrange(self.get_box_size())]
            
        assert (0 <= rot <= 15)
        rot = rot*11.25

        # res = np.full((self.get_box_size(), self.get_box_size()), self.bg)
        res = [[self.bg]*self.get_box_size() for _ in xrange(self.get_box_size())]

        def bound_point(p):
            while p[0] < 0: p[0] += 1
            while p[0] >= self.get_box_size(): p[0] -= 1
            while p[1] < 0: p[1] += 1
            while p[1] >= self.get_box_size(): p[1] -= 1
            return p

        conv = lambda x: map(int, np.floor(x))
        
        ## The reason the indeces are extending to -2 and 10 is because the
        ## rotation is calculated as sin/cos, meaning, we need a long line to
        ## fill the diagonals
        if self.get_box_size() % 2 == 0:
            ## 4 different origins for rotation
            # First quadrant
            origin = [(self.get_box_size() - 1) / 2, (self.get_box_size() - 1) / 2]
            for idx in xrange(-2, origin[1] + 1):
                #for jdx in xrange(4):
                jdx = origin[1]
                point = self.rotate_point(origin, [idx, jdx], rot)
                point = conv(point)
                point = bound_point(point)
                res[point[0]][point[1]] = self.fg

            # Second quadrant
            origin[1] += 1
            for idx in xrange(-2, origin[1] + 1):
                jdx = origin[1]
                point = self.rotate_point(origin, [idx, jdx], rot)
                point = conv(point)
                point = bound_point(point)
                res[point[0]][point[1]] = self.fg

            # Third quadrant
            origin[0] += 1
            for idx in xrange(origin[1] + 1, self.get_box_size() + 2):
                jdx = origin[1]
                point = self.rotate_point(origin, [idx, jdx], rot)
                point = conv(point)
                point = bound_point(point)
                res[point[0]][point[1]] = self.fg

            # Fourth quadrant
            origin[1] -= 1
            for idx in xrange(origin[1] + 1, self.get_box_size() + 2):
                jdx = origin[1]
                point = self.rotate_point(origin, [idx, jdx], rot)
                point = conv(point)
                point = bound_point(point)
                res[point[0]][point[1]] = self.fg
        else:
            ## Single rotation origin
            origin = [self.get_box_size() / 2, self.get_box_size() / 2]
            for idx in xrange(self.get_box_size()):
                jdx = origin[1]
                point = self.rotate_point(origin, [idx, jdx], rot)
                point = conv(point)
                point = bound_point(point)
                res[point[0]][point[1]] = self.fg
        return res

    def rotate_point(self, center, point, angle):
        """
        Rotate point around center by angle

        Args:
            center: Center point
            point: Point to be rotated
        angle: Angle in radians to rotate by
        Returns:
            New coordinates for the point
        """
        angle = math.radians(angle)
        temp_point = point[0]-center[0] , point[1]-center[1]
        temp_point = ( -temp_point[0]*math.cos(angle)+temp_point[1]*math.sin(angle) , temp_point[0]*math.sin(angle)-temp_point[1]*math.cos(angle))
        temp_point = [temp_point[0]+center[0] , temp_point[1]+center[1]]
        return temp_point