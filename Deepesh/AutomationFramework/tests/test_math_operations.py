"""
install pytest framework with commnad
- pip install pytest
"""

def test_addition():
    num1 = 30
    num2 = 40
    assert num1+num2 == 70

def test_multiplication():
    num1 = 30
    num2 = 40
    assert num1*num2 == 1200


def test_subtraction():
    num1 = 30
    num2 = 600
    assert num2- num1 == 500


def test_addition_fun1():
    num1 = 30
    num2 = 40
    assert num1+num2 == 70

def test_multiplication_fun2():
    num1 = 30
    num2 = 40
    assert num1*num2 == 1200


def test_subtraction_fun3():
    num1 = 30
    num2 = 600
    assert num2- num1 == 500

def division():
    num1 = 30
    num2 = 4
    assert num1//num2 == 3.28