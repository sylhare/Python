# TDD with Python

Following the tutorial fro; [tutsplus](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137)
by [David Sale](https://tutsplus.com/authors/david-sale?_ga=2.247794695.1248959652.1515442515-1593036353.1515199852)
TDD stands for Test Driven Development, it is the process of implementing code by writing your tests first,
seeing them fail, then writing the code to make the tests pass

The process can be defined as such:

- Write a failing unit test
- Make the unit test pass
- Refactor

Repeat this process for every feature, as is necessary.


## Set Up

How to process to get started:

- Install [Python](https://github.com/Sylhare/Python)
- Install [Nose](http://nose.readthedocs.io/en/latest/), to try the nosetests runner package
```
easy_install nose
```
- Install [pytest](https://docs.pytest.org/en/latest/) which is another test runner package
```
pip install -U pytest
```

## Execute tests

### Standard

If the file is configured with a `__name__` you can run the tests using the standard unittest runner.
python test/test_calculator.py

### Nose

Nose auto detects unit test, by there name starting with `test_`.
Using nosetests to execute tests:
```
nosetests test/test_calculator.py
```

### Py.test

It works as nose, using the same conventions.
A nice feature of pytest is that it captures your output from the test at the bottom in a separate area

Run test using:
```
py.test test/test_calculator.py
```

## TDD tips

The method should work on the given parameters, and it should raise an error when those parameters are wrong.

