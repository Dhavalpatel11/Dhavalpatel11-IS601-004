from MyCalc import Calculator
import pytest

def test_add_dap44():
    calc = Calculator()
    check=calc.calc(9, 2, "+")
    assert check == 11


def test_ans_add_dap44():
    calc = Calculator()
    ans=calc.calc(3, 2, "+")
    check=calc.calc("ans", 2, "+")
    assert ans == 5
    assert check == 7

def test_subtract_dap44():
    calc = Calculator()
    check=calc.calc(9,1,"-")
    assert check == 8

def test_ans_subtract_dap44():
    calc = Calculator()
    ans= calc.calc(3, 2, "-")
    check=calc.calc("ans",1,"-")
    assert ans == 1
    assert check == 0


def test_mult_dap44():
    calc = Calculator()
    check = calc.calc(7, 5, "*")
    assert check == 35

def test_ans_mult_dap44():
    calc = Calculator()
    ans = calc.calc(3, 5, "*")
    check = calc.calc("ans", 5, "*")
    assert ans == 15
    assert check == 75


def test_division_dap44():
    calc = Calculator()
    check = calc.calc(10, 2, "/")
    assert check == 5

def test_ans_division_dap44():
    calc = Calculator()
    ans = calc.calc(8, 2, "/")
    check = calc.calc("ans", 2, "/")
    assert ans == 4
    assert check == 2



