"""This module contains the utility functions that power Injectify."""

import ast
import inspect
from textwrap import dedent

import dill


def parse_object(obj):
    """Parse the source into an AST node."""
    for _ in range(5):
        try:
            return ast.parse(source)
        except IndentationError:
            source = dedent(source)


def get_class_that_defined_method(meth):
    if dill.source.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if cls.__dict__.get(meth.__name__) is meth:
                return cls
        meth = meth.__func__  # fallback to __qualname__ parsing
    if dill.source.isfunction(meth):
        class_name = meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0]
        try:
            cls = getattr(dill.source.getmodule(meth), class_name)
        except AttributeError:
            cls = meth.__globals__.get(class_name)
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)  # handle special descriptor objects


def tryattrs(obj, *attrs):
    """Return the first value of the named attributes found of the given object."""
    for attr in attrs:
        try:
            return getattr(obj, attr)
        except AttributeError:
            pass
    obj_name = dill.source.getname(obj)
    raise AttributeError("'{}' object has no attribute in {}", obj_name, attrs)
