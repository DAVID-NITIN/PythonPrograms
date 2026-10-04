import importlib.util

spec = importlib.util.spec_from_file_location(
    "common_elements",
    "Code/17_common_elements.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

common_elements = module.common_elements


def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([1, 2], [3, 4]) == []
    assert common_elements([1, 1, 2], [1, 2]) == [1, 2]