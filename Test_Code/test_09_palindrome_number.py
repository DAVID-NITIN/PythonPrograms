import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome = module.is_palindrome


def test_palindrome_number():
    assert is_palindrome(121) is True
    assert is_palindrome(12321) is True
    assert is_palindrome(123) is False
    assert is_palindrome(10) is False
    assert is_palindrome(-121) is False