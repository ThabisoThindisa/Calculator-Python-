import tkinter as tk
import math
import operator
import ast


def calculate_expression(expression):
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def calculate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            left = calculate(node.left)
            right = calculate(node.right)
            return operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](calculate(node.operand))

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")
    return calculate(tree.body)


def start(number):  # Display numbers
    entry.config(state="normal")
    current_value = entry.get()
    new_value = current_value + str(number)
    entry.delete(0, tk.END)
    entry.insert(0, new_value)
    entry.config(state="disabled")


def add_symbol(symbol):  # Add symbols to display
    entry.config(state="normal")
    entry.insert(tk.END, symbol)
    entry.config(state="readonly")


def Calc_Sin(number):  # Perforn sin operation
    return math.sin(number)


def calc_Cos(number):  # Perforn Cosine operation
    return math.cos(number)


def calc_Tan(number):  # Perforn tangent operation
    return math.tan(number)


def calc_Exponent(number, exponent):
    total = 0
    index = 0

    while index < exponent:
        total *= number
        index += 1

    return total

 # Perform simple addition,substraction,multiplication and divition


def calc_Multiply(*numbers):
    total = 0
    for index in numbers:
        total *= index
    return total


def calc_Addition(*numbers):
    total = 0
    for index in numbers:
        total += index
    return total


def calc_Divition(*numbers):
    total = 0
    for index in numbers:
        total /= index
    return total


def calc_Substraction(*numbers):
    total = 0
    for index in numbers:
        total -= index
    return total

# Calculate final answer from the entry textArea


def CAlculate_Answer():
    try:
        expression = entry.get().strip()
        result = calculate_expression(expression)

        entryAnswer.config(state="normal")
        entryAnswer.delete(0, tk.END)
        entryAnswer.insert(0, str(result))
        entryAnswer.config(state="readonly")

    except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
        entryAnswer.config(state="normal")
        entryAnswer.delete(0, tk.END)
        entryAnswer.insert(0, "Error")
        entryAnswer.config(state="readonly")


# 1. Create the main window
DisplayArea = tk.Tk()
DisplayArea.title("Calculator")
DisplayArea.geometry("400x370")

entry = tk.Entry(DisplayArea, width=16, font=("Arial", 24))
entry.grid(row=1, column=0, columnspan=4,
           padx=10, pady=5, sticky="ew")

entryAnswer = tk.Entry(DisplayArea, width=16, font=("Arial", 24))
entryAnswer.grid(row=2, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

# Buttons
button_Tangent = tk.Button(DisplayArea, text="Tan")
button_Sin = tk.Button(DisplayArea, text="Sin")
button_Cos = tk.Button(DisplayArea, text="Cos")
button_log = tk.Button(DisplayArea, text="Log")
button_Exponent = tk.Button(DisplayArea, text="x²")

button_Substract = tk.Button(
    DisplayArea, text="-", command=lambda: add_symbol("-"))
button_Multiply = tk.Button(DisplayArea, text="x",
                            command=lambda: add_symbol("*"))
button_Divide = tk.Button(DisplayArea, text="÷",
                          command=lambda: add_symbol("/"))
button_Add = tk.Button(DisplayArea, text="+", command=lambda: add_symbol("+"))

# Numbers
button_one = tk.Button(DisplayArea, text="1", command=lambda: start(1))
button_Two = tk.Button(DisplayArea, text="2", command=lambda: start(2))
button_Three = tk.Button(DisplayArea, text="3", command=lambda: start(3))
button_Four = tk.Button(DisplayArea, text="4", command=lambda: start(4))
button_Five = tk.Button(DisplayArea, text="5", command=lambda: start(5))
button_Six = tk.Button(DisplayArea, text="6", command=lambda: start(6))
button_Seven = tk.Button(DisplayArea, text="7", command=lambda: start(7))
button_Eight = tk.Button(DisplayArea, text="8", command=lambda: start(8))
button_Nine = tk.Button(DisplayArea, text="9", command=lambda: start(9))
button_Zero = tk.Button(DisplayArea, text="0", command=lambda: start(0))

button_Commar = tk.Button(DisplayArea, text=".",
                          command=lambda: add_symbol("."))
button_Asin = tk.Button(DisplayArea, text="sin`")
button_ACos = tk.Button(DisplayArea, text="Cos `")
button_ATan = tk.Button(DisplayArea, text="Tan `")
button_Open_Bracket = tk.Button(
    DisplayArea, text="(", command=lambda: add_symbol("("))
button_Close_Bracket = tk.Button(
    DisplayArea, text=")", command=lambda: add_symbol(")"))

# Button to display the final answer.
Final_answer = tk.Button(
    DisplayArea,
    text="ANS",
    command=CAlculate_Answer
)
# Row 3
button_Tangent.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
button_Sin.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
button_Cos.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
Final_answer.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

# Row 4
button_Asin.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
button_ACos.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
button_ATan.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")
button_Exponent.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")
# Row 5
button_one.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
button_Two.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
button_Three.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
button_Add.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")
# Row 6
button_Four.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
button_Five.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
button_Six.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")
button_Multiply.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

# Row 7

button_Seven.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
button_Eight.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
button_Nine.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
button_Divide.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

button_Zero.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
button_Open_Bracket.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
button_Close_Bracket.grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
button_Substract.grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

for column in range(4):
    DisplayArea.grid_columnconfigure(column, weight=1, uniform="buttons")

# 4. Run the application loop
DisplayArea.mainloop()
