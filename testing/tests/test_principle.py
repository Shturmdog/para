import sys

#TODO make with 'pip install -e
sys.path.append("../src")

from math demo import add

def test_addition():
    assert add(2, 2) == 4
    print("Tests passed")

if __name__ == '__main__':
    test_addition()