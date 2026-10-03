import importlib.util

spec = importlib.util.spec_from_file_location(
    "even_odd",
    "Code/01_even_odd.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

even_odd = module.even_odd


assert even_odd(10) == "Even"
assert even_odd(7) == "Odd"
assert even_odd(0) == "Even"
assert even_odd(-4) == "Even"
assert even_odd(-5) == "Odd"

print("All test cases passed.")