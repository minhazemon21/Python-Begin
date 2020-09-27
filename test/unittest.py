
import pytest
def test_calc_total():
    result = pytest.calc_total(9,20)
    assert result == 180
def test_calc_multiply():
    result2 = pytest.calc_multiply(10,20)
    assert result2 == 200