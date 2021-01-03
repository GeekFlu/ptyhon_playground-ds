from datastructures.Stack import Stack


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    s = Stack()
    if equation is None:
        return False
    if len(equation) <= 0:
        return False

    for letter in equation:
        if letter == '(':
            s.push(letter)
        elif letter == ')':
            if s.pop() is None:
                return False

    if s.size() == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    print(stack.arr)

    stack.push(1)
    assert stack.size() == 1
    print(stack.arr)

    stack.push(2)
    assert stack.size() == 2
    print(stack.arr)

    stack.push(3)
    assert stack.size() == 3
    print(stack.arr)

    for i in range(18):
        stack.push(i)
        print(stack.arr)

    for i in range(21):
        print(f"Pop value = {stack.pop()}")
    print(stack.arr)

    # if we pop one more an error should happen
    print(stack.pop())

    for i in range(18):
        stack.push(i)
        print(stack.arr)
    print(stack.pop())
    print(stack.arr)

    print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
