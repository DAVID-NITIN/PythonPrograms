
def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)

if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers from 1 to n with one missing: ").split()))
    print(find_missing_number(numbers))