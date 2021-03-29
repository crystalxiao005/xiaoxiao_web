import pytest
from pytest import assume

#断言失败还能继续运行后面的代码pytest.assume的运用

def test_a():
    print("11111")
    a = "hello"
    b = "hello world"
    #assert a == b
    pytest.assume(a == b)
    #断言通过后，后面的代码会继续
    print("1断言后：%s" % b)
    #assert a in b
    pytest.assume(a in b)

def test_b():
    print("22222")

def test_c():
    print("333")
    a = "hello"
    b = "hello world"
    #assert a == b
    #pytest.assume(a == b)
    with assume:
        assert a == b
    #断言通过后，后面的代码会继续
    print("3断言后：%s" % b)
    #assert a in b
    #pytest.assume(a in b)
    with assume:
        assert a in b


