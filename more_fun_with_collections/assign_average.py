"""
Program: assign_average.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: demonstrate the use of selection using a Dictionary
"""


def get_switch_value(letter_grade):
    """
    Description: Get the numeric value of letter grade

    :param letter_grade: this is what the first parameter represents
    :returns: value of letter grade
    :raises ValueError: raises an exception if letter not found
    """
    grade_dict = {'A': 90, 'a': 90,
                  'B': 80, 'b': 80,
                  'C': 70, 'c': 70,
                  'D': 60, 'd': 60,
                  'F': 50, 'f': 50}

    # I feel like this is a better solution but going to try and match instructions
    # if letter_grade in grade_dict:
    #     return grade_dict[letter_grade]
    # else:
    #     raise ValueError(f'Grade does not exist: {letter_grade}')
    if letter_grade == 'A' or letter_grade == 'a':
        return grade_dict[letter_grade]
    elif letter_grade == 'B' or letter_grade == 'b':
        return grade_dict[letter_grade]
    elif letter_grade == 'C' or letter_grade == 'c':
        return grade_dict[letter_grade]
    elif letter_grade == 'D' or letter_grade == 'd':
        return grade_dict[letter_grade]
    elif letter_grade == 'F' or letter_grade == 'f':
        return grade_dict[letter_grade]
    else:
        raise ValueError(f'Grade does not exist: {letter_grade}')


def switch_average(grades):
    """
    Description: Calculate the average of list of letter grades

    :param grades: list of letter grades to calculate average on
    :returns: average grade
    :raises
    """
    pass


if __name__ == '__main__':
    try:
        print(get_switch_value('E'))
    except ValueError as err:
        print(f'Input Error: {err}')
