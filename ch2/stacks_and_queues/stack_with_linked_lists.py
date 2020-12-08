from datastructures.StackLL import Stack


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
    s_ = Stack()
    s_.push(1)
    s_.push(2)
    s_.push(3)
    print(s_.pop())
    print(s_.pop())
    print(s_.pop())
    print(s_.pop())

    for i in range(1000):
        s_.push(i)

    for i in range(999):
        s_.pop()

    assert s_.size() == 1
    print(s_.pop())

    print("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
