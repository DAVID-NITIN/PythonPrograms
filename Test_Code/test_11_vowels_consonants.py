import importlib.util

spec = importlib.util.spec_from_file_location(
    "vowels_consonants",
    "Code/11_vowels_consonants.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

count_vowels_consonants = module.count_vowels_consonants


def test_vowels_consonants():
    assert count_vowels_consonants("hello") == (2, 3)
    assert count_vowels_consonants("aeiou") == (5, 0)
    assert count_vowels_consonants("xyz") == (0, 3)
    assert count_vowels_consonants("Hello World") == (3, 7)