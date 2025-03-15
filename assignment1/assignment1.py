def hello():
    return "Hello!"


def greet(userName):
    return f"Hello, {userName}!"


def is_numeric_value(value):
    return isinstance(value, float | int)


def calc(a, b, operator="multiply"):
    try:
        if is_numeric_value(a) and is_numeric_value(b):
            match operator:
                case "multiply":
                    result = a * b
                case "add":
                    result = a + b
                case "divide":
                    result = a / b
                case "subtract":
                    result = a - b
                case "modulo":
                    result = a % b
        else:
            raise ValueError
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except ValueError:
        return f"You can't {operator} those values!"
    else:
        return result


def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                result = int(value)
            case "float":
                result = float(value)
            case "str":
                result = str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
    else:
        return result


def grade(*args):
    try:
        score = sum(args) / len(args)
        if score >= 90:
            result = "A"
        elif score >= 80:
            result = "B"
        elif score >= 70:
            result = "C"
        elif score >= 60:
            result = "D"
        else:
            result = "F"
    except TypeError:
        return "Invalid data was provided."
    else:
        print(f"avg score: {score}")
        return result


def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
        print(result)
    return result


def student_scores(param, **kwargs):
    if param == "best":
        highest_score = 0
        best_student = "Vlad"
        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best_student = key
        return best_student
    if param == "mean":
        return sum(kwargs.values()) // len(kwargs)


def titleize(string):
    # title = ''
    # (1) The first word is always capitalized.
    # (2) The last word is always capitalized.
    # (3) All the other words are capitalized, except little words.

    # For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
    # split(' '), join(), and capitalize().
    # words[-1] gives the last element in the list.

    # The in comparison operator: You have seen in used in loops. But it can also be used for comparisons,
    # for example to check to see if a substring occurs in a string, or a value occurs in a list.
    # A new trick: As you loop through the words in the words list,
    # it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:
    return
