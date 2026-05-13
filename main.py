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
