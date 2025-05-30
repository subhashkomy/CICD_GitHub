from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(5,7)==12

def test_sub():    
    assert sub(-1, 1) == -2
    assert sub(500-375)==125    