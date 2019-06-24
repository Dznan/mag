from .cell import Cell
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


def plot_cell(cells):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for cell in cells:
        cir = Circle(xy=cell.position, radius=cell.radius, fill=None)
        ax.add_patch(cir)
        for particle in cells.particles:
            ax.quiver(particle.position[0], particle.position[1], particle.m[0], particle.m[1], length=0.1)
    ax.set_aspect(1)
    plt.show()
