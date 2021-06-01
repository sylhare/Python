# TDD with Python

Following the tutorial from [tutsplus](https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137)
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
- Install [pytest](https://docs.pytest.org/en/latest/) which is another test runner package (by default with Conda)
```
pip install -U pytest
```

## Execute tests

### Standard

If the file is configured with a `__name__` you can run the tests using the standard unittest runner.
python test/test_calculator.py

### Nose

Nose auto-detects unit test, by there name starting with `test_`.
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

## Debugging

You can add some print  statements in your code to see what is happening and better debug your code.
But sometime, it is not enough, and you can use the `pdb` (Python Debugger).
The tool is included in the standard library.

Use `import pdb; pdb.set_trace()` in your code.
If used with nosetests, you need to use the `-s` or it will jam.

To use the pdb console will open try `help`, here is how it looks like entering `list` as a command in pdb.
```python
nosetests -s test/test_bugged_calculators
> /Users/sylhare/Documents/Github/Python/src/tdd/app/calculator.py(31)bugged_add_with_pdb()
-> return x - y
(Pdb) list
  2          def add(self, x, y):
  3             number_types = (int, long, float, complex)
  4
  5             if isinstance(x, number_types) and isinstance(y, number_types):
  6                 import pdb; pdb.set_trace()
  7  ->              return x - y
  8             else:
  9                 raise ValueError
[EOF]
(Pdb)
```

Here are some shortcut that can be useful:

- `n`: step forward to next line of execution.
- `list`: show five lines either side of where you are currently executing to see the code involved with the current execution point.
- `args`: list the variables involved in the current execution point.
- `continue`: run the code through to completion.
- `jump <line number>`: run the code until the specified line number.
- `quit`/`exit`: stop pdb.


## TDD tips

- Write the test first, see it fail then write the code to make it pass
- The method should work on the given parameters, and it should raise an error when those parameters are wrong.

