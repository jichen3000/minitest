# http://guide.python-distribute.org/creation.html
# https://github.com/jichen3000/codes/tree/master/python/minitest

if __name__ == '__main__':
    # import the minitest
    from minitest import *

    import operator

    # declare a test case
    with test_case("new test case"):
        # declare a variable for test
        tself = get_test_self()
        # you could put all your test variables on tself
        # just like declare your variables on setup.
        tself.jc = "jc"

        # declare a test
        with test("test must_equal"):
            tself.jc.must_equal('jc')

        with test("test must_true"):
            True.must_true()
            False.must_true()

        # using a funcation to test equal.
        with test("test must_equal_with_func"):
            (1).must_equal(1, key=operator.eq)
            (1).must_equal(2, key=operator.eq)

        def div_zero():
            1/0
            
        # test excecption
        with test("test must_raise"):
            (lambda : div_zero()).must_raise(ZeroDivisionError)
    # Running tests:

    # .FF.

    # Finished tests in 0.011786s.

    # 1) Failure:
    # The line No is [/Users/Colin/work/minitest/minitest/with_test.py:163]:
    # --- expected
    # +++ actual
    # -[True]
    # #[False]

    # 2) Failure:
    # The line No is [/Users/Colin/work/minitest/minitest/with_test.py:168]:
    # --- expected
    # +++ actual
    # -[2]
    # #[1]

    # 4 tests, 6 assertions, 2 failures, 0 errors.
    # [Finished in 0.1s]