
from typing import Any, Callable


def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
        print("start")
        return fn(*args, **kwargs)
    return inner


@wrapper
def do_it(a: int, b: int) -> int:
    return a + b


# wrapped_do_it = wrapper(do_it)
print(do_it(1, 2))


@wrapper
def do_it2(a: int, b: int) -> int:
    return a - b


# wrapped_do_it = wrapper(do_it2)
print(do_it2(1, 2))
