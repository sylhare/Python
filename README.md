# Python projects 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/79b0234d210c427f95285a15dc4f81e9)](https://www.codacy.com/app/Sylhare/Python_Projects?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sylhare/Python_Projects&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/Sylhare/Python.svg?branch=master)](https://travis-ci.org/Sylhare/Python)

## Introduction 

Some miscellaneous Python projects that I created or worked on. Mainly tests on some functionality or example 
that I can reuse for other works as tutorials.

### Installing Python

There are currently two versions of python currently in use, 
I would suggest going with the latest Python 3 (3.x.x) 
because it is the future but there's no wrong choice here 
and you can switch from one to the other easily.

The [Anaconda](https://www.anaconda.com/) distribution is the easiest way to get you started with python, 
it comes with built in package, IDE and a lot of great stuffs.

 - Download [Anaconda](https://www.anaconda.com/download/)

You can also do it the classic way, 
by downloading python directly from there website [here](https://www.python.org/downloads/) and then start coding on a text editor.

Python should have already been installed if you're using a linux distribution. 
You can always check which version is installed:

```bash
python --version
```

### Python on Windows

Assuming that you've installed python via Anaconda, or manually (setting the environment path as well).

Start a python prompt on the command prompt:

```bash
python
```

Install dependencies via pip on a command prompt:

```bash
python -m pip install <package>
```
   
Uninstall with pip through:

```bash
python -m pip uninstall <package>
```

Install dependencies through a proxy

```bash
python -m pip install --proxy http://user:password@proxyserver:port <package>
```

- Replace Package by the *package* you want to install
- the `-m` means module
- user and password are the ones you use to connect to your session (most probably)
-  The proxy server and port are in 
	-  Control Panel > Internet Options > Connections > Lan Settings button

Run a python script on a command prompt (windows):

```bash
python.exe script.py arg1
```

### Creating Python packages

A Python package is simply an organized collection of python modules. A python module is simply a single python file.

To create a python package, create a directory and then add a `__init__.py` file. 
Creating a package with `__init__.py` is all about making it easier to develop large Python projects. 
It provides an easy way for you to group large folders of many separate python scripts into a single importable module.

[PyPI](https://pypi.org/) is the Python Package Index a repository of software for the Python programming language. 
You can find a seed template at [sylhare/python-seed](https://github.com/sylhare/pyhon-seed)

Read more about [Publish a pyhton package](https://sylhare.github.io/2018/01/12/Publish-a-python-package.html)

### Create a webserver in Python

You can simply create a webserver at [localhost:8000](http://localhost:8000) in python thanks to this module:

- Python 2

```bash
python –m SimpleHTTPServer 9000 # You can change the port
```

- Python 3

```bash
python -m http.server 8000 
```

### Sources

- [For special methods in class](http://www.diveintopython3.net/special-method-names.html)
- [Built in attributes](https://www.tutorialspoint.com/python/python_classes_objects.htm)
- [Going Full Stack Python](https://www.fullstackpython.com/introduction.html)
- [How to create a python package](http://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html)
- [How to structure your python project](http://docs.python-guide.org/en/latest/writing/structure/)
- [Python package - Minimal Structure](http://python-packaging.readthedocs.io/en/latest/minimal.html)