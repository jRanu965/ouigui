import tkinter as tk
from tkinter import messagebox

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Calculator App")
window.geometry("400x400")
window.configure(bg="lightgray")

# ---------------- FUNCTIONS ----------------
def calculate(): 

    # Try to convert user input into numbers 
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Get selected operation from radio buttons
        operation = math_choice.get()
    

        # Check which operation user selected
        if operation == "+":
            answer = num1 + num2

        elif operation == "-":
            answer = num1 - num2

        else:
            answer = "Choose an operation"

        # Display answer on screen
        answer_label.config(text=f"Answer: {answer}")

    # If user enters invalid data
    except:
        messagebox.showerror("Error", "Please enter valid numbers")


# Function to clear all fields
def clear():

    # Remove text from entry boxes
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

    # Reset answer label
    answer_label.config(text="Answer: ")

    # Remove selected radio button
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
input_frame = tk.Frame(window, bg="red")
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

# Variable to store selected radio button
math_choice = tk.StringVar()

# Set default selection (must match one of the radio button values)
math_choice.set("+")

# Addition radio button
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
  
# Subtraction radio button
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

# ---------------- BUTTON FRAME ----------------
button_frame = tk.Frame(window, bg="red")
button_frame.pack(pady=25)

# CALCULATE BUTTON
calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12, "bold"),
    width=14,
    height=1,
    bg="#073168",
    fg="white",
    command=calculate
)
calculate_button.grid(row=0, column=0, padx=15)

# CLEAR BUTTON
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    width=14,
    height=1,
    bg="#028128",
    fg="white",
    command=clear
)
clear_button.grid(row=0, column=1, padx=15)

# ---------------- ANSWER SECTION ----------------
answer_title = tk.Label(
    window,
    text="Your Answer",
    font=("Arial", 14, "bold"),
    bg="gray"
)
answer_title.pack(pady=5)

answer_label = tk.Label(
    window,
    text="Answer will appear here",
    font=("Arial", 16),
    bg="white",
    fg="black",
    width=24,
    height=2,
    relief="solid",
    bd=2
)
answer_label.pack(pady=10)

# ---------------- RUN PROGRAM ----------------
window.mainloop()   