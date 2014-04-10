# http://guide.python-distribute.org/creation.html
# distribute to PyPI
# Create your distribution
# python setup.py sdist
# Uploading your distribution file
# python setup.py register # just run in first time.

# python setup.py sdist upload

if __name__ == '__main__':
    # import the minitest
    from minitest import *

    import operator

    # declare a variable for test
    tself = get_test_self()
    # you could put all your test variables on tself
    # just like declare your variables on setup.
    tself.jc = "jc"

    # declare a test
    with test("test must_equal"):
        tself.jc.must_equal('jc')
        None.must_equal(None)

    with test("test must_true"):
        True.must_true()
        False.must_true()

    with test("test must_false"):
        True.must_false()
        False.must_false()

    # using a funcation to test equal.
    with test("test must_equal_with_func"):
        (1).must_equal(1, key=operator.eq)
        (1).must_equal(2, key=operator.eq)

    def div_zero():
        1/0
        
    # test excecption
    with test("test must_raise"):
        (lambda : div_zero()).must_raise(ZeroDivisionError)
        (lambda : div_zero()).must_raise(ZeroDivisionError, "integer division or modulo by zero")
        (lambda : div_zero()).must_raise(ZeroDivisionError, "in")

    # customize your must method 
    with test("inject"):
        def close_one(int1, int2):
            return int1 == int2+1 or int2 == int1+1
        (1).must_equal(2, close_one)
        inject(close_one)
        (1).must_close_one(2)
        inject_customized_must_method(close_one, 'must_close')
        (1).must_close(2)

        # import numpy
        # inject(numpy.allclose, 'must_close')
        # numpy.array([1]).must_close(numpy.array([1.0]))

    value = "Minitest"
    value.p()
    value.p("It is a value:")
    value.p(auto_get_title=False)
    value.pp()
    value.pp("It is a value:")
    value.pp(auto_get_title=False)
    [1, 2].length().pp()
    (1, 2).size().pp()

