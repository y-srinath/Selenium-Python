import pytest

@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello World!"
    assert msg == "Hi", "Test failed, strings do not match"

def test_secondProgram():
    a = 10
    b = 20   
    assert a + b == 30, "Test failed, sum does not match expected value"