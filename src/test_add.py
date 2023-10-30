from add import add

def test_add_int():
    assert add(4,5)==19

def test_add_str():
    assert add('a','b')=='ab'