import numpy as np
from consts import WIDTH, HEIGHT

class Model():
    def __init__(self, rule: np.uint8):
        self.create_grid()
        self.line_num = 0
        self.rule = np.unpackbits(np.array([rule], dtype= np.uint8))[::-1]
        print(self.rule)
        self.randomize_line()

    def create_grid(self):
        self.grid = np.zeros((WIDTH,HEIGHT), dtype= bool)

    def randomize_line(self):
        # line = self.get_line()
        self.set_line(np.random.choice([False, True], WIDTH))
        self.line_num += 1

    def get_previous_line(self):
        return self.grid[self.line_num-1].copy()

    def set_line(self, new_line):
        self.grid[self.line_num] = new_line

    def step(self):
        neighborhood_types = self.get_neighborhood_type_array()
        line = self.get_previous_line()
        for i , _ in np.ndenumerate(line):
            line[i] = bool(self.rule[neighborhood_types[i]])
        self.set_line(line)
        self.line_num = (self.line_num + 1) % HEIGHT

    def get_neighborhood_type_array(self):
        line = self.get_previous_line().astype(int)
        R = np.roll(line, -1)
        L = np.roll(line, 1)

        return 4*L + 2*line + R
