import random

from returns.pipeline import flow

_BIAS = random.randint(1, 100)


def _sum_1(bias: int, x: int) -> int:
    return (x + 1) * bias


def _sum_2(bias: int, x: int) -> int:
    return (x + 2) * bias


def _sum_3(bias: int, x: int) -> int:
    return (x + 3) * bias


# TODO rewrite following usage in flow mode


def sum_all(bias: int, x: int) -> int:
    sum1 = _sum_1(bias, x)
    sum2 = _sum_2(bias, sum1)
    sum3 = _sum_3(bias, sum2)
    return sum3


def sum_all_with_flow(bias: int, x: int) -> int:
    # TODO here ....
    pass


if __name__ == "__main__":
    assert sum_all(_BIAS, 5) == sum_all_with_flow(_BIAS, 5)
