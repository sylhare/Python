#!/bin/bash

python --version || echo checking if python 2.x is installed
lettuce --version || echo checking if lettuce package is installed

lettuce tests/features/calculator.feature