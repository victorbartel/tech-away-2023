from random import randint

import uuid

from _pytest.monkeypatch import MonkeyPatch
from assertpy import assert_that
from box import Box

from workshop.railway.part3_solved import do_it

_SUT = do_it


def _raise(*_):
    raise Exception("Oops")


def test_do_it_when_everything_works():
    # Arrange
    id_ = randint(1, 10)
    data = Box({"fields": {"mandatory1": id_, "mandatory2": str(uuid.uuid4())}})
    # Act
    actual = _SUT(data)
    # Assert
    assert_that(actual).is_between(200, 220)


def test_do_it_when_mandatory1_is_missing():
    # Arrange
    id_ = randint(1, 10)
    data = Box({"fields": {"wrong": id_, "mandatory2": str(uuid.uuid4())}})
    # Act
    actual = _SUT(data)
    # Assert
    assert_that(actual).is_equal_to(-1)


def test_do_it_when_mandatory2_is_missing():
    # Arrange
    id_ = randint(1, 10)
    data = Box({"fields": {"mandatory1": id_, "wrong": str(uuid.uuid4())}})
    # Act
    actual = _SUT(data)
    # Assert
    assert_that(actual).is_equal_to(-1)


def test_do_it_when_something_unexpected_happens(monkeypatch: MonkeyPatch):
    # Arrange
    id_ = randint(1, 10)
    data = Box({"fields": {"mandatory1": id_, "mandatory2": str(uuid.uuid4())}})
    monkeypatch.setattr(uuid, uuid.uuid4.__name__, _raise)
    # Act
    actual = _SUT(data)
    # Assert
    assert_that(actual).is_equal_to(-0)
