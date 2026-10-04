import importlib.util

spec = importlib.util.spec_from_file_location(
    "primes_in_range",
    "Code/07_primes_in_range.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

primes_in_range = module.primes_in_range


def test_primes_in_range():
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
    assert primes_in_range(10, 20) == [11, 13, 17, 19]
    assert primes_in_range(1, 2) == [2]