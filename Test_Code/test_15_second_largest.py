import importlib.util

spec = importlib.util.spec_from_file_location(
    "second_largest",
    "Code/15_second_largest.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

second_largest = module.second_largest


def test_second_largest():
    assert second_largest([10, 20, 30]) == 20
    assert second_largest([5, 1, 4, 2]) == 4
    assert second_largest([10, 10, 5]) == 5
    assert second_largest([7]) is None