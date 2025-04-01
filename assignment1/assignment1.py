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
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    # For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
    # split(' '), join(), and capitalize().
    # words[-1] gives the last element in the list.
    # The in comparison operator: You have seen in used in loops. But it can also be used for comparisons,
    # for example to check to see if a substring occurs in a string, or a value occurs in a list.
    # A new trick: As you loop through the words in the words list,
    # it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:
    words_list = string.split()
    last_word_index = len(words_list) - 1
    for index, word in enumerate(words_list):
        if index == 0 or index == last_word_index:
            word = word.capitalize()
            words_list[index] = word
        elif word in little_words:
            continue
        else:
            word = word.capitalize()
            words_list[index] = word
    return " ".join(words_list)


def hangman(secret, guess):
    result = ""
    guess_list = list(guess)
    for letter in secret:
        if letter in guess_list:
            result += letter
        else:
            result += "_"
    return result


# Pig Latin is a kid's trick language.
# Each word is modified according to the following rules.
# (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end.
# (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them.
# (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
# Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, returning the result.
# We will assume that there is no punctuation and that everything is lower case.


def pig_latin(sequence):
    vowels = "aeiou"
    vowels_list = [*vowels]
    words_list = sequence.split(" ")

    for key, word in enumerate(words_list):
        if word[0] in vowels_list:
            words_list[key] = word + "ay"
        else:
            pointer = 0
            tail = ""
            while pointer < len(word):
                letter = word[pointer]
                if letter in vowels_list:
                    break
                if (letter + word[pointer + 1]) == "qu":
                    tail += "qu"
                    pointer += 2
                    break
                else:
                    tail += letter
                    pointer += 1
            words_list[key] = word[pointer:] + tail + "ay"

    return " ".join(words_list)
