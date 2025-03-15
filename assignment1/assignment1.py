def hello():
    return "Hello!"


def greet(userName):
    return f"Hello, {userName}!"


def is_numeric_value(value):
    if type(value) == float or type(value) == int:
        return True
    else:
        return False


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
        return "You can't multiply those values!"
    else:
        return result
