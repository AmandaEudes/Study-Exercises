from pytest import raises

from study_exercises.fibonacci_numbers import fibonacci_numbers, sum_even_numbers


def test_one_fibonacci_numbers() -> None:
    assert [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] == fibonacci_numbers(100)


def test_two_fibonacci_numbers() -> None:
    assert [
        1,
        2,
        3,
        5,
        8,
        13,
        21,
        34,
        55,
        89,
        144,
        233,
        377,
        610,
        987,
        1_597,
        2_584,
        4_181,
        6_765,
        10_946,
        17_711,
        28_657,
        46_368,
        75_025,
        121_393,
        196_418,
        317_811,
        514_229,
        832_040,
        1_346_269,
        2_178_309,
        3_524_578,
    ] == fibonacci_numbers(4_000_000)


def test_three_fibonacci_numbers() -> None:
    with raises(ValueError, match="Only positive integers are allowed"):
        fibonacci_numbers(-1)


def test_four_fibonacci_numbers() -> None:
    assert [1] == fibonacci_numbers(1)
    assert [1, 2] == fibonacci_numbers(2)


def test_five_fibonacci_numbers() -> None:
    assert 44 == sum_even_numbers(fibonacci_numbers(100))


def test_six_fibonacci_numbers() -> None:
    assert 4_613_732 == sum_even_numbers(fibonacci_numbers(4_000_000))
