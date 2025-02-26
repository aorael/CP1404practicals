"""
Word Occurrences
Estimate: 35 minutes
Actual:   42 minutes
"""
from operator import itemgetter
word_to_length = {}

def main():
    """Counting the number of words appeared in a text"""
    text = input("Text: ")
    words = text.split(" ")
    sorted_words = get_sorted_word_to_length(words)

    word_width = max(len(pair[0]) for pair in sorted_words)
    number_of_word_width = max(len(str(pair[1])) for pair in sorted_words)

    display_data(number_of_word_width, sorted_words, word_width)

    # print(words) #LIST
    # print(word_to_length) #UNSORTED DICTIONARY
    # print(sorted_words) #SORTED LISTS

def display_data(number_of_word_width, sorted_words, word_width):
    """Displaying all the data"""
    for word, number_of_word in sorted_words:
        print(f"{word:{word_width}} : {number_of_word:{number_of_word_width}}")

def get_sorted_word_to_length(words):
    """Converting a list to a dictionary with sorted words as the key and number of words as the value"""
    for word in words:
        word_to_length[word] = word_to_length.get(word, 0) + 1
    sorted_words = sorted(word_to_length.items(), key=itemgetter(0))
    return sorted_words

main()