import numpy as np
import mag


cells = [mag.Cell(np.random.randn(2)) for _ in range(4)]
mag.plot_cell(cells)
