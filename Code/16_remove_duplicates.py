def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

if __name__ == "__main__":
    items = input("Enter items separated by spaces: ").split()
    print(remove_duplicates(items))
