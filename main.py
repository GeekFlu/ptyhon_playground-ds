# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest = None
    for num in in_list:
        if len(in_list) == 0:
            return None

        if num > 0:
            if smallest is None:
                smallest = num
            elif num < smallest:
                smallest = num

    return smallest


def when_offered(courses_in, course):
    offer = []
    for key_period in courses_in:
        if course in courses_in[key_period].keys():
            offer.append(key_period)
    return offer


if __name__ == '__main__':
    courses = {
        'spring2020': {'cs101': {'name': 'Building a Search Engine',
                                 'teacher': 'Dave',
                                 'assistant': 'Peter C.'},
                       'cs373': {'name': 'Programming a Robotic Car',
                                 'teacher': 'Sebastian',
                                 'assistant': 'Andy'}},
        'fall2020': {'cs101': {'name': 'Building a Search Engine',
                               'teacher': 'Dave',
                               'assistant': 'Sarah'},
                     'cs212': {'name': 'The Design of Computer Programs',
                               'teacher': 'Peter N.',
                               'assistant': 'Andy',
                               'prereq': 'cs101'},
                     'cs253': {'name': 'Web Application Engineering - Building a Blog',
                               'teacher': 'Steve',
                               'prereq': 'cs101'},
                     'cs262': {'name': 'Programming Languages - Building a Web Browser',
                               'teacher': 'Wes',
                               'assistant': 'Peter C.',
                               'prereq': 'cs101'},
                     'cs373': {'name': 'Programming a Robotic Car',
                               'teacher': 'Sebastian'},
                     'cs387': {'name': 'Applied Cryptography',
                               'teacher': 'Dave'}},
        'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                                 'teacher': 'Dorina'},
                       'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                                 'teacher': 'Jasper'},
                       }
    }
    # Test cases

    print(smallest_positive([4, -6, 7, 2, -4, 10]))
    # Correct output: 2

    print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
    # Correct output: 0.2

    print(smallest_positive([-6, -9, -7]))
    # Correct output: None

    print(smallest_positive([]))
    # Correct output: None

    print(when_offered(courses, 'cs101'))
    # Correct result:
    # ['fall2020', 'spring2020']

    print(when_offered(courses, 'bio893'))
    # Correct result:
    # []
