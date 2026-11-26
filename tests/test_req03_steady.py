# tests/test_req03_steady.py
from simulate import run, metrics
def test_req03_steady_error_below_1deg():
    t, y, *_ = run(2.0, 1.5, 1.0)
    assert metrics(t, y)[2] < 1.0