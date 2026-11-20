# model/plant.py
import numpy as np

DT = 0.01  # pas de calcul : 10 ms (100 Hz)


def clip(x, lo, hi):
    return max(lo, min(hi, x))


class Actuator:
    """Servo de gouverne : premier ordre + vitesse max + saturation.
    Hypothèses (voir docs/assumptions.md) : tau=0.08 s, 40 deg/s, +-25 deg."""

    def __init__(self, tau=0.08, rate_max=40.0, limit=25.0):
        self.tau, self.rate_max, self.limit = tau, rate_max, limit
        self.delta = 0.0  # position réelle de l'elevator (deg)

    def step(self, cmd, dt=DT):
        cmd = clip(cmd, -self.limit, self.limit)           # saturation
        rate = (cmd - self.delta) / self.tau               # retard 1er ordre
        rate = clip(rate, -self.rate_max, self.rate_max)   # vitesse limite
        self.delta += rate * dt
        return self.delta


class PitchPlant:
    """theta'' + 2 theta' + 4 theta = 4 delta + d
    (wn = 2 rad/s, zeta = 0.5, gain statique = 1). Modèle INVENTÉ et simplifié."""

    def __init__(self):
        self.theta = 0.0  # angle de tangage (deg)
        self.q = 0.0      # vitesse de tangage (deg/s)

    def step(self, delta, d=0.0, dt=DT, sub=10):
        h = dt / sub
        for _ in range(sub):
            acc = -2.0 * self.q - 4.0 * self.theta + 4.0 * delta + d
            self.q += acc * h
            self.theta += self.q * h
        return self.theta


class Sensor:
    """Centrale inertielle simplifiée : theta + bruit gaussien."""

    def __init__(self, sigma=0.05, seed=42):
        self.sigma = sigma
        self.rng = np.random.default_rng(seed)  # seed fixe = test reproductible

    def read(self, theta):
        return theta + self.rng.normal(0.0, self.sigma)


def gust(t, t_start=5.0, duration=2.0, amplitude=2.0):
    """Rafale en créneau : perturbation d (deg/s^2)."""
    return amplitude if t_start <= t < t_start + duration else 0.0