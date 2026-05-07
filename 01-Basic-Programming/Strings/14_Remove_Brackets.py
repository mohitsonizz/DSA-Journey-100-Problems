text = "(Hello) [World] {Python}"
table = str.maketrans('', '', '()[]{}')
print(text.translate(table))

