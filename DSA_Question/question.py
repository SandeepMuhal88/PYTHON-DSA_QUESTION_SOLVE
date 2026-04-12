def is_valid_parentheses(s):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Test
print(is_valid_parentheses("()"))  # → True
print(is_valid_parentheses("()[]{}"))  # → True
print(is_valid_parentheses("(]"))  # → False
print(is_valid_parentheses("([)]"))  # → False
print(is_valid_parentheses("{[]}"))  # → True
