import importlib.util

spec = importlib.util.spec_from_file_location(
    "find_duplicates",
    "Code/19_find_duplicates.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates


def test_find_duplicates():
    assert find_duplicates([1, 2, 2, 3, 3]) == [2, 3]
    assert find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]
    assert find_duplicates([1, 2, 3]) == []