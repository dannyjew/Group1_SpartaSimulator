def is_int(question, answer):
    while not answer.isnumeric() or int(answer) < 0:
        answer = input(question)
        if not answer.isnumeric() or int(answer) < 0:
            print("Invalid input, please enter a positive integer\n")
    return answer


def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)
