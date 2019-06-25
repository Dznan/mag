import numpy as np
import mag


params = {
    'gamma': 8.681e6,
    'eta': 0.01,
    'HE': np.array([50e-6, 50e-6, 0.]),
    'gamma_D': 1/3,
    'dt': 1e-2,
    'max_iteration': 500,
    'eps': 1e-4,
    'warm_start': False
}

num_of_cell = 1
cparams = {
    'position': np.array([0, 0, 0]),
    'num_of_particle': 2,
    'radius': 126e-12
}

cells = [mag.Cell(**cparams) for _ in range(num_of_cell)]

mag.magnetic_simulation(cells, **params)

mag.plot_3D_cell(cells)