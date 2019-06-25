from .cell import Cell
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


# def plot_cell(cells, filename):
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     for cell in cells:
#         cir = Circle(xy=cell.position, radius=cell.radius, fill=None)
#         ax.add_patch(cir)
#         for particle in cell.particles:
#             ax.quiver(particle.position[0], particle.position[1], particle.m[0], particle.m[1])
#     ax.set_aspect(1)
#     plt.savefig('{}.png'.format(filename))
#     plt.close()


def plot_cell(cells):
    for i in range(len(cells[0].particles[0]._cache['m'])):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for cell in cells:
            cir = Circle(xy=cell.position, radius=cell.radius, fill=None)
            ax.add_patch(cir)
            for particle in cell.particles:
                ax.quiver(particle.position[0], particle.position[1], particle._cache['m'][i][0], particle._cache['m'][i][1])
        ax.set_aspect(1)
        plt.savefig('picture/{}.png'.format(i))
        plt.close()


def plot_3D_cell(cells):
    for i in range(len(cells[0].particles[0]._cache['m'])):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for cell in cells:
            for particle in cell.particles:
                ax.quiver(
                    particle.position[0],
                    particle.position[1],
                    particle.position[2],
                    particle._cache['m'][i][0],
                    particle._cache['m'][i][1],
                    particle._cache['m'][i][2],
                    length=1, normalize=True
                )
        # ax.set_aspect(1)
        ax.set_xlim3d([-1, 1])
        ax.set_ylim3d([-1, 1])
        ax.set_zlim3d([-1, 1])
        plt.savefig('picture/{}.png'.format(i))
        plt.close()