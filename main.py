import numpy as np
import mag
import sys

# Different parameters of experiment from 1 to 4.
heff_change, show_dmdt, show_rg = 0, False, False
params_HE = np.array([0., 0., 50e-6])
params_gamma_D = 1 / 3
params_dt = 1e-2
num_of_fe_cell = 2
fe_num_of_particle = 2
fe_active, ea_active = True, False

if len(sys.argv) >= 2:
    if sys.argv[1][1:] == '1':
        show_rg = True
        params_gamma_D = 0
        params_dt = 5e-3
        num_of_fe_cell = 1
        fe_num_of_particle = 1
    elif sys.argv[1][1:] == '2':
        fe_active, ea_active = False, True
        heff_change, show_dmdt = 5e3, True
        params_HE = np.array([0., 0., 0.])
        params_gamma_D = 0
        params_dt = 5e-5
    elif sys.argv[1][1:] == '3':
        if len(sys.argv) >= 3:
            if sys.argv[2][1:] == '2':
                num_of_fe_cell = 2
            elif sys.argv[2][1:] == '4':
                num_of_fe_cell = 4
            else:
                print('Undefined instruction:', sys.argv[1], sys.argv[2])
                exit(1)
    elif sys.argv[1][1:] == '4':
        heff_change = 5e5
        num_of_fe_cell = 1
        if len(sys.argv) >= 3:
            if sys.argv[2][1:] == '1':
                params_HE = np.array([0., 0., 10e-6])
            elif sys.argv[2][1:] == '2':
                params_HE = np.array([0., 0., 20e-6])
            elif sys.argv[2][1:] == '3':
                params_HE = np.array([0., 0., 25e-6])
            elif sys.argv[2][1:] == '4':
                params_HE = np.array([0., 0., 44e-6])
            else:
                print('Undefined instruction:', sys.argv[1], sys.argv[2])
                exit(1)
    else:
        print('Undefined instruction:', sys.argv[1])
        exit(1)


# params = {
#     'gamma': 8.681e6,
#     'eta': 0.006,
#     'HE': np.array([0., 0., 50e-6]),
#     'gamma_D': 0, # easy axis modify, 1/3 before.
#     'dt': 1e-3, # 5e-5, # easy axis modify, 1e-2 before.
#     'max_iteration': 500,
#     'eps': 1e-4,
#     'warm_start': False
# }

params = {
    'gamma': 8.681e6,
    'eta': 0.01,
    'HE': params_HE, # presentation modify, 50e-6 before.
    'gamma_D': params_gamma_D, # easy axis modify, 1/3 before.
    'dt': params_dt, # easy axis modify, 1e-2 before.
    'max_iteration': 50,
    'eps': 1e-4,
    'warm_start': False
}

# ferromagnet
cparams_fe = {
    'Ms': 8e-5,
    'num_of_particle': fe_num_of_particle,
    'radius': 126e-8
}

# one particle with z-axis as easy axis
num_of_ea_cell = 1
cparams_ea = {
    'position': np.array([0, 0, 0]),
    'Ms': 8e-5,
    'num_of_particle': 1,
    'radius': 126e-12,
    'Ku': 2e-3
}

if fe_active:
    cells = [mag.Cell(position=np.random.randn(3) * 5, **cparams_fe) for _ in range(num_of_fe_cell)]

if ea_active:
    cells = [mag.Cell(**cparams_ea) for _ in range(num_of_ea_cell)]

mag.magnetic_simulation(cells, **params)

print()
s = input('Save pictures? (y/n) ')
if s == 'y':
    mag.plot_3D_cell(cells, 10, heff_change, show_dmdt, show_rg)