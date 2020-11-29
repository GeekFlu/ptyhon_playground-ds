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


def word_flipper(our_string):
    """
    Flip the individual words in place in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    words = our_string.split(" ")
    w_reversed = []
    for word in words:
        l = len(word) - 1
        wr = ''
        for i in range(len(word)):
            wr += word[l - i]
        w_reversed.append(wr)
    if len(w_reversed) == 1:
        return "".join(w_reversed)
    else:
        return " ".join(w_reversed)


def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    if len(str1) != len(str2):
        return None
    counter = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            counter += 1
    return counter


if __name__ == "__main__":
    print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
    print(
        "Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
    print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")

    print(
        '-------------------------------------------------------------------------------------------------------------')
    print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
    print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
    print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
    print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
    print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")

    print(
        '-------------------------------------------------------------------------------------------------------------')
    print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
    print("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
    print("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")

    # Test Cases
    print(
        '-------------------------------------------------------------------------------------------------------------')
    print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
    print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
    print("Pass" if (None == hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
    print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
    print("Pass" if (2 == hamming_distance('0101010100011101', '0101010100010001')) else "Fail")