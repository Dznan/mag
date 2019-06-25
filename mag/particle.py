import numpy as np


class Particle:
    def __init__(self, position=None, M=None, changeable=True):
        self._position = position
        self._magnetic_moment_density = M
        self._changeable = changeable
        self._cache = {
            'H': [],
            'Heff': [],
            'm': []
        }
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos):
        assert len(pos) in [2, 3]
        self._position = pos
    
    @property
    def Ms(self):
        return np.linalg.norm(self._magnetic_moment_density)

    @property
    def m(self):
        return self._magnetic_moment_density / self.Ms
    
    @property
    def M(self):
        return self._magnetic_moment_density

    @M.setter
    def M(self, _M):
        self._magnetic_moment_density = _M

    @property
    def magnetic_moment_density(self):
        return self._magnetic_moment_density

    @magnetic_moment_density.setter
    def magnetic_moment_density(self, _m):
        self._magnetic_moment_density = _m
    
