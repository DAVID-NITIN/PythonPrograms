import importlib.util

spec = importlib.util.spec_from_file_location(
    "factorial",
    "Code/04_factorial.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

fact = module.factorial


def test_factorial():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(7) == 5040
    assert fact(-1) == "Invalid input"