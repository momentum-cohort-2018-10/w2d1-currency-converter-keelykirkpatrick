#Create a set of functions to convert currency from one direction to another
#No functions longer than 7 lines of coxde
#100% test coverage
#Passing unit tests
#No PEP8 or Pyflakes warnings or errors
#Each requirement, write test first, then make test to pass

from currency import convert

def test_convert_same_currency():
    assert convert([], 1, current="USD", to="USD") == 1
    assert convert([], 2, current="USD", to="USD") == 2

def test_convert_usd_to_euros():
    assert convert( rates=[('USD', "EUR", 0.74)], values, current='USD', to='EUR')