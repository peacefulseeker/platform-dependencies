import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "input_list, expected",
    [([0, 4, 2, 8], 428), ([1, 2], 12), ([3], 3), ([9, 9, 9], 999)],
)
def test_single_value(input_list, expected):
    assert list_to_decimal(input_list) == expected


def test_out_of_range():
    with pytest.raises(ValueError):
        list_to_decimal([10, 8])
    with pytest.raises(ValueError):
        list_to_decimal([1, 1222])
    with pytest.raises(ValueError):
        list_to_decimal([6, 2, -2])
    with pytest.raises(ValueError):
        list_to_decimal([-3, 1, 100])


def test_invalid_value_type():
    with pytest.raises(TypeError):
        list_to_decimal(["6", 9])
    with pytest.raises(TypeError):
        list_to_decimal([3, 1.1])
