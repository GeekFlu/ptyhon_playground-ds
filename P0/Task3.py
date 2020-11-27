"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Ban   galore."
The percentage should have 2 decimal digits
"""


def is_mobile_number(telephone_number):
    """
    Function to determine if a number is a mobile number
    :param telephone_number:
    :return: None if it is not a mobile number otherwise the number
    """
    index_space = telephone_number.find(" ", 0)
    if index_space > -1:
        if telephone_number.find("7", 0, 1) > -1 or telephone_number.find("8", 0, 1) > -1 \
                or telephone_number.find("9", 0, 1) > -1:
            return telephone_number[0: 4]
    return None


def is_telemarketer_number(telephone_number):
    """
    Function to determine if a Telephone number is Telemarketer
    :param telephone_number:
    :return: Telemarketer Prefix
    """
    if telephone_number.find("140", 0, 3) > -1:
        return "140"
    return None


def is_fixed_line_number(telephone_number):
    """
    Function to determine if a number is a fixed line
    :param telephone_number:
    :return: Code for the fixed line
    """
    open_p = telephone_number.find("(", 0, 1)
    close_p = telephone_number.find(")", 0)
    if open_p > -1 and close_p > -1:
        return telephone_number[open_p: close_p + 1]
    return None


if __name__ == "__main__":
    telephone_codes = set()
    for call_record in calls:
        caller = call_record[0]
        receiver = call_record[1]
        # Part A
        if caller.find("(080)", 0) > -1:
            mobile_number = is_mobile_number(receiver)
            tkm_marketer = is_telemarketer_number(receiver)
            fixed_line = is_fixed_line_number(receiver)
            if mobile_number is not None:
                telephone_codes.add(mobile_number)
            elif tkm_marketer is not None:
                telephone_codes.add(tkm_marketer)
            elif fixed_line is not None:
                telephone_codes.add(fixed_line)

    lst_telephone_codes = list(telephone_codes)
    lst_telephone_codes.sort()
    print(f"The numbers called by people in Bangalore have codes: ")
    for code in lst_telephone_codes:
        print(code)
