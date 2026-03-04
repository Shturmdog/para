import sys
from urllib.response import addbase

#TODO make with 'pip install -e'
sys.path.append("../src")

from math_demo import (add, add_with_bug, add_something)

def test_addition():
    assert add(2, 2) == 4
    print("Tests passed")

def test_bug_addition_notsufficient():
    assert add_with_bug(2, 2) == 4
    print("Test BUG ADDITION PASSED")

def test_bug_addition_enough():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(5, 6) == 11
    print("Test BUG ADDITION PASSED")

def test_addition_duplicated_logic():
    #BAD TEST since it relies on absence of '+' in add(
    assert add(6, 3) == 6 + 3
    #GOOD TEST since input and output are independent add()
    assert add(6, 3) == 9
    print("Test DUPLICATION LOGIC PASSED")

def test_addition_overcomplicated():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j #bad since violated "duplicated"
            assert add(-i, j) == -i + j
            assert add(i, -j) == i - j
            assert add(-i, -j) == -i - j

def test_addition_resonable():
    assert add(6, 3) == 9
    assert add(0, 3) == 3
    assert add(0, -3) == -3
    assert add(-7, 83) == 76
    assert add(-7, -83) == -90

def test_add_something_resonable():
    assert add_something(6, 3) == 9
    assert add_something(None, None) == 0
    assert add_something(None, "abc") == 0
    assert add_something(None, 10) == 0
    assert add_something("abc", 10) == "abc10"
    assert add_something("10", "abc") == "10abc"
    assert add_something("xyz", "abc") == "xyzabc"
    print("TESTS PASSED")
    




if __name__ == '__main__':
    test_addition()
    test_bug_addition_notsufficient()
    test_bug_addition_enough()
    test_addition_duplicated_logic()
    test_addition_resonable()
    test_add_something_resonable()