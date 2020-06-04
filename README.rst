=========
Injectify
=========

.. image:: https://api.travis-ci.com/Maltzur/injectify.svg?branch=master
    :target: https://travis-ci.com/Maltzur/injectify
.. image:: https://codecov.io/gh/Maltzur/injectify/branch/master/graphs/badge.svg?branch=master
    :target: https://codecov.io/gh/Maltzur/injectify
.. image:: https://img.shields.io/scrutinizer/g/Maltzur/injectify.svg
    :target: https://scrutinizer-ci.com/g/Maltzur/injectify/?branch=master

A code injection library for Python.

Basic Example:

.. code:: python

    from injectify import inject, HeadInjector

    def foo(x):
        return x

    print(foo(10))  # 10

    @inject(target=foo, injector=HeadInjector())
    def handler():
        x = 9000

    print(foo(10))  # 9000


Supported Features
--------------------

Injection is ready to inject code into different kinds of objects.

+ Inject into functions
+ Inject into methods
+ Inject into nested functions
+ Inject into classes
+ Inject into modules

Installation
-------------------

The recommended way to install `injectify` is to use `pipenv`_
(or `pip`, of course):

.. code:: console

    $ pipenv install injectify
    Adding injectify to Pipfile's [packages]…
    ✔ Installation Succeeded
    …

Injectify officially supports Python 3.5+.

.. _pipenv: https://pipenv.kennethreitz.org
