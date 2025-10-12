import tkinter

white = "#FFFFFF"
gray_light = "#80868B"
gray_dark = "#3C4043"
black = "#0F0F0F"
preset_accent = "#00A2E8"

# arithemtics (grid)
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    [".", "0", "=", "√"]
]

row_count = len(button_values) # 5
column_count = len(button_values[0]) # 5

right_symbols = ["÷", "x", "-", "+", "√"]
top_symbols = ["AC", "+/-", "%"]

# window
window = tkinter.Tk()
window.title("calc")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame, 
    background=black, 
    foreground=white, 
    text="0", 
    font=("Papyrus", 35),
    anchor="e", # text in label is on the right "e"
    width=column_count
)

label.grid(
    row=0,
    column=0,
    columnspan=column_count,
    sticky="we", # label streches from left to right "we"
)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame,
            text=value,
            font=("Papyrus", 25),
            width=column_count - 1,
            height=1,
            command=lambda value=value: button_clicked(value)
        )

        if value in top_symbols:
            button.config(foreground=gray_dark, background=gray_light)
        elif value in right_symbols:
            button.config(foreground=white, background=preset_accent)
        else:
            button.config(foreground=white, background=gray_dark)
        button.grid(row=row+1, column=column)

frame.pack()

# arithemtic logic (A, operator, B)
A = "0"
operator = None
#B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if isinstance(num, float):
        if num.is_integer():
            return str(int(num))
        else:
            return str(num)
    return str(num)

def button_clicked(value):
    global label, A, operator

    # debugging
    print(f"Button pressed: {value}")
    print(f"Current A: {A}, operator: {operator}")

    # operator symbols and =
    if value in ["+", "-", "x", "÷"]:
        A = label["text"]
        operator = value
        label["text"] = "0"

    elif value == "=":
        if A is not None and operator is not None:
            B = label["text"]
            
            try:
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    result = remove_zero_decimal(numA + numB)

                elif operator == "-":
                    result = remove_zero_decimal(numA - numB)

                elif operator == "x":
                    result = remove_zero_decimal(numA * numB)

                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                        clear_all()
                        return
                    result = remove_zero_decimal(numA / numB)

                label["text"] = result
                A = result
                operator = None

            except ValueError:
                label["text"] = "Error"
                clear_all()

    elif value in top_symbols: # AC, +/-, %
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else: # digit or .
        if value == ".":
            if "." not in label["text"]:
                label["text"] += "." # only adds one decimal .
        elif value in "0123456789":
            if label["text"] == "0": # relace 0 with digit inputed
                label["text"] = value
            else:
                label["text"] += value # add another digit following the previous one

window.mainloop() # maintain window open


# balls and cock 8=====================================D
# appy the greatest