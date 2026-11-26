# tests/test_req07_saturation.py
import numpy as np
from simulate import run
def test_req07_command_limited_to_25deg():
    _, _, _, delta, cmd = run(2.0, 1.5, 1.0, ref=20.0)   # échelon fort
    assert np.max(np.abs(cmd)) <= 25.0 + 1e-9
    assert np.max(np.abs(delta)) <= 25.0 + 1e-9