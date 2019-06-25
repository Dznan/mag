from .cell import Cell
import numpy as np
from scipy.optimize import fsolve


def integration_equation(m, mi, gamma, dt, alpha, H):
    coeff = gamma * dt / (2 * (1 + alpha ** 2))
    # print(coeff)
    # print(coeff, np.cross(m, H))
    res = m + coeff * np.cross(m, H) - mi + coeff * np.cross(mi, H)
    return res


def magnetic_simulation(cells, gamma, eta, gamma_D=1/3, dt=1e-4, max_iteration=500, eps=1e-4, warm_start=False):
    iteration = 0
    error = 1e8

    # compute Dij
    D = []
    for i in range(len(cells)):
        Dij = []
        for j in range(len(cells)):
            if i == j:
                Dij.append(None)
                continue
            rij = cells[i].position - cells[j].position
            rij = np.reshape(rij, (-1, 1))
            rn = np.linalg.norm(rij)
            Dij.append(1 / (4 * np.pi * rn ** 3) * (np.eye(3) - 3 / (rn ** 2) * (np.dot(rij, rij.T))))
        D.append(Dij)

    while error > eps and iteration < max_iteration:
        print(error, iteration)
        error = 0.0
        # traversal of all the magnetic moments
        for i, cell in enumerate(cells):
            # TODO: compute HE and HK
            HE, HK = np.array([50e-6, 50e-6, 0]), 0.

            # compute Hexo_D
            Hexo_D = 0.
            for j, _cell in enumerate(cells):
                if D[i][j] is None:
                    continue
                Hexo_D += np.dot(D[i][j], _cell.mu)

            # compute Hendo_D
            Hendo_D = - gamma_D * cell.M

            # compute Heff
            Heff = HE + Hexo_D + Hendo_D + HK
            # Heff = HE
            print('H', Heff)

            for particle in cell.particles:
                H = particle._cache['H']
                m = particle._cache['m']

                # integrate m
                alpha = gamma * eta * particle.Ms

                # First step of m
                if iteration == 0 and not warm_start:
                    H.clear()
                    m.clear()
                    m.append(particle.m)
                    H.append(Heff + alpha * np.cross(m[0], Heff))
                    grad_m = -gamma / (1 + alpha ** 2) * (np.cross(m[0], H[0]))
                    half_m = m[0] + 0.5 * dt * grad_m
                    half_H = Heff + alpha * np.cross(half_m, Heff)
                    grad_half_m = -gamma / (1 + alpha ** 2) * (np.cross(half_m, half_H))
                    m.append(m[0] + dt * grad_half_m)
                else:
                    # update H^(i+1)
                    H.append(Heff + alpha * np.cross(particle.m, Heff))

                    # compute H^(i+1/2)
                    # TODO: calculate H^0 and H^(1/2)
                    H_ = 3/2 * H[-1] - 1/2 * H[-2]
                    m.append(
                        fsolve(
                            integration_equation,
                            x0=np.array([0.0, 0.0, 0.0]),
                            args=(particle.m, gamma, dt, alpha, H_)
                        )
                    )         

                    # update M
                    particle.M = m[-1] * particle.Ms

                print('m', m[-1])

                # compute error
                h = Heff / np.linalg.norm(Heff)
                error += np.linalg.norm(np.cross(m[-1], h))

        iteration += 1