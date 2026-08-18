import matplotlib.pyplot as plt
import numpy as np
from model import Model
from consts import HEIGHT, WIDTH

FRAME_DELAY = 0.1

class Front:
    def __init__(self, model: Model):
        self.model = model
        self.define_grid()

    def define_grid(self):
        fig, ax = plt.subplots(figsize=(6, 6))

        self.image = ax.imshow(self.model.grid, cmap='Blues', vmin=0, vmax=1)

        # Add lines between cells (grid grid lines sit at half-step boundaries)
        ax.set_xticks(np.arange(-0.5, WIDTH, 1))
        ax.set_yticks(np.arange(-0.5, HEIGHT, 1))
        ax.grid(color='black', linestyle='-', linewidth=1)

        # Remove number labels on axes for a clean board look
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        # Overlay Agent marker on top
        # ax.legend(loc='upper right')
        plt.title("2D Matrix Board")
        plt.ion()
        plt.show()

        fig.canvas.mpl_connect('close_event', self.handle_close)
        self.is_open = True

    def step(self):
        self.image.set_data(self.model.grid)
        plt.pause(FRAME_DELAY)

    def show(self):
        plt.ioff()
        plt.show()

    def handle_close(self, event):
        self.is_open = False