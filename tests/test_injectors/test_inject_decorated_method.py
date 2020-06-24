"""Tests to make sure that decorated methods are injected as expected."""

from injectify.api import inject
from injectify.injectors import (
    HeadInjector,
    TailInjector,
    ReturnInjector,
    FieldInjector,
    NestedInjector,
)


def decorate(f):
    """Decorate methods to be injected."""

    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


def test_head_injector_correctly_injects_decorated_method():
    """Test :class:`~injectify.injectors.HeadInjector` correctly injects a \
    decorated method."""

    class Target:
        @decorate
        def target(self, x):
            a = 10
            if x > a:
                a = x
            return a

    @inject(target=Target.target, injector=HeadInjector())
    def handler():
        x = 11

    target = Target()
    assert target.target(0) == 11
    assert target.target(10) == 11
    assert target.target(101) == 11


def test_tail_injector_correctly_injects_decorated_method():
    """Test :class:`~injectify.injectors.TailInjector` correctly injects a \
    decorated method."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                return x

    @inject(target=Target.target, injector=TailInjector())
    def handler():
        return -1

    target = Target()
    assert target.target(13) == -1
    assert target.target(101) == 101


def test_return_injector_correctly_injects_decorated_method_all_returns():
    """Test :class:`~injectify.injectors.ReturnInjector` correctly injects a \
    decorated method before all return statements."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
                return y
            else:
                y = x + 2
                return y

    @inject(target=Target.target, injector=ReturnInjector())
    def handler():
        return '{} :)'.format(y)

    target = Target()
    assert target.target(13) == '15 :)'
    assert target.target(101) == '202 :)'


def test_return_injector_correctly_injects_decorated_method_ordinal_returns():
    """Test :class:`~injectify.injectors.ReturnInjector` correctly injects a \
    decorated method before an ordinal return statement."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
                return y
            else:
                y = x + 2
                return y

    @inject(target=Target.target, injector=ReturnInjector(ordinal=1))
    def handler():
        return '{} :)'.format(y)

    target = Target()
    assert target.target(13) == '15 :)'
    assert target.target(101) == 202


def test_field_injector_correctly_injects_decorated_method_before_all_fields():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    decorated method before all ``y`` fields."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
            else:
                y = x + 2
            return y

    @inject(target=Target.target, injector=FieldInjector('y', insert='before'))
    def handler():
        x += 1

    target = Target()
    assert target.target(13) == 16
    assert target.target(101) == 204


def test_field_injector_correctly_injects_decorated_method_after_all_fields():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    decorated method after all ``y`` fields."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
            else:
                y = x + 2
            return y

    @inject(target=Target.target, injector=FieldInjector('y', insert='after'))
    def handler():
        y -= 1

    target = Target()
    assert target.target(13) == 14
    assert target.target(101) == 201


def test_field_injector_correctly_injects_decorated_method_before_ordinal_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    decorated method before an ordinal ``y`` field."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
            else:
                y = x + 2
            return y

    @inject(
        target=Target.target, injector=FieldInjector('y', ordinal=1, insert='before'),
    )
    def handler():
        x += 1

    target = Target()
    assert target.target(13) == 16
    assert target.target(101) == 202


def test_field_injector_correctly_injects_decorated_method_after_ordinal_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    decorated method after an ordinal ``y`` field."""

    class Target:
        @decorate
        def target(self, x):
            if x > 100:
                y = x * 2
            else:
                y = x + 2
            return y

    @inject(
        target=Target.target, injector=FieldInjector('y', ordinal=0, insert='after')
    )
    def handler():
        y -= 1

    target = Target()
    assert target.target(13) == 15
    assert target.target(101) == 201


def test_nested_injector_correctly_injects_decorated_method():
    """Test :class:`~injectify.injectors.NestedInjector` correctly injects a \
    decorated method with a nested function."""

    class Target:
        @decorate
        def target(self, x):
            def nested(y):
                if y > 100:
                    return y

            if x < 200:
                return nested(x)

    @inject(target=Target.target, injector=NestedInjector('nested', TailInjector()))
    def handler():
        return -1

    target = Target()
    assert target.target(13) == -1
    assert target.target(101) == 101
    assert target.target(200) is None
