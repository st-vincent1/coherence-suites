import argparse
import sys
import numpy as np


def interpret_bias_scores(scores, type):
    """
    Given scores as a list of strings (e.g. ['-0.3', '-0.1'], computes the bias of the model towards a certain context.
    The scores are produced according to a pre-established process and are expected to be in the following format:
    type=spg -> Female \n Male \n ...
    type=for -> Formal \n Informal \n ...
    :param scores: list of strings - scores
    :param type: type of test suite: spg, ilg, iln, for
    :return:
    """
    type_counts = {
        'spg': 2,
        'ilg': 4,
        'for': 2,
        'iln': 2
    }
    variations_n = type_counts[type]
    bias_table = np.zeros(variations_n)
    for i in range(0, len(scores), variations_n):
        winner = np.argmax(np.array(scores[i:i + variations_n]))
        bias_table[winner] += 1
    bias = 100 * bias_table / (len(scores) / variations_n)
    print(f"Bias: {bias}")
    return bias


def interpret_scores(scores, type):
    """
    Given scores as a list of strings (e.g. ['-0.3', '-0.1'], computes the accuracy of the model.
    The scores are produced according to a pre-established process and are expected to be in the following format:
    Score for correct setting
    Score for incorrect setting\n * 1-3 (depending on suite)
    Score for correct setting
    Score for incorrect setting\n * 1-3 (depending on suite)
    ...
    :param scores: list of strings - scores
    :param type: type of test suite: spg, ilg, iln, for
    :return:
    """
    tests_passed = 0
    tests_failed = 0
    type_counts = {
        'spg': 2,
        'ilg': 4,
        'for': 2,
        'iln': 2
    }
    variations_n = type_counts[type]
    for i in range(0, len(scores), variations_n):
        valid_score = float(scores[i])
        invalid_score = max([float(scores[t]) for t in range(i + 1, i + variations_n)])
        if valid_score > invalid_score:
            tests_passed += 1
        else:
            tests_failed += 1
        tests_passed += int(valid_score > invalid_score)
        tests_failed += int(valid_score <= invalid_score)

    accuracy = tests_passed / (tests_passed + tests_failed)
    print(f"Accuracy: {accuracy} | {tests_passed / 2} passed out of {(tests_passed + tests_failed) / 2} examples.")
    return accuracy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='File with test suite scores', required=True)
    parser.add_argument('-t', '--type',
                        help='Type of test suite. \nspg - speaker gender\nilg - interlocutor gender and number\nfor - '
                             'formality',
                        required=True)
    args = vars(parser.parse_args())
    try:
        f = open(args['file'], 'r')
    except FileNotFoundError:
        print("No file under the specified path.")
        sys.exit(0)
    if type not in ['spg', 'ilg', 'iln', 'for']:
        print("Invalid type.")
        sys.exit(0)

    scores = f.read().splitlines()
    accuracy = interpret_scores(scores, args['type'])


if __name__ == '__main__':
    main()
