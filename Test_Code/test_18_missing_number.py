import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_missing_number = module.find_missing_number


def test_missing_number():
    assert find_missing_number([1, 2, 3, 5]) == 4
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([1, 3]) == 2
    assert find_missing_number([2, 3, 4, 5]) == 1