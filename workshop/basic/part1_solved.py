from typing import Callable


def sum_3(x: int, y: int, z: int) -> int:
    return x + y + z

# TODO write the same currified implementation using lambda with type notation

sum_3_lambda: Callable[[int], Callable[[int], Callable[[int], int]]] = lambda x : lambda y : lambda z: x + y + z

# TODO write the same currified implementation using standard function def with type notation

def sum_3_df(x: int) -> Callable[[int], Callable[[int], int]]:
    def sub_sum_yz(y: int) -> Callable[[int], int]:
        def sub_sum_z(z: int) -> int:
            return x + y + z
        return sub_sum_z
    return sub_sum_yz


if __name__ == '__main__':
    assert sum_3(1, 2, 3) == sum_3_lambda(1)(2)(3) == sum_3_df(1)(2)(3)