# BDD with Python

## Introduction
Following the tutorial from [tutsplus](https://code.tutsplus.com/tutorials/behavior-driven-development-in-python--net-26547?_ga=2.53094891.2123691085.1515887817-1593036353.1515199852)
by [David Sale](https://tutsplus.com/authors/david-sale?_ga=2.247794695.1248959652.1515442515-1593036353.1515199852)

BDD stands for Behaviour driven development mostly used in *Agile development*, it follows the same principle as TDD, writing your test before the code.
But the key point is to not only test have granular code tested with unit test, but also having the application tested end to end using acceptance tests.

The process can be simply defined as:
 
- Write a failing acceptance test
- Write a failing unit test
- Make the unit test pass
- Refactor
- Make the acceptance test pass

Acceptance tests famously make use of an English (or possibly alternative) language format "feature" file, 
describing what the test is covering and the individual tests themselves.

## Acceptance Tests with Gherkin Syntax

Acceptance tests usually make use of the Gherkin Syntax, introduced by the Cucumber Framework, written for Ruby. 
The syntax is quite easy to understand, and, in the Lettuce Python package, makes use of the following eight keywords to define your features and tests:

- Given
- When
- Then
- And

The acceptance tests will be saved in a `.feature` file. It id deco;posed into multiple blocks:

- Feature:
  - Where you write your documentation for what this group of test is cover, no code executed here. Only for comprehension
- Background:
  - Executed prior to every *Scenario* in the `.feature` file, similar to the `SetUp()` in `unittest`.
- Scenario:
  - Here you define the test, the first line is for documentation and then the test (with the give syntax).
- Scenario Outline:

Once the `.feature` has been created  you need to have a `steps.py` that will create the test from the features (it's not just magic).
The `steps.py` uses RegEx with lettuce to read the input and execute the test.

## Project Structure

The project should be structured like:

```
Root
  |_ app
  |   |_ __init__.py
  |   |_ calculator.py
  |
  |_ tests
      |_ __init__.py
      |_ features
          |_ calculator.feature
          |_ steps.py
 ```  

## Installation

For the process, once you have python **2.x** installed (because lettuce is only compatible with Python 2.x):

- Install [lettuce](http://lettuce.it/index.html) that will be used as the *Gherkin* parser.
```
pip install lettuce
```
- Install the same test module as in tdd such as [Nose](http://nose.readthedocs.io/en/latest/):
```
easy_install nose

# or

pip instaal nose
```    
    

## Executing the features

You can either run just one feature file, or, 
if you pass a directory of feature files, you can run all of them.
```bash
lettuce tests/features/calculator.feature 
```

The expected result:
```yaml
Feature: As a person for curiosity's sake        # tests/features/calculator.feature:1
  I wish to demonstrate                          # tests/features/calculator.feature:2
  How easy writing Acceptance Tests              # tests/features/calculator.feature:3
  In Python really is.                           # tests/features/calculator.feature:4

  Background:
    Given I am using the calculator              # tests/features/steps.py:7
    Given I am using the calculator              # tests/features/steps.py:7

  Scenario: Calculate 2 plus 2 on our calculator # tests/features/calculator.feature:9
    Given I input "2" add "2"                    # tests/features/steps.py:13
    Then I should see "4"                        # tests/features/steps.py:18

1 feature (1 passed)
1 scenario (1 passed)
2 steps (2 passed)
```