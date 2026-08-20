import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "calculator"))
from functions.arithmetics import summe, multiplikation, subtraktion, division
import pytest

def test_ops():
    assert summe(2, 3) == 5
    assert multiplikation(2, 4) == 8
    assert subtraktion(10, 3) == 7
    assert division(9, 3) == 3

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)
