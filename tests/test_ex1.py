import pytest 


def test_example():
    print('test1')
    assert 1 == 1

def test_example1():
    assert 1 == 2

'''
You can run the tests individually

You can do 

pytest [name of the folder] [name of the file] :: [name of the function]

pytest tests/test_ex1.py::example1
'''
    