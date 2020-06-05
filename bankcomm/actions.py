from bankcomm.random_num import RandomSeed
from bankcomm.config import seed
from macaca import WebElement


class Actions:

    def __init__(self, wd):
        self.wd = wd
        # self.random_seed = RandomSeed(seed)

    def touch_action(self, point):
        self.wd.touch('tap', {
            'x': point.x,
            'y': point.y
        })

    def slide_action(self, points):
        self.wd.touch('drag', {
            'fromX': points[0].x,
            'fromY': points[0].y,
            'toX': points[1].x,
            'toY': points[1].y,
            'step': 100
        })

    def alert_if_exist(self):
        pass
