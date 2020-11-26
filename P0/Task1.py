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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_telephone_numbers = set()

for telephone_text_record in texts:
    sending_number = telephone_text_record[0].strip()
    receiving_number = telephone_text_record[1].strip()
    unique_telephone_numbers.add(sending_number)
    unique_telephone_numbers.add(receiving_number)

for telephone_call_record in calls:
    sending_number = telephone_call_record[0].strip()
    receiving_number = telephone_call_record[1].strip()
    unique_telephone_numbers.add(sending_number)
    unique_telephone_numbers.add(receiving_number)

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")
