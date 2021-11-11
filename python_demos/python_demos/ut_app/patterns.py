""" patterns """

from typing import Callable


def console_log(msg: str) -> None:
    print(msg)


# unconstrained mocking/testing
# legacy code
def action_a() -> None:
    console_log("action a")


# constrained mocking/testing
# modern code
def action_b(log: Callable[..., None]) -> None:
    log("action b")
