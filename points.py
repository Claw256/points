# !/bin/env python3

"""
This is Fearghal's QQI credits to CAO points calculator.
"""

__author__ = 'Fearghal Hayes'
__date__ = '24 March 2020'
__credits__ = 'Me, myself, and I :)'
__version__ = '0.0.1'


def get_positive_integer(prompt):
    """
    Requests a positive integer from the user, repeating the prompt until valid input is provided.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("ERROR: Please only use positive numbers, not zero or negative numbers")
        except ValueError:
            print("ERROR: This is not a number, please input only numbers, nothing else")


def calculate_qqi_score(credit, score):
    """Calculates and returns the QQI score based on credit and score."""
    return int(credit * score * 13 / 12)


def main():
    print("\nWelcome to Fearghal's QQI Calculator for Points (FQCP)")

    loop_counter = 0
    module_credit_total = 0
    qqi_score_total = 0

    while module_credit_total <= 120 and qqi_score_total < 390 and loop_counter < 8:
        module_credit_input = get_positive_integer("\nPlease input your credit weighting for your Module:\n\n")
        module_score_input = get_positive_integer(
            "\nPlease input your marking for your QQI Module (3 for Distinction, 2 for Merit, and 1 for Pass):\n\n")

        module_credit_total += module_credit_input
        if module_credit_total > 120:
            print("You have exceeded your module credit total")
            print("You get NOTHING! You LOSE! Good day sir.")
            break

        qqi_score = calculate_qqi_score(module_credit_input, module_score_input)
        qqi_score_total += qqi_score

        if qqi_score_total >= 390:
            qqi_score_total = min(qqi_score_total, 390)
            print("\nYou achieved 390 CAO points. Congrats! You got full marks.")
            break

        print("\nYour total QQI score is:", qqi_score_total)
        loop_counter += 1

    if loop_counter >= 8:
        print("You have exceeded your maximum QQI module count")

    if qqi_score_total > 390:
        print("You have exceeded your CAO score total")
        print("You get NOTHING! You LOSE! Good day sir.")

    print("\nThank you for using FQCP")


if __name__ == "__main__":
    main()
