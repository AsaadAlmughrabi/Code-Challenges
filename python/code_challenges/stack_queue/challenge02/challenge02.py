def is_valid(s):
    """Check if the input string of brackets is valid."""
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            continue

    return not stack  # If the stack is empty, all brackets are closed properly
def is_valid(s):
    """Check if the input string of brackets is valid."""
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            continue

    return not stack  # If the stack is empty, all brackets are closed properly

if __name__ == "__main__":
    
    print("Test case '()':", is_valid("()"))
    print("Test case '()[]{}':", is_valid("()[]{}"))
    print("Test case '[({}]':", is_valid("[({}]"))
    print("Test case '[(hello)()]':", is_valid("[(hello)()]"))
    print("Test case '[{(())}]':", is_valid("[{(())}]"))
