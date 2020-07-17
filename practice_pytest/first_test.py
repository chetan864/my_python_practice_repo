import pytest

def func(x):
    return x + 5

def test_method_to_fail():
    assert func(3) == 5

def test_method_to_pass():
    assert func(3) == 8