import sys
from urllib.response import addbase

#TODO make with 'pip install -e'
sys.path.append("../src")

from math demo import add, add_with_bug

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


if __name__ == '__main__':
    test_addition()