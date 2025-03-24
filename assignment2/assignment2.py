import os
import csv
import traceback

path = os.path.join(os.getcwd(), "assignment2/dairy.txt")

first_prompt = "What happened today? "
second_prompt = "What else? "
closing_prompt = "done for now"

is_chat_started = False
is_conversation_open = True
print(path)


def writeToDairy(output):
    with open(path, "a", newline="") as dairy:
        try:
            writer = csv.writer(dairy)
            writer.writerow([output])
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(
                    f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
                )
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")


while is_conversation_open:
    output = ""
    if is_chat_started:
        output += input(second_prompt)
    else:
        output += input(first_prompt)
        is_chat_started = True
    writeToDairy(output)
    if output == closing_prompt:
        is_conversation_open = False
        is_chat_started = False
