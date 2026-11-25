# model/simulate.py
import numpy as np
from plant import Actuator, PitchPlant, Sensor, gust, DT
from pid import PID

def run(kp, ki, kd, ref=5.0, T=15.0, with_gust=False, sigma=0.05):
    act, plant, sensor, pid = Actuator(), PitchPlant(), Sensor(sigma=sigma), PID(kp, ki, kd)
    t = np.arange(0, T, DT)
    y, m, delta, cmd = (np.zeros_like(t) for _ in range(4))
    meas = 0.0
    for k, tk in enumerate(t):
        cmd[k] = pid.step(ref, meas)
        delta[k] = act.step(cmd[k])
        y[k] = plant.step(delta[k], d=gust(tk, amplitude=4.0) if with_gust else 0.0)
        meas = sensor.read(y[k]); m[k] = meas
    return t, y, m, delta, cmd

def metrics(t, y, ref=5.0):
    overshoot = max(0.0, (y.max() - ref) / ref * 100)
    outside = np.where(np.abs(y - ref) > 0.02 * ref)[0]
    settling = t[outside[-1]] if len(outside) else 0.0
    steady_err = abs(ref - y[-50:].mean())     # moyenne des 0,5 dernières secondes
    return overshoot, settling, steady_err