# tests/test_req02_settling.py
from simulate import run, metrics
def test_req02_settling_below_3s():
    t, y, *_ = run(2.0, 1.5, 1.0)
    assert metrics(t, y)[1] < 3.0