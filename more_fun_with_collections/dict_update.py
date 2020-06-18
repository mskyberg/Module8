"""
Program: dict_update.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: demonstrate the use of dictionary functionality
"""


def get_test_scores():
    """
    Description: Get test scores from user input and store in dictionary

    :returns: dictionary of test scores
    :raises
    """
    # create an empty dictionary
    scores_dict = dict()
    try:
        # get number of scores to enter
        num_scores = int(input('Enter number of scores you wish to input:'))
        # loop to enter number of scores to dictionary
        for test in range(num_scores):
            score = int(input('Enter Test Score:'))
            scores_dict.update({f'Test {test}': score})
    except ValueError as e:
        raise ValueError(f'{e}')
    else:
        return scores_dict


def average_scores(a_dict):
    """
    Description: Average the values of a dictionary

    :param a_dict: a dictionary of scores
    :returns: the average scores
    :raises keyError: raises an exception
    """
    total_score = 0
    # loop through the values and add to total score
    for score in a_dict.values():
        total_score += score

    return total_score / len(a_dict)


if __name__ == '__main__':
    try:
        scores = get_test_scores()
        print(scores)
        print(average_scores(scores))
    except ValueError as err:
        print(f'Input Error: {err}')
