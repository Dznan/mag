from .cell import Cell
import numpy as np
from scipy.optimize import fsolve


def integration_equation(m, mi, gamma, dt, alpha, H):
    coeff = gamma * dt / (2 * (1 + alpha ** 2))
    res = m + coeff * np.cross(m, H) - mi + coeff * np.cross(mi, H)
    return res


def magnetic_simulation(cells, gamma_D=1/3, max_iteration=50, eps=1e-4):
    iteration = 0
    error = 1e8

    # compute Dij
    D = []
    for i in range(len(cells)):
        Dij = []
        for j in range(len(cells)):
            if i == j:
                continue
            rij = cells[i].position - cells[j].position
            rij = np.reshape(rij, (-1, 1))
            rn = np.linalg.norm(rij)
            Dij.append(1 / (4 * np.pi * rn ** 3) * (np.eye(3) - 3 / (rn ** 2) * (np.dot(rij, rij.T))))
        D.append(Dij)

    H = []
    while error > eps or iteration < max_iteration:
        # traversal of all the magnetic moments
        for i, cell in enumerate(cells):
            HE = 0.
            HK = 0.
    
            # compute Hexo_D
            Hexo_D = 0.
            for j, _cell in enumerate(cells):
                Hexo_D += np.dot(D[i][j], _cell.mu)
            
            # compute Hendo_D
            Hendo_D = - gamma_D * cell.M

            # compute Heff
            Heff = HE + Hexo_D + Hendo_D + HK

            for particle in cell.particles:
                # integrate m
                m = fsolve(integration_equation, x0=np.array([0.0, 0.0, 0.0]))

        # compute error
        iteration += 1
