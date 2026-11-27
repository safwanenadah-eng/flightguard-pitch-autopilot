# tests/test_req08_stability.py
import numpy as np, plant, simulate
def test_req08_stable_with_slow_actuator(monkeypatch):
    monkeypatch.setattr(plant.Actuator.__init__, "__defaults__", (0.25, 40.0, 25.0))
    t, y, *_ = simulate.run(2.0, 1.5, 1.0)
    assert np.max(np.abs(y)) < 10.0                 # reste borné
    assert abs(y[-50:].mean() - 5.0) < 0.5          # revient à la consigne