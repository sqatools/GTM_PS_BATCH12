"""
Fixture scopes.
1.  function :  This fixture will execute before and after execution of each test function.
2.  class :  This fixture will execute before and after execution of each test class.
3.  module : This fixture will execute before and after execution of each test module.
4.  package : This fixture will execute before and after execution of each test package.
5.  session : This fixture will execute before and after execution of pytest session.

"""
import pytest

@pytest.fixture(scope="function")
def func_fixture():
    print("\n------Function Fixture Initiated-----")
    yield
    print("\n------Function Fixture Completed-----")

@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\n------class Fixture Initiated-----")
    yield
    print("\n------class Fixture Completed-----")

@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("\n------module Fixture Initiated-----")
    yield
    print("\n------module Fixture Completed-----")


@pytest.fixture(scope="package", autouse=True)
def package_fixture():
    print("\n------package Fixture Initiated-----")
    yield
    print("\n------package Fixture Completed-----")


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n------session Fixture Initiated-----")
    yield
    print("\n------session Fixture Completed-----")


def test_addition(func_fixture):
    num1 = 30
    num2 = 40
    assert num1+num2 == 70

def test_multiplication(func_fixture):
    num1 = 30
    num2 = 40
    assert num1*num2 == 1200


def test_subtraction(func_fixture):
    num1 = 30
    num2 = 600
    assert num2- num1 == 500


def test_addition_fun1(func_fixture):
    num1 = 30
    num2 = 40
    assert num1+num2 == 70

def test_multiplication_fun2(func_fixture):
    num1 = 30
    num2 = 40
    assert num1*num2 == 1200


def test_subtraction_fun3(func_fixture):
    num1 = 30
    num2 = 600
    assert num2- num1 == 500

def division(func_fixture):
    num1 = 30
    num2 = 4
    assert num1//num2 == 3.28