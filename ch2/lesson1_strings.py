def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    reversed_ = ''
    l = len(our_string) - 1
    for i in range(len(our_string)):
        reversed_ += our_string[l - i]
    print(reversed_)
    return reversed_


# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    s1 = str1.replace(' ', '')
    s2 = str2.replace(' ', '')
    if len(s1) != len(s2):
        return False

    s1 = s1.lower()
    s2 = s2.lower()

    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 != s2:
        return False

    return True


if __name__ == "__main__":
    print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
    print(
        "Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
    print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")

    print('-------------------------------------------------------------------------------------------------------------')
    print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
    print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
    print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
    print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
    print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")