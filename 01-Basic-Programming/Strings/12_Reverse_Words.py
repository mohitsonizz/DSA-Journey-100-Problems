def reverse_words(sentence):
    words = sentence.split()
    reversed_list = words[::-1]
    return " ".join(reversed_list)

