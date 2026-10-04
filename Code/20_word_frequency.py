def word_frequency(text):
    frequency = {}
    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(word_frequency(text))