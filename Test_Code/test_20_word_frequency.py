import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

word_frequency = module.word_frequency


def test_word_frequency():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}
    assert word_frequency("Python Python code") == {"python": 2, "code": 1}
    assert word_frequency("") == {}