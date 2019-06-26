from .particle import Particle
import numpy as np


class Cell:
    # TODO: Ms的初始化
    def __init__(self, position=None, Ms=8e-5, num_of_particle=2, radius=0.1, changeable=True, m=None):
        self.position = position
        self.num_of_particle = num_of_particle
        self.particles = []
        self.radius = radius
        self.volume = 4 / 3 * np.pi * self.radius ** 3
        self._changeable = changeable
        self._m = m

        if self._m is None:
            if self.num_of_particle % 2 == 1:
                m = np.random.randn(3)
                m = m / np.linalg.norm(m)
                self.particles.append(Particle(position, m * Ms, changeable))
                num_of_particle -= 1
            
            for i in range(0, num_of_particle, 2):
                m = np.random.randn(3)
                m /= np.linalg.norm(m)
                self.particles.append(Particle(position, m * Ms, changeable))
                self.particles.append(Particle(position, -m * Ms, changeable))
        else:
            self._m /= np.linalg.norm(self._m)
            for i in range(0, num_of_particle):
                self.particles.append(Particle(position, self._m * Ms, changeable))

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
        return _M / len(self.particles)
