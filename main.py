import numpy as np
import mag


params = {
    'gamma': 8.681e6,
    'eta': 0.01,
    'HE': np.array([50e-6, 50e-6, 0.]),
    'gamma_D': 1/3,
    'dt': 1e-2,
    'max_iteration': 50,
    'eps': 1e-4,
    'warm_start': False
}

# ferromagnet
num_of_fe_cell = 2
cparams_fe = {
    'Ms': 8e-5,
    'num_of_particle': 2,
    'radius': 126e-8
}

# permanent magnet
num_of_pe_cell = 1
cparams_pe = {
    'position': np.array([0, 0, 0]),
    'Ms': 8e3,
    'num_of_particle': 2,
    'radius': 126e-4,
    # m在cell中会进行规范化
    'm': np.array([-1., 1., 0])
}

cells = [mag.Cell(position=np.random.randn(3) * 5, **cparams_fe) for _ in range(num_of_fe_cell)]
cells += [mag.Cell(**cparams_pe) for _ in range(num_of_pe_cell)]

mag.magnetic_simulation(cells, **params)

print()
s = input('Save pictures? (y/n) ')
if s == 'y':
    mag.plot_3D_cell(cells, scale=10)