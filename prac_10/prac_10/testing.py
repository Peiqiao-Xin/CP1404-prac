import pytest
from recursion import factorial, fib

def test_factorial_base_case():
    assert factorial(0) == 1

def test_factorial_small():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_fib_sequence_length():
    seq = fib(5)
    assert isinstance(seq, list)
    assert seq == [0, 1, 1, 2, 3]

def test_fib_zero():
    assert fib(0) == []

def test_fib_one():
    assert fib(1) == [0]