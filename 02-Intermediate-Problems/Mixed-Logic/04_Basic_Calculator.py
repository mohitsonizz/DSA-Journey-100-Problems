num1, num2 = 10, 5
op = '*'
ops = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Error"
}
print(ops.get(op, "Invalid Operator"))
