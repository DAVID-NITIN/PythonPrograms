import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime_number",
    "Code/06_prime_number.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_prime = module.is_prime


def test_prime_number():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert is_prime(1) is False
    assert is_prime(0) is False