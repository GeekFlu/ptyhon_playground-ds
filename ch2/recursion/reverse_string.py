def reverse_string(input_str):
    """
    Return reversed input string
    Examples:
       reverse_string("abc") returns "cba"
    Args:
      input_str(str): string to be reversed
    Returns:
      a string that is the reverse of input
    """
    if len(input_str) == 0:
        return ""
    else:
        first_char = input_str[0]
        the_rest = input_str[1:len(input_str)]
        reversed_str = reverse_string(the_rest)
        return reversed_str + first_char


if __name__ == "__main__":
    print("Pass" if ("siul" == reverse_string("luis")) else "Fail")
    print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
    print("Pass" if ("" == reverse_string("")) else "Fail")
