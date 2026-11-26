# tests/test_req01_overshoot.py
from simulate import run, metrics
def test_req01_overshoot_below_10_percent():
    t, y, *_ = run(2.0, 1.5, 1.0)
    assert metrics(t, y)[0] < 10.0