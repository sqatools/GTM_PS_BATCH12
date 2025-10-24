"""
install pytest framework with command
pip install pytest
"""
import pytest

ENV= "TEST"

@pytest.mark.skipif(ENV == "PROD", reason="Feature is not available in the PROD environment")
@pytest.mark.smoke
def test_addition():
    num1 = 30
    num2 = 40
    assert num1 + num2 == 70


@pytest.mark.skip
@pytest.mark.smoke
def test_multiplication():
    num1 = 30
    num2 = 40
    assert num1 * num2 == 1200


@pytest.mark.sanity
@pytest.mark.xfail
def test_subtraction():
    num1 = 30
    num2 = 600
    assert num2 - num1 == 500


@pytest.mark.sanity
@pytest.mark.xfail
def test_addition_fun1():
    num1 = 30
    num2 = 40
    assert num1 + num2 == 70


@pytest.mark.regression
def test_multiplication_fun2():
    num1 = 30
    num2 = 40
    assert num1 * num2 == 1200


@pytest.mark.regression
def test_subtraction_fun3():
    num1 = 30
    num2 = 600
    assert num2 - num1 == 500


def test_division():
    num1 = 30
    num2 = 4
    assert num1 // num2 == 3.28
