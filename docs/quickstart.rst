Quickstart
==========

Eager to get started? This page gives a good introduction to Injectify. Follow
:doc:`installation` to set up a project and install Injectify first.

A Minimal Application
---------------------

 Injecting code with Injectify is very simple.

.. code-block:: python

    from injectify import inject, HeadInjector

    def foo(x):
        return x

    print(foo(10))  # 10

    @inject(target=foo, injector=HeadInjector())
    def handler():
        x = 9000

    print(foo(10))  # 9000

So what does this code do?

1. We begin by importing from the ``injectify`` module.
2. Next we defined a function ``foo`` that we will inject code into.
3. When we print the result of ``foo(10)``, we get 10.
4. We then use the :func:`~injectify.api.inject` decorator. The first argument
   is the target object. This is the object that will have code injected into.
   The second argument is the injector. An injector is used to indicate the
   point at which the target object should be injected. Here we use the
   :class:`~injectify.injectors.HeadInjector` for our injector. This injector
   indicates that the code should be injected at the top of the target object.
5. Then we defined a function ``handler``. The body of this function is the
   code that will be injected into ``foo``.
6. Now when we print the result of ``foo(10)``, we get 9000.

Thus, after we inject the body of ``handler``, the function ``foo`` then has
the following code:

.. code-block:: python

    def foo(x):
        x = 9000
        return x

Injection Points
----------------

The first thing we need to be able to do is identify parts of the target
object. Let's decorate a function with markers which show some of the areas we
are able to easily identify.

.. code-block:: python

    def bar():
        # HEAD

        def wrapper():  # NESTED
            pass

        x = 10  # FIELD

        if x > 10:
            # RETURN
            return True
        else:
            # RETURN
            return False

        # TAIL

The markers indicate parts of the object's anatomy:

* **HEAD** indicates the point at the top of the target object.
* **TAIL** indicates the point at the bottom of the target object.
* **FIELD** indicates the point at a field's assignment.
* **RETURN** indicates the point before a return statement.
* **NESTED** indicates a nested function.

.. note::

    Not all Python objects have all these injection points. For example, a
    module does not have a return statement, so a module has no RETURN marker.

Injectors
---------

The injector you use tells Injectify the injection point to use when merging
the code inside the target object. Each of the markers above has a
corresponding injector.

For more information on injectors you can visit the
:ref:`injectify.injectors module` documentation.
