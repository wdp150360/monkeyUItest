import random


class RandomSeed:

    def __init__(self):
        self.random = random.seed()

    def __init__(self, num):
        self.random.seed(num)


