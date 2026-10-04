import importlib.util

spec = importlib.util.spec_from_file_location(
    "sum_of_digits",
    "Code/10_sum_of_digits.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

sum_of_digits = module.sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(1234) == 10
    assert sum_of_digits(555) == 15
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-123) == 6