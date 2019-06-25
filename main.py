import numpy as np
import mag


cells = [mag.Cell(np.array([0, 0, 0]), radius=126e-12) for _ in range(1)]
# mag.plot_cell(cells)

mag.magnetic_simulation(cells, gamma=8.681e6, eta=0.01)

mag.plot_3D_cell(cells)