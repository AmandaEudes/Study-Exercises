from pytest import raises

from study_exercises.binary_search import binary_search


def test_one() -> None:
    assert 4 == binary_search([4, 8, 12, 16, 23, 28, 32], 23)


def test_two() -> None:
    with raises(ValueError, match="value not in array"):
        binary_search([4, 8, 12, 16, 23, 28, 32], 10)


def test_three() -> None:
    assert 0 == binary_search([4, 8, 12, 16, 23, 28, 32], 4)


def test_four() -> None:
    assert 6 == binary_search([4, 8, 12, 16, 23, 28, 32], 32)
