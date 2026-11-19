# tests/test_plant.py
import numpy as np
from plant import Actuator, PitchPlant, Sensor, DT

def test_static_gain_is_one():
    p = PitchPlant()
    for _ in range(int(15 / DT)):
        p.step(1.0)
    assert abs(p.theta - 1.0) < 0.01

def test_actuator_saturation():            # prépare REQ-07
    a = Actuator()
    for _ in range(int(3 / DT)):
        a.step(100.0)
    assert abs(a.delta) <= 25.0 + 1e-9

def test_actuator_rate_limit():
    a = Actuator()
    for _ in range(10):                    # 0.1 s
        a.step(25.0)
    assert a.delta <= 40.0 * 0.1 + 1e-6    # <= 4 deg

def test_sensor_noise_level():
    s = Sensor(sigma=0.05)
    v = np.array([s.read(0.0) for _ in range(5000)])
    assert abs(v.std() - 0.05) < 0.01