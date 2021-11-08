
from typing import Any, Callable

# class Flask:

#     def __init__(self):

#         self.routes = []

#     def route(self, path: str) -> Callable[..., Any]:
#         def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
#             self.routes.append({"path": path, "fn": fn})
#         return wrapper

#     def request_received(path: str):
#         ...


def param_wrapper(msg: str) -> Callable[..., Any]:
    def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
            print(msg)
            return fn(*args, **kwargs)
        return inner
    return wrapper


msg_of_hope = "python is cool"


@param_wrapper(msg_of_hope)
def do_it(a: int, b: int) -> int:
    return a + b


# wrapped_do_it = wrapper(do_it)
print(do_it(1, 2))


@param_wrapper("python programmers are cooler")
def do_it2(a: int, b: int) -> int:
    return a - b


# wrapped_do_it = wrapper(do_it2)
print(do_it2(1, 2))
