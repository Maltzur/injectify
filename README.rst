=========
Injectify
=========

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
