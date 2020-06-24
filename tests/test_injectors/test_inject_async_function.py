"""Tests to make sure that async functions are injected as expected."""

try:
    from asyncio import run
except ImportError:
    import asyncio

    def run(main):
        """Run an async function."""
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(main)


from injectify.api import inject
from injectify.injectors import (
    HeadInjector,
    TailInjector,
    ReturnInjector,
    FieldInjector,
    NestedInjector,
)


def test_head_injector_correctly_injects_async_function():
    """Test :class:`~injectify.injectors.HeadInjector` correctly injects an \
    async function."""  # noqa: D202

    async def target(x):
        a = 10
        if x > a:
            a = x
        return a

    @inject(target=target, injector=HeadInjector())
    def handler():
        x = 11

    assert run(target(0)) == 11
    assert run(target(10)) == 11
    assert run(target(101)) == 11


def test_tail_injector_correctly_injects_async_function():
    """Test :class:`~injectify.injectors.TailInjector` correctly injects an \
    async function."""  # noqa: D202

    async def target(x):
        if x > 100:
            return x

    @inject(target=target, injector=TailInjector())
    def handler():
        return -1

    assert run(target(13)) == -1
    assert run(target(101)) == 101


def test_return_injector_correctly_injects_async_function_all_returns():
    """Test :class:`~injectify.injectors.ReturnInjector` correctly injects an \
    async function before all return statements."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
            return y
        else:
            y = x + 2
            return y

    @inject(target=target, injector=ReturnInjector())
    def handler():
        return '{} :)'.format(y)

    assert run(target(13)) == '15 :)'
    assert run(target(101)) == '202 :)'


def test_return_injector_correctly_injects_async_function_ordinal_returns():
    """Test :class:`~injectify.injectors.ReturnInjector` correctly injects an \
    async function before an ordinal return statement."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
            return y
        else:
            y = x + 2
            return y

    @inject(target=target, injector=ReturnInjector(ordinal=1))
    def handler():
        return '{} :)'.format(y)

    assert run(target(13)) == '15 :)'
    assert run(target(101)) == 202


def test_field_injector_correctly_injects_async_function_before_all_fields():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects an \
    async function before all ``y`` fields."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
        else:
            y = x + 2
        return y

    @inject(target=target, injector=FieldInjector('y', insert='before'))
    def handler():
        x += 1

    assert run(target(13)) == 16
    assert run(target(101)) == 204


def test_field_injector_correctly_injects_async_function_after_all_fields():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects an \
    async function after all ``y`` fields."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
        else:
            y = x + 2
        return y

    @inject(target=target, injector=FieldInjector('y', insert='after'))
    def handler():
        y -= 1

    assert run(target(13)) == 14
    assert run(target(101)) == 201


def test_field_injector_correctly_injects_async_function_before_ordinal_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects an \
    async function before an ordinal ``y`` field."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
        else:
            y = x + 2
        return y

    @inject(
        target=target, injector=FieldInjector('y', ordinal=1, insert='before'),
    )
    def handler():
        x += 1

    assert run(target(13)) == 16
    assert run(target(101)) == 202


def test_field_injector_correctly_injects_async_function_after_ordinal_field():
    """Test :class:`~injectify.injectors.FieldInjector` correctly injects an \
    async function after an ordinal ``y`` field."""  # noqa: D202

    async def target(x):
        if x > 100:
            y = x * 2
        else:
            y = x + 2
        return y

    @inject(target=target, injector=FieldInjector('y', ordinal=0, insert='after'))
    def handler():
        y -= 1

    assert run(target(13)) == 15
    assert run(target(101)) == 201


def test_nested_injector_correctly_injects_async_function_sync_nested():
    """Test :class:`~injectify.injectors.NestedInjector` correctly injects an \
    async function with a non-async nested function."""  # noqa: D202

    async def target(x):
        def nested(y):
            if y > 100:
                return y

        if x < 200:
            return nested(x)

    @inject(target=target, injector=NestedInjector('nested', TailInjector()))
    def handler():
        return -1

    assert run(target(13)) == -1
    assert run(target(101)) == 101
    assert run(target(200)) is None


def test_nested_injector_correctly_injects_async_function_async_nested():
    """Test :class:`~injectify.injectors.NestedInjector` correctly injects an \
    async function with a nested async function."""  # noqa: D202

    async def target(x):
        async def nested(y):
            if y > 100:
                return y

        if x < 200:
            return await nested(x)

    @inject(target=target, injector=NestedInjector('nested', TailInjector()))
    def handler():
        return -1

    assert run(target(13)) == -1
    assert run(target(101)) == 101
    assert run(target(200)) is None


def test_nested_injector_correctly_injects_nested_sync_function_async_nested():
    """Test :class:`~injectify.injectors.NestedInjector` correctly injects a \
    non-async function with a nested async function."""  # noqa: D202

    def target(x):
        async def nested(y):
            if y > 100:
                return y

        if x < 200:
            return run(nested(x))

    @inject(target=target, injector=NestedInjector('nested', TailInjector()))
    def handler():
        return -1

    assert target(13) == -1
    assert target(101) == 101
    assert target(200) is None
