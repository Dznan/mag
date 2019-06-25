from .particle import Particle
import numpy as np


class Cell:
    # TODO: Ms的初始化
    def __init__(self, position=None, Ms=1, radius=0.1):
        self.position = position
        self.num_of_particle = 2
        zero_vec = np.zeros(3)
        m = np.random.randn(3)
        m = m / np.linalg.norm(m)
        self.particles = [Particle(position, m * Ms), Particle(position, -m * Ms)]
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
