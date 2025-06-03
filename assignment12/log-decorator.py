import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"

        result = func(*args, **kwargs)

        log_message = (
            f"function: {func_name}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n"
        )
        logger.log(logging.INFO, log_message)
        return result

    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def accept_args(*args):
    return True


@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


say_hello()
accept_args(1, 2, 3, "test")
return_decorator(a=1, b="hello", flag=True)
