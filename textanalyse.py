def enter_text():
    return input("Please enter a text:\n> ")

def word_count(text):
    # Remove punctuation and make the text lowercase
    text = text.lower()
    for char in "-.,\n":
        text = text.replace(char, ' ')
    words = text.split()
    return len(words), words

def word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def longest_word(words):
    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

def average_word_length(words):
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def main_program():
    text = enter_text()
    word_count_result, words = word_count(text)
    frequency = word_frequency(words)
    max_word = longest_word(words)
    average_length = average_word_length(words)
    
    print("\nNumber of words:", word_count_result)
    print("Word frequency:")
    for word, count in frequency.items():
        print("  {}: {}".format(word, count))
    print("Longest word:", max_word)
    print("Average word length: {:.7f}".format(average_length))
   # print(f"Average word length: {average_length:.1f}")
  
# Call the main program
main_program()