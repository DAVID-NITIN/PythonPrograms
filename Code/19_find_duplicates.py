def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

if __name__ == "__main__":
    items = input("Enter items separated by spaces: ").split()
    print(find_duplicates(items))