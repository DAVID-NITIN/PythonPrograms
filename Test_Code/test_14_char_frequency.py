import importlib.util

spec = importlib.util.spec_from_file_location(
    "char_frequency",
    "Code/14_char_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

character_frequency = module.character_frequency


def test_char_frequency():
    assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert character_frequency("aaa") == {"a": 3}
    assert character_frequency("") == {}