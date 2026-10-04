import importlib.util

spec = importlib.util.spec_from_file_location(
    "fibonacci_series",
    "Code/05_fibonacci_series.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

fib = module.fibonacci


def test_fibonacci():
    assert fib(1) == [0]
    assert fib(2) == [0, 1]
    assert fib(5) == [0, 1, 1, 2, 3]
    assert fib(7) == [0, 1, 1, 2, 3, 5, 8]
    assert fib(0) == []