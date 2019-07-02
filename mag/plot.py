from .cell import Cell
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.patches import Circle
import matplotlib.pyplot as plt



def plot_3D_cell(cells, scale=10, heff_change=0, show_dmdt=False, show_rg=False):
    for i in range(len(cells[0].particles[0]._cache['Heff'])):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        for cell in cells:
            # length=5e3*np.linalg.norm(cell.particles[0].position - cell.particles[0]._cache['Heff'][i])
            if heff_change == 0:
                heff_length = 1 * scale
            else:
                heff_length = heff_change * np.linalg.norm(cell.particles[0]._cache['Heff'][i])
            ax.quiver(
                cell.particles[0].position[0],
                cell.particles[0].position[1],
                cell.particles[0].position[2],
                cell.particles[0]._cache['Heff'][i][0],
                cell.particles[0]._cache['Heff'][i][1],
                cell.particles[0]._cache['Heff'][i][2],
                # length: presentation modify, 1 * scale before
                length=heff_length, normalize=True, color='k'
                # length=length, normalize=True, color='k'
            )
            for particle in cell.particles:
                # print track
                for j in range(1, i + 1):
                    ax.plot(
                        [particle.position[0] + particle._cache['m'][j-1][0] * scale, particle.position[0] + particle._cache['m'][j][0] * scale],
                        [particle.position[1] + particle._cache['m'][j-1][1] * scale, particle.position[1] + particle._cache['m'][j][1] * scale],
                        [particle.position[2] + particle._cache['m'][j-1][2] * scale, particle.position[2] + particle._cache['m'][j][2] * scale],
                        c='k', linestyle=':'
                    )

                dmdt = -np.cross(particle._cache['m'][i], particle._cache['H'][i])
                a1 = -np.cross(particle._cache['m'][i], particle._cache['Heff'][i])
                a2 = np.cross(particle._cache['m'][i], dmdt)

                ax.text(
                    particle.position[0] + particle._cache['m'][i][0] * scale * 1.1,
                    particle.position[1] + particle._cache['m'][i][1] * scale * 1.1,
                    particle.position[2] + particle._cache['m'][i][2] * scale * 1.1,
                    'M',
                    None,
                    color='b'
                )

                ax.quiver(
                    particle.position[0],
                    particle.position[1],
                    particle.position[2],
                    particle._cache['m'][i][0],
                    particle._cache['m'][i][1],
                    particle._cache['m'][i][2],
                    length=1 * scale, normalize=True, color='b'
                )
                if show_rg:
                    ax.quiver(
                        particle.position[0] + particle._cache['m'][i][0] * scale,
                        particle.position[1] + particle._cache['m'][i][1] * scale,
                        particle.position[2] + particle._cache['m'][i][2] * scale,
                        dmdt[0],
                        dmdt[1],
                        dmdt[2],
                        length=0.2 * scale, normalize=True, color='r'
                    )

                    ax.quiver(
                        particle.position[0] + particle._cache['m'][i][0] * scale,
                        particle.position[1] + particle._cache['m'][i][1] * scale,
                        particle.position[2] + particle._cache['m'][i][2] * scale,
                        a2[0],
                        a2[1],
                        a2[2],
                        length=0.2 * scale, normalize=True, color='g'
                    )
                if show_dmdt:
                    ax.quiver(
                        particle.position[0] + particle._cache['m'][i][0] * scale,
                        particle.position[1] + particle._cache['m'][i][1] * scale,
                        particle.position[2] + particle._cache['m'][i][2] * scale,
                        dmdt[0],
                        dmdt[1],
                        dmdt[2],
                        #0.2 * scale
                        length=10e2 * np.linalg.norm(dmdt), normalize=True, color='r'
                    )
        # ax.set_aspect(1)
        ax.set_xlim3d([-scale, scale])
        ax.set_ylim3d([-scale, scale])
        ax.set_zlim3d([-scale, scale])
        plt.savefig('picture/%03d.png' % i)
        plt.close()