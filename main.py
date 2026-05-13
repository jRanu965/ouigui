# Addition and Subtraction Calculator
# Save as calculator.py

import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Calculator App")
window.geometry("400x400")
window.configure(bg="lightgray") 

# ---------------- FUNCTIONS ----------------
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        operation = math_choice.get()

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        else:
            answer = "Choose an operation"

        answer_label.config(text=f"Answer: {answer}")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    answer_label.config(text="Answer: ")
    math_choice.set("")

# ---------------- TITLE LABEL ----------------
title_label = tk.Label(
    window,
    text="Calculator for Addition and Subtraction",
    font=("Arial", 16),
    bg="lightgray"
)
title_label.pack(pady=10)

# ---------------- FRAME ----------------
input_frame = tk.Frame(window, bg="lightgray")
input_frame.pack(pady=15)


# ---------------- FIRST NUMBER ----------------
label1 = tk.Label(
    input_frame,
    text="Enter First Number",
    font=("Arial", 12, "bold"),
    bg="lightgray",
    fg="black"
)
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry1 = tk.Entry(
    input_frame,
    font=("Arial", 13),
    width=18,
    bd=3
)
entry1.grid(row=0, column=1, padx=10, pady=10)

# ---------------- SECOND NUMBER ----------------
label2 = tk.Label(
    input_frame,
    text="Enter Second Number",
    font=("Arial", 12, "bold"),
    bg="lightgray",
    fg="black"
)
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry2 = tk.Entry(
    input_frame,
    font=("Arial", 13),
    width=18,
    bd=3
)
entry2.grid(row=1, column=1, padx=10, pady=10)

# ---------------- OPERATION SECTION ----------------
operation_label = tk.Label(
    window,
    text="Choose an Operation",
    font=("Arial", 13, "bold"),
    bg="lightgray"
)
operation_label.pack(pady=5)

math_choice = tk.StringVar()

radio_add = tk.Radiobutton(
    window,
    text=" Addition (+)",
    variable=math_choice,
    value="+",
    font=("Arial", 12),
    bg="lightgray",
    activebackground="lightgray"
)
radio_add.pack()

radio_subtract = tk.Radiobutton(
    window,
    text=" Subtraction (-)",
    variable=math_choice,
    value="-",
    font=("Arial", 12),
    bg="lightgray",
    activebackground="lightgray"
)
radio_subtract.pack()