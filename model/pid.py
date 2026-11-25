# model/pid.py
class PID:
    """PID avec dérivée sur la mesure filtrée et anti-windup."""

    def __init__(self, kp, ki, kd, umin=-25.0, umax=25.0, dt=0.01, n=20.0):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.umin, self.umax, self.dt = umin, umax, dt
        self.alpha = dt / (dt + 1.0 / n)   # coefficient du filtre (n = 20 rad/s)
        self.i = 0.0
        self.m_prev = None
        self.d_f = 0.0

    def step(self, ref, meas):
        e = ref - meas
        if self.m_prev is None:
            self.m_prev = meas
        d_raw = -(meas - self.m_prev) / self.dt      # dérivée de la MESURE (signe -)
        self.m_prev = meas
        self.d_f += self.alpha * (d_raw - self.d_f)  # filtre passe-bas
        u_raw = self.kp * e + self.ki * self.i + self.kd * self.d_f
        u = max(self.umin, min(self.umax, u_raw))
        if u == u_raw:                               # anti-windup
            self.i += e * self.dt
        return u