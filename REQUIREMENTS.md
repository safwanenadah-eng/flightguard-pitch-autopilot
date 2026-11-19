# Requirements

Scope: Fixed-wing light aircraft / UAV, pitch axis, 1 sensor, PC simulation.

| ID | Requirement | Verification Method |
|----|-------------|---------------------|
| REQ-01 | Overshoot < 10% for a 5° step input | Simulation test |
| REQ-02 | Settling time (2%) < 3 s | Simulation test |
| REQ-03 | Steady-state error < 1° | Simulation test |
| REQ-04 | Sensor fault detected in < 200 ms | Fault injection test |
| REQ-05 | Control task at 100 Hz, jitter < 1 ms | FreeRTOS timing measurement |
| REQ-06 | C code free of cppcheck violations | Static analysis in CI |
| REQ-07 | Control command limited to ±25° | Simulation test |
| REQ-08 | Closed-loop stable with actuator (delay + rate limit) | Simulation test |