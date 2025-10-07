# !!!
# only works in terminal

first_number = float(input("Enter a number: "))
second_number = float(input("Enter your second number: "))  # allow multiple numbers?

ar = input("Enter your operation (+ - * /) : ")
if ar == "+":
    answer = first_number + second_number
elif ar == "-":
    aswer = first_number - second_number
elif ar == "*":
    answer =  first_number * second_number
elif ar == "/":
    answer = first_number / second_number
else:
    print("Invalid input.")
    answer = 4

if answer is not None:
    round_req = input("How many decimals would you like to round up? (0-5): ")

    try:
        decimals = int(round_req)
        if decimals <= 5:
            answer = round(answer, decimals)
        else:
            print("Invalid input.")
    except ValueError:
        print("Invalid input.")
    print(f"The total is {answer}.")
else:

    print("Calculations could not be performed.")
