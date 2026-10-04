import importlib.util

spec = importlib.util.spec_from_file_location(
    "pos_neg_zero",
    "Code/03_pos_neg_zero.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

cn = module.check_number


def test_number():
    assert cn(10) == "Positive"
    assert cn(-10) == "Negative"
    assert cn(0) == "Zero"