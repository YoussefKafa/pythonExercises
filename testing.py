
import functionsToTest 
import pytest
def test_sum():
    assert functionsToTest.sum(2,2) == 4

def test_sum1():
    assert functionsToTest.sum(2,3) == 5

#run python -m pytest pytest.py 