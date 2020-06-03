import random
from bankcomm.util import bounds_to_list
from collections import namedtuple


class RandomSeed:

    def __init__(self, num=0):
        self.random = random.seed(num)
        self.Point = namedtuple('Point', 'x y')

    # Point = namedtuple('Point', 'x y')

    def random_int(self, int_num):
        random_int = self.random.randint(0, int_num)
        return random_int

    def rect_random_point(self, bounds):
        bounds_list = bounds_to_list(bounds)
        if bounds_list:
            x0 = bounds_list[0]
            y0 = bounds_list[1]
            x1 = bounds_list[2]
            y1 = bounds_list[3]
            x = self.random.randint(x0, x1)
            y = self.random.randint(y0, y1)
            point = self.Point(x, y)
        else:
            point = None
        return point

    def rect_center_point(self, bounds):
        bounds_list = bounds_to_list(bounds)
        if bounds_list:
            x0 = bounds_list[0]
            y0 = bounds_list[1]
            x1 = bounds_list[2]
            y1 = bounds_list[3]
            point = self.Point(x0 + int((x1 - x0)/2), y0 + int((y1-y0)/2))
        else:
            point = None
        return point

    def slide_points(self, bounds):
        bounds_list = bounds_to_list(bounds)
        if bounds_list:
            x0 = bounds_list[0]
            y0 = bounds_list[1]
            x1 = bounds_list[2]
            y1 = bounds_list[3]
            origin_point = self.Point(x0 + int((x1 - x0)/2), y1)
            target_point = self.Point(x0 + int((x1 - x0)/2), y0)
            points = [origin_point, target_point]
        else:
            points = []
        return points


if '__main__' == __name__:
    rm = RandomSeed().rect_center_point('[22,234]')
    print(rm)