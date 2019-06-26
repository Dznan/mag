from .cell import Cell


class Box:
    def __init__(self, position, width, height, cell_shape=(2, 2), **cell_param):
        assert width * cell_shape[1] == height * cell_shape[2]
        self.position = position
        self.width = width
        self.height = height
        radius = width / cell_shape[0] / 2
        self.cells = []
        for i in range(cell_shape[0]):
            for j in range(cell_shape[1]):
                self.cells.append(
                    Cell(position=(radius + radius*i, radius, + radius*j), **cell_param)
                )
