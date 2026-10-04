import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_number",
    "Code/08_reverse_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_number = module.reverse_number


def test_reverse_number():
    assert reverse_number(12345) == 54321
    assert reverse_number(100) == 1
    assert reverse_number(7) == 7
    assert reverse_number(-123) == -321