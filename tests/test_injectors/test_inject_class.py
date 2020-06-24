"""Tests to make sure that classes are injected as expected."""

from injectify.api import inject
from injectify.injectors import (
    HeadInjector,
    TailInjector,
    FieldInjector,
)


class _cls11:
    x = 10


def test_head_injector_correctly_injects_class():
    """Test :class:`~injectify.injectors.HeadInjector` correctly injects a \
    class."""

    @inject(target=_cls11, injector=HeadInjector())
    def handler():
        x = 11

    assert _cls11.x == 10
    assert _cls11().x == 10


class _cls27:
    x = 10


def test_tail_injector_correctly_injects_class():
    """Test :class:`~injectify.injectors.TailInjector` correctly injects a \
    class."""

    @inject(target=_cls27, injector=TailInjector())
    def handler():
        x = 11

    assert _cls27.x == 11
    assert _cls27().x == 11


class _cls43:
    x = 10
    y = 20
    z = 30


def test_field_injector_correctly_injects_class_before_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    class before the ``y`` field."""

    @inject(target=_cls43, injector=FieldInjector('y', insert='before'))
    def handler():
        x = 15

    assert _cls43.x == 15
    assert _cls43().x == 15
    assert _cls43.y == 20
    assert _cls43().y == 20
    assert _cls43.z == 30
    assert _cls43().z == 30


class _cls65:
    x = 10
    y = 20
    z = 30


def test_field_injector_correctly_injects_class_after_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects a \
    class after the ``y`` field."""

    @inject(target=_cls65, injector=FieldInjector('y', insert='after'))
    def handler():
        y = 25

    assert _cls65.x == 10
    assert _cls65().x == 10
    assert _cls65.y == 25
    assert _cls65().y == 25
    assert _cls65.z == 30
    assert _cls65().z == 30
