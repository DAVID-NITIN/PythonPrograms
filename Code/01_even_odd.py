def even_odd(number):
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = even_odd(number)
    print(f"{number} is {result}.")