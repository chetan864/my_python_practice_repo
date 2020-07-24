import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a, b, c]

@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    assert numbers[0] == 15
@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == 20

def test_method3(numbers):
    z = 25
    assert numbers[2] == 25