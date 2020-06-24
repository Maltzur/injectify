"""This module contains the apis that power Injectify."""


def inject(target, injector):
    """Decorate a function to inject that code into the target object.

    :param target: The object to inject code into.
    :param injector: The :class:`~injectify.injectors.BaseInjector`.
    """

    def decorator(f):
        injector.prepare(target=target, handler=f)
        injector.compile(injector.visit_target())
        return f

    return decorator
