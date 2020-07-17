import pytest

@pytest.mark.one
def test_method_to_fail_new():
    x = 5
    y = 10
    assert x == y


@pytest.mark.two
def test_method_to_pass_new():
    a = 15
    b = 20
    assert a + 5 == b
