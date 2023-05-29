from typing import Callable


def sum_3(x: int, y: int, z: int) -> int:
    return x + y + z

# TODO write the same currified implementation using lambda with type notation

sum_3_lambda = None

# TODO write the same currified implementation using standard function def with type notation

def sum_3_df(_: int):
    pass


if __name__ == '__main__':
    assert sum_3(1, 2, 3) == sum_3_lambda(1)(2)(3) == sum_3_df(1)(2)(3)

