def reverse_text(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def is_palindrome_string(text):
    cleaned = ""
    for char in text.lower():
        if char.isalnum():
            cleaned += char
    return cleaned == reverse_text(cleaned)

if __name__ == "__main__":
    text = input("Enter a string: ")
    print(is_palindrome_string(text))