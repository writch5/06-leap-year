
from leap_year import is_leap_year

test_cases = [
    [1944, True],
    [2011, False],
    [1986, False],
    [1956, True],
    [1957, False],
    [1800, False],
    [1900, False],
    [1600, True],
    [2056, True],
]

def test_leap_year_test_cases():
    for test_case in test_cases:
        is_leap_year_response = is_leap_year(test_case[0])
        assert is_leap_year_response == test_case[
            1], f'For {test_case[0]} Expected {test_case[1]}, got {is_leap_year_response}'
