#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2
def halve(number):
    return number / 2

def test_halve_int():
    result = halve(100)
    assert result == 50

test_halve_int()
def halve(number):
    return number / 2

def test_halve_float():
    result = halve(99.0)
    assert result == 49.5

test_halve_float()