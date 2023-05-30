import random
import uuid
from dataclasses import dataclass
from typing import Callable, Any

from box import Box


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


def _validate(data: Box) -> Box:
    if not data.fields.mandatory1:
        raise NoMandatory1Exception("Oops 1")
    if not data.fields.mandatory2:
        raise NoMandatory1Exception("Oops 2")
    return data


def _map(data: Box) -> ValidData:
    return ValidData(int(data.fields.mandatory1), str(data.fields.mandatory2))


def _update(data: ValidData, log: Callable[[Any], Any]) -> UpdatedData:
    log(f"Do some DB magic here with {data}")
    return UpdatedData(data.mandatory_field1, str(uuid.uuid4()))


def _send(data: UpdatedData, log: Callable[[Any], Any]) -> int:
    log(data)
    return random.randint(200, 220)


def do_it(data: Box) -> int:
    try:
        valid = _validate(data)
        mapped = _map(valid)
        print(f"Start writing data with {mapped}")
        updated = _update(mapped, print)
        sent = _send(updated, print)
        return sent
    except NoMandatory1Exception as mex1:
        print(f"Your mex1 {mex1}")
        return -1
    except NoMandatory2Exception as mex2:
        print(f"Your mex2 {mex2}")
        return -2
    except Exception as ex:
        print(f"Truly oops {ex}")
        return -0
