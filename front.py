import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
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
        
        # 2. Create the Slider Axis & Widget
        ax_slider = plt.axes([0.18, 0.05, 0.6, 0.04])
        self.rule_slider = Slider(
            ax=ax_slider,
            label='SELECT INT:',
            valmin=0,
            valmax=255,
            valinit=110,
            valstep=1, 
            color='royalblue'
        )
        ax_button = plt.axes([0.85, 0.05, 0.1, 0.04])
        self.start_button = Button(ax_button, 'Start', color='lightgoldenrodyellow', hovercolor='0.975')
        self.start_button.on_clicked(self.start)
        plt.ion()
        plt.show()

        fig.canvas.mpl_connect('close_event', self.handle_close)
        self.is_open = True

    def get_rule(self):
        return int(self.rule_slider.val)

    def start(self, event):
        self.model.set_up(self.get_rule())

    def step(self):
        self.image.set_data(self.model.grid)
        plt.pause(FRAME_DELAY)

    def handle_close(self, event):
        self.is_open = False