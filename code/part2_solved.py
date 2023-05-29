from returns.pipeline import flow


def _sum_1(x: int) -> int:
    return x + 1


def _sum_2(x: int) -> int:
    return x + 2


def _sum_3(x: int) -> int:
    return x + 3


# TODO rewrite following usage in flow mode


def sum_all(x: int) -> int:
    sum1 = _sum_1(x)
    sum2 = _sum_2(sum1)
    sum3 = _sum_3(sum2)
    return sum3


def sum_all_with_flow(x: int) -> int:
    return flow(x, _sum_1, _sum_2, _sum_3)


if __name__ == '__main__':
    assert sum_all(5) == sum_all_with_flow(5)
