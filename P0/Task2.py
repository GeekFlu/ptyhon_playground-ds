"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def extract_date(date):
    """
    Given a date with format dd-MM-yyyy hh:mm:ss, this function will return
    dd, mm, yyyy
    :param date:
    :return: tuple day, month, year
    """
    return date[0:2], date[3:5], date[6:10]


def update_telephone_dict(telephone_dictionary, telephone_key, spent_time):
    if telephone_dictionary.get(month) is None:
        telephone_dictionary[month] = {}
        telephone_dictionary[month][telephone_key] = spent_time
        time_count = spent_time
    elif telephone_dictionary.get(month).get(telephone_key) is None:
        telephone_dictionary[month][telephone_key] = spent_time
        time_count = spent_time
    else:
        telephone_dictionary[month][telephone_key] = telephone_dictionary.get(month).get(telephone_key) + spent_time
        time_count = telephone_dictionary.get(month).get(telephone_key) + spent_time
    return time_count


months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

directory_stats = dict()
max_seconds = -1
telephone = ''
m_month = ''

for call_record in calls:
    day, month, year = extract_date(call_record[2])
    # first as caller
    max_spent_time = update_telephone_dict(directory_stats, call_record[0], int(call_record[3]))
    if max_spent_time > max_seconds:
        max_seconds = max_spent_time
        telephone = call_record[0]
        m_month = month

    # then as a receiver
    max_spent_time = update_telephone_dict(directory_stats, call_record[1], int(call_record[3]))
    if max_spent_time > max_seconds:
        max_seconds = max_spent_time
        telephone = call_record[1]
        m_month = month

print(f"{telephone} spent the longest time, {directory_stats.get(m_month).get(telephone)} seconds, on the phone during September 2016.")
