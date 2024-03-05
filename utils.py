def double(x):
    return x * 2

def test_double():
    assert 4 == double(2)

def triple(n):
    return n * 3

def test_triple():
    assert 6 == triple(2)

def minus_one(n):
    return n - 1

def test_minus_one():
    assert 1 == minus_one(2)
