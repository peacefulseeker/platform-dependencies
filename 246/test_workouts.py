import pytest

from workouts import print_workout_days


@pytest.mark.parametrize("workout, expected", [
    ('cardio', 'Wed'),
    ('QWEQWEQWE', 'No matching workout'),
    ('lower', 'Tue, Fri'),
    ('UPPER', 'Mon, Thu'),
])
def test_print_workout_days(workout, expected, capsys):
    print_workout_days(workout)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
