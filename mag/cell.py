from .particle import Particle
import numpy as np


class Cell:
    def __init__(self, position=None, num_of_magnetic_moment=2, radius=0.1):
        self.position = position
        self.num_of_magnetic_moment = num_of_magnetic_moment
        self.particles = [Particle(position) for i in range(num_of_magnetic_moment)]
        self.radius = radius
        self.volume = 4 / 3 * np.pi ** 3

    @property
    def mu(self):
        _mu = 0.
        for particle in self.particles:
            _mu += particle.M
        _mu *= self.volume / len(self.particles)
        return _mu

    @property
    def M(self):
        _M = 0.
        for particle in self.particles:
            _M += particle.M
        # TODO: 是否需要除以len(particles)
        return _M / len(particles)
