import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest_of_three", "Code/02_largest_of_three.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

largest_of_three = module.largest_of_three


def test_largest_of_three():
    assert largest_of_three(10, 20, 15) == 20
    assert largest_of_three(5, 3, 1) == 5
    assert largest_of_three(2, 8, 4) == 8
    assert largest_of_three(-1, -5, -3) == -1
    assert largest_of_three(7, 7, 5) == 7