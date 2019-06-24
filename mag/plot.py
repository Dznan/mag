from .cell import Cell
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def plot_cell(cells):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for cell in cells:
        cir = Circle(xy=cell.position, radius=cell.radius, fill=None)
        ax.add_patch(cir)
    ax.set_aspect(1)
    plt.show()
