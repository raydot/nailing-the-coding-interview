def is_balanced(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

print(is_balanced("((()))")) # True
print(is_balanced("(()))")) # False