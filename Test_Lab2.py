import Lab2
import mock

print("Test_Lab2")

def test_get_user_input():
    result = []
    input_arr = "1,3,5,8"
    test_arr = [1, 3, 5, 8]

    with mock.patch('builtins.input', return_value=input_arr):
        assert (Lab2.get_user_input() == test_arr)


def test_calc_average_temperature():
    result = []
    input_arr = [1, 3, 5, 8]
    test_arr = 4.25

    result = Lab2.calc_average_temperature(input_arr)

    assert (result == test_arr)

def test_calc_median_temperature():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = 25

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test_arr)