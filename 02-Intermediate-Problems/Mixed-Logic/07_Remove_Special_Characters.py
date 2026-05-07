def remove_special_chars(s):
    result = ""
    for char in s:
        if char.isalnum():
            result += char
    return result


