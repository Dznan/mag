import numpy as np
import mag


cells = [mag.Cell(np.random.randn(3) / 10 * np.array([1, 1, 0]), radius=126e-12) for _ in range(1)]
# mag.plot_cell(cells)

mag.magnetic_simulation(cells, gamma=8.681e6, eta=0.01)

mag.plot_cell(cells)