Installation
============

Python Version
--------------

Injectify is compatible with Python 3.5 and newer.

Dependencies
------------

These packages will be installed automatically with Injectify.
If you don't have ``pipenv``, head over the Pipenv website for installation
instructions.

* `astunparse`_ is an AST unparser for Python.

Pipenv
------

The recommended way to install the ``injectify`` package is to simply use `pipenv`_.

.. code-block:: sh

    $ pipenv install injectify

Pipenv is a tool that automatically creates and manages a virtual environment for your
project.

Virtual Environment
-------------------

If you prefer, ``pip`` and ``virtualenv`` can be used separately. Python comes bundled
with the :mod:`venv` module to create virtual environments, which you can use.

Create an Environment
~~~~~~~~~~~~~~~~~~~~~

Create a project folder and a :file:`venv` folder within:

.. code-block:: sh

    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv

Activate the environment
~~~~~~~~~~~~~~~~~~~~~~~~

Before you work on your project, activate the corresponding environment:

.. code-block:: sh

    $ . venv/bin/activate

On Windows:

.. code-block:: bat

    > venv\Scripts\activate

Your shell prompt will change to show the name of the activated environment.

Install Injectify
~~~~~~~~~~~~~~~~~

Within the activated environment, use the following command to install Injectify:

.. code-block:: console

    $ pip install Injectify

Injectify is now installed. Check out the :doc:`/quickstart` or go to the
:doc:`Documentation Overview </index>`.

.. _astunparse: https://github.com/simonpercivall/astunparse
.. _pipenv: https://pipenv.kennethreitz.org
