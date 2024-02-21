def double(x):
    return x * 2

def test_double():
    assert 4 == double(2)

def plus_one(x):
    return x + 1

def test_plus_one():
    assert 2 == plus_one(1)

def minus_one(n):
    return n - 1

def test_minus_one():
    assert 1 == minus_one(2)

def plus_two(n):
    return n + 2

def test_plus_two():
    assert 2 == plus_two(0)

def minus_two(n):
    return n - 2

def test_minus_two():
    assert 0 == minus_two(2)