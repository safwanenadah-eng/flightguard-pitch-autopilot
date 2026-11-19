# model/simulate.py
import numpy as np
from plant import Actuator, PitchPlant, Sensor, gust, DT
from pid import PID

def run(kp, ki, kd, ref=5.0, T=10.0, with_gust=False, sigma=0.05):
    act, plant, sensor, pid = Actuator(), PitchPlant(), Sensor(sigma=sigma), PID(kp, ki, kd)
    t = np.arange(0, T, DT)
    y, meas_log, delta = (np.zeros_like(t) for _ in range(3))
    meas = 0.0
    for k, tk in enumerate(t):
        cmd = pid.step(ref, meas)
        delta[k] = act.step(cmd)
        y[k] = plant.step(delta[k], d=gust(tk) if with_gust else 0.0)
        meas = sensor.read(y[k])
        meas_log[k] = meas
    return t, y, meas_log, delta