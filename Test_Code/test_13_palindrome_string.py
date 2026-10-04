import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

is_palindrome_string = module.is_palindrome_string


def test_palindrome_string():
    assert is_palindrome_string("madam") is True
    assert is_palindrome_string("racecar") is True
    assert is_palindrome_string("hello") is False
    assert is_palindrome_string("A man a plan a canal Panama") is True