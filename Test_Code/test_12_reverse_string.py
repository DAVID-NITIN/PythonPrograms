import importlib.util

spec = importlib.util.spec_from_file_location(
    "reverse_string",
    "Code/12_reverse_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

reverse_string = module.reverse_string


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""