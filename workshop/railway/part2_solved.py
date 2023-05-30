import random
import uuid
from dataclasses import dataclass
from typing import Callable, Any

from box import Box
from returns.curry import curry
from returns.functions import tap
from returns.pipeline import flow
from returns.pointfree import bind
from returns.result import safe, Success, Failure, ResultE


class NoMandatory1Exception(Exception):
    pass


class NoMandatory2Exception(Exception):
    pass


@dataclass
class ValidData:
    mandatory_field1: int
    mandatory_field2: str


@dataclass
class UpdatedData:
    mandatory_field1: int
    mandatory_field3: str


@safe
def _validate(data: Box) -> Box:
    if "mandatory1" not in data.fields:
        raise NoMandatory1Exception("Oops 1")
    if "mandatory2" not in data.fields:
        raise NoMandatory1Exception("Oops 2")
    return data


@safe
def _map(data: Box) -> ValidData:
    return ValidData(int(data.fields.mandatory1), str(data.fields.mandatory2))


@curry
@safe
def _update(data: ValidData, log: Callable[[Any], Any]) -> UpdatedData:
    log(f"Do some DB magic here with {data}")
    return UpdatedData(data.mandatory_field1, str(uuid.uuid4()))


@safe
def _log(x: ValidData) -> None:
    print(f"Start writing data with {x}")


@curry
@safe
def _send(data: UpdatedData, log: Callable[[Any], Any]) -> int:
    log(data)
    return random.randint(200, 220)


def do_it(data: Box) -> int:
    result: ResultE[int] = flow(
        data,
        _validate,
        bind(_map),
        tap(_log),
        bind(_update(log=print)),
        bind(_send(log=print)),
    )
    match result:
        case Success(x):
            return x
        case Failure(NoMandatory1Exception()):
            return -1
        case Failure(NoMandatory2Exception()):
            return -2
        case Failure(err):
            print(f"Truly oops {err}")
            return 0
