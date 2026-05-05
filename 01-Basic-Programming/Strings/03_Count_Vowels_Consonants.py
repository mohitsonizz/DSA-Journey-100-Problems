s = "mohit soni"
vowels = sum(1 for char in s if char.lower() in "aeiou")
consonants = sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")
