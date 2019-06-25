import numpy as np


class Particle:
    def __init__(self, position=None, M=None, Heff=None):
        self._position = position
        self._magnetic_moment_density = M
        # self._effective_magnetic_field = Heff
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, pos):
        """
        pos is a vector.
        """
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
    
    # @property
    # def Heff(self):
    #     return self._effective_magnetic_field
    
    # @Heff.setter
    # def Heff(self, h):
    #     self._effective_magnetic_field = h

    # @property
    # def effective_magnetic_field(self):
    #     return self._effective_magnetic_field
    
    # @effective_magnetic_field.setter
    # def effective_magnetic_field(self, h):
    #     self._effective_magnetic_field = h
    