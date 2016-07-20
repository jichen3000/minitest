'''
    http://stackoverflow.com/questions/14956313/dictionary-ordering-non-deterministic-in-python3
    run this script many times in python 3.
    sometimes print:
    {'value': 'bar', 'name': 'foo'}
    sometimes print:
    {'name': 'foo', 'value': 'bar'}
'''
foo = {'name': 'foo', 'value': 'bar'}
print("foo : {'name': 'foo', 'value': 'bar'}")
print("%s" % foo)
print(foo)