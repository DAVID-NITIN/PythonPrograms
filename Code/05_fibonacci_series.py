def fibonacci(n):
    if n <= 0:
        return []

    series = [0, 1]

    if n == 1:
        return [0]

    for i in range(2, n):
        series.append(series[-1] + series[-2])

    return series


if __name__ == "__main__":
    n = int(input("Enter number of terms: "))
    print(fibonacci(n))