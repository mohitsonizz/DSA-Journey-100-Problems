def capitalize_first_letter(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        result.append(new_word)
        
    return " ".join(result)

