import numpy as np
import mag


cells = [mag.Cell(np.random.randn(2) / 10, radius=0.01) for _ in range(4)]
mag.plot_cell(cells)
