# ============================================================
#                 ADVANCED SCIENTIFIC CALCULATOR
# ============================================================
#
# ✔ PROJECT NAME:
#     Advanced GUI Scientific Calculator using Python (Tkinter)
#
# ✔ PROJECT TYPE:
#     Desktop GUI Application
#
# ✔ LANGUAGE:
#     Python 3
#
# ============================================================
# ✔ OVERALL PURPOSE OF PROJECT
# ============================================================
#
# ✔ This project is a calculator that:
#     → Performs basic arithmetic operations
#     → Performs scientific calculations
#     → Stores calculation history
#     → Provides modern GUI interface
#     → Handles errors safely
#
# ============================================================
# ✔ FEATURES OF THIS CALCULATOR
# ============================================================
#
# ✔ Basic arithmetic operations (+, -, *, /)
# ✔ Scientific calculations (sin, cos, tan, log, sqrt)
# ✔ Modern dark-themed UI
# ✔ Scientific calculator functions
# ✔ Basic arithmetic operations
# ✔ Backspace and clear functionality
# ✔ Calculation history panel
# ✔ Timestamp-based history logging
# ✔ Responsive grid layout system
# ✔ Error handling (invalid input protection)
# ✔ Clean structured button system
# ✔ Auto layout generation using loops
#

# ============================================================
# ✔ LIBRARIES USED AND THEIR PURPOSE
# ============================================================
#
# ✔ tkinter
#     → Used to build GUI interface (buttons, layout, display)
#
# ✔ math
#     → Provides scientific functions like:
#         sqrt(), sin(), cos(), tan(), log10(), factorial()
#
# ✔ datetime
#     → Used to generate timestamps for calculation history
#     → Example: [12:45:10] 5 + 5 = 10
#
# ✔ random
#     → Used for generating dynamic AI-style suggestions
#     → Provides variation in UI messages
#
# ============================================================
# ✔ TKINTER (MAIN GUI LIBRARY)
# ============================================================
#
# ✔ Tkinter is Python’s built-in GUI library.
#
# ✔ PURPOSE IN THIS PROJECT:
#     - Creates application window
#     - Creates buttons (numbers + operators)
#     - Creates input/display field
#     - Creates frames and layout system
#
# ✔ HOW IT WORKS:
#     Tkinter uses a "widget-based system"
#     Each element (button, label, entry) is a widget.
#
# ✔ IMPORTANT WIDGETS USED:
#     - Tk()        → Main application window
#     - Entry()     → Input/display screen
#     - Button()    → Clickable buttons
#     - Frame()     → Layout container
#     - Text()      → History display panel
#
# ============================================================
# ✔ IMPORTANT CONCEPTS USED IN THIS PROJECT
# ============================================================
#
# ✔ OPERATORS:
#     → +  (Addition)
#     → -  (Subtraction)
#     → *  (Multiplication)
#     → /  (Division)
#
# ✔ EXPRESSIONS:
#     → A combination of numbers + operators
#     → Example: 5 + 3 * 2
#
# ✔ FUNCTIONS:
#     → Reusable blocks of code
#     → Example: click(), calculate(), scientific()
#
# ✔ IF / ELSE USAGE:
#     → Used inside scientific() function
#     → Used to check which operation to perform
#
#         Example:
#         if func == "sin":
#             calculate sine
#         elif func == "cos":
#             calculate cosine
#
# ✔ LIBRARY USAGE FLOW:
#     → tkinter → UI creation
#     → math → calculations
#     → datetime → history time
#     → random → AI messages
#
# ============================================================
# ✔ CODE EXECUTION STEPS (VERY IMPORTANT FLOW)
# ============================================================
#
# ✔ STEP 1:
#     Import all libraries (tkinter, math, datetime, random)
#
# ✔ STEP 2:
#     Create main window using Tk()
#
# ✔ STEP 3:
#     Create display (Entry box)
#
# ✔ STEP 4:
#     Create history panel (Text box)
#
# ✔ STEP 5:
#     Define all functions:
#         click()
#         clear_display()
#         backspace()
#         calculate()
#         scientific()
#         add_history()
#
# ✔ STEP 6:
#     Define buttons list (data structure)
#
# ✔ STEP 7:
#     Use FOR LOOP:
#         → Create buttons automatically
#
# ✔ STEP 8:
#     Configure grid layout (rows & columns loops)
#
# ✔ STEP 9:
#     Start application using mainloop()
#
# ============================================================
# ✔ LOOP SYSTEM EXPLANATION
# ============================================================
#
# ✔ FOR LOOP USED HERE:
#
#     for b in buttons:
#
# ✔ HOW IT WORKS:
#     → Takes one button from list
#     → Sends it to create_button()
#     → Creates GUI button
#     → Moves to next button
#
# ✔ WHY LOOP USED:
#     → Avoids repetitive code
#     → Makes project scalable
#
# ============================================================
# ✔ IF / ELSE LOGIC (VERY IMPORTANT)
# ============================================================
#
# ✔ USED INSIDE scientific() FUNCTION
#
# ✔ PURPOSE:
#     → To decide which scientific operation to perform
#
# ✔ FLOW:
#
#     if func == "sqrt":
#         square root calculate
#     elif func == "sin":
#         sine calculate
#     elif func == "cos":
#         cosine calculate
#     else:
#         other operations
#
# ✔ RESULT:
#     → Only ONE condition executes at a time
#
# ============================================================
# ✔ OPERATORS + EXPRESSIONS (WHERE USED)
# ============================================================
#
# ✔ OPERATORS USED IN calculate():
#     → + - * /
#
# ✔ EXPRESSIONS:
#     → User input string like:
#         "5+3*2"
#
# ✔ eval() FUNCTION:
#     → Converts string expression into real calculation
#
# ============================================================
# ✔ FUNCTION CALL FLOW (VERY IMPORTANT)
# ============================================================
#
# ✔ BUTTON PRESS FLOW:
#
#     Button clicked →
#         click() OR calculate() OR scientific()
#
# ✔ SCIENTIFIC FLOW:
#
#     scientific("sin") →
#         IF condition check →
#         math function execute →
#         result display →
#         history update
#
# ✔ CALCULATE FLOW:
#
#     calculate() →
#         eval(expression) →
#         result →
#         history save
#
# ============================================================
# ✔ FEATURES SUMMARY
# ============================================================
#
# ✔ Basic calculator
# ✔ Scientific calculator
# ✔ History system
# ✔ Error handling
# ✔ Modern UI
# ✔ Auto button generation
#
# ============================================================
# ✔ UI / DESIGN SYSTEM (COLORS & STYLING)
# ============================================================
#
# ✔ Background Theme:
#     - Dark theme (#0f172a)
#
# ✔ Display Screen:
#     - Dark bluish background (#1e293b)
#     - White text for high contrast
#
# ✔ Button Color Coding:
#
#     ✔ Number Buttons:
#         → Dark gray-blue (#1e293b)
#
#     ✔ Operator Buttons (+, -, *, /):
#         → Blue color (#2563eb)
#
#     ✔ Scientific Buttons:
#         → Purple color (#7c3aed)
#
#     ✔ Equal Button:
#         → Green color (#10b981)
#
#     ✔ Clear / Backspace:
#         → Red color (#ef4444)
#
# ✔ Design Style:
#     → Flat UI design (modern minimal look)
#     → No heavy borders
#     → Rounded-like feel using padding
#     → Consistent spacing using grid system
#
# ============================================================
# ✔ BUTTON SYSTEM DESIGN LOGIC
# ============================================================
#
# ✔ All buttons are stored inside a list structure.
#
# ✔ Each button contains:
#     - Button text (label)
#     - Row position
#     - Column position
#     - Function to execute
#     - Background color
#
# ✔ A LOOP is used to generate buttons automatically:
#     → This avoids repetitive manual coding
#     → Ensures scalability and clean structure
#
# ============================================================
# ✔ LOOPS USED IN THIS PROJECT
# ============================================================
#
# ✔ Button Creation Loop:
#     → Automatically creates all calculator buttons
#
# ✔ Row Configuration Loop:
#     → Makes UI responsive vertically
#
# ✔ Column Configuration Loop:
#     → Makes UI responsive horizontally
# ✔ WHAT IS TKINTER?
# ============================================================
#
# ✔ Tkinter is Python's built-in GUI library.
# ✔ It is used to build desktop applications.
# ✔ It works using "widgets" such as:
#     - Button
#     - Entry (input box)
#     - Label
#     - Frame
#     - Text box
#
# ✔ In this project:
#     → Entry = calculator display
#     → Buttons = numbers + operations
#     → Text = history panel
#     → Frames = layout structure
#
# ============================================================
# ✔ DESIGN SYSTEM (UI STYLING)
# ============================================================
#
# ✔ Background: Dark theme (#0f172a)
# ✔ Display: Dark bluish panel (#1e293b)
# ✔ Number buttons: Dark gray-blue
# ✔ Operator buttons: Blue
# ✔ Scientific buttons: Purple
# ✔ Equal button: Green
# ✔ Clear/Backspace: Red
#
# ✔ Design Style:
#     → Flat UI (modern minimal design)
#     → No heavy borders
#     → Clean spacing using grid system
#
# ============================================================
# ✔ LOOP SYSTEM (VERY IMPORTANT PART)
# ============================================================
#
# ✔ LOOP is used to repeat code automatically instead of writing
#   same code multiple times manually.
#
# ============================================================
# ✔ 1. BUTTON CREATION LOOP (MAIN LOOP)
# ============================================================
#
#     for button in buttons:
#
# ✔ HOW IT WORKS STEP BY STEP:
#
#     1. Python reads "buttons" list
#     2. It picks ONE button at a time
#     3. Each button contains:
#         → text (what is shown)
#         → row position
#         → column position
#         → function (click or scientific)
#         → color
#
#     4. Loop sends this data to create_button()
#     5. Tkinter creates actual GUI button
#     6. Button is placed on screen
#     7. Moves to next button automatically
#     8. Repeats until list ends
#
# ✔ WHY THIS LOOP IS IMPORTANT:
#     → Saves writing 30+ manual button codes
#     → Makes code clean and scalable
#     → Easy to update or add new buttons
#
# ============================================================
# ✔ 2. ROW CONFIGURATION LOOP
# ============================================================
#
#     for i in range(8):
#
# ✔ HOW IT WORKS:
#     → Generates numbers from 0 to 7
#     → Each number represents a row
#     → Tkinter applies settings to each row
#
# ✔ PURPOSE:
#     → Makes UI responsive vertically
#     → Prevents uneven button spacing
#
# ============================================================
# ✔ 3. COLUMN CONFIGURATION LOOP
# ============================================================
#
#     for j in range(4):
#
# ✔ HOW IT WORKS:
#     → Generates numbers 0,1,2,3
#     → Each column is configured one by one
#
# ✔ PURPOSE:
#     → Equal spacing between buttons
#     → Clean alignment in UI
#
# ============================================================
# ✔ SUMMARY OF LOOP CONCEPT
# ============================================================
#
# ✔ Loop = repetition system
# ✔ Processes one item at a time
# ✔ Automatically continues until list ends
# ✔ Reduces manual coding effort
# ✔ Makes code scalable and professional
#
# ============================================================
# ✔ FUNCTIONALITY OVERVIEW
# ============================================================
#
# ✔ click(value)
#     → Adds input to display
#
# ✔ clear_display()
#     → Clears full screen
#
# ✔ backspace()
#     → Deletes last character
#
# ✔ calculate()
#     → Evaluates expression
#
# ✔ scientific()
#     → Performs advanced math operations
#
# ✔ add_to_history()
#     → Stores calculation with time
#
# ✔ ai_suggestion()
#     → Shows dynamic random messages
#
#
# ============================================================
# ✔ NAMING CONVENTION (CODE STYLE)
# ============================================================
#
# ✔ Python Standard Style Used:
#
#     → snake_case naming convention
#     Example:
#         clear_display()
#         backspace()
#         add_to_history()
#
# ✔ Variables are descriptive for readability:
#     → entry
#     → button_frame
#     → history_box
#
# ============================================================
# ✔ FUNCTIONALITY BREAKDOWN
# ============================================================
#
# ✔ click(value)
#     → Inserts number/operator into display screen
#
# ✔ clear_display()
#     → Clears full input screen
#
# ✔ backspace()
#     → Removes last character from input
#
# ✔ calculate()
#     → Evaluates mathematical expression
#
# ✔ scientific(function)
#     → Performs advanced math operations
#
# ✔ add_to_history()
#     → Saves calculation result with timestamp
#
# ✔ ai_suggestion()
#     → Displays dynamic suggestion messages
#
# ============================================================
# ✔ PROGRAM EXECUTION FLOW
# ============================================================
#
# ✔ 1. Import required libraries
# ✔ 2. Create main application window
# ✔ 3. Setup display screen
# ✔ 4. Setup history panel
# ✔ 5. Define all functions
# ✔ 6. Create button layout structure
# ✔ 7. Generate buttons using loop
# ✔ 8. Configure grid layout system
# ✔ 9. Start main application loop
#
# ============================================================
# ✔ ERROR HANDLING SYSTEM
# ============================================================
#
# ✔ try/except blocks used to prevent crashes
# ✔ Invalid inputs show popup error messages
# ✔ Application clears screen on error automatically
#
# ============================================================
# ✔ CODE STRUCTURE QUALITY
# ============================================================
#
# ✔ Modular function-based design
# ✔ Clean separation of UI and logic
# ✔ Scalable button system
# ✔ Easy to read and maintain
# ✔ Professional level organization
#
# ============================================================
# ✔ END OF DOCUMENTATION SECTION
# ============================================================
#

import tkinter as tk
from tkinter import messagebox
import math
from datetime import datetime
import random

# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("700x750")
root.configure(bg="#0f172a")
root.resizable(True, True)

# ================= DISPLAY =================

display_frame = tk.Frame(root, bg="#0f172a")
display_frame.pack(pady=15)

entry = tk.Entry(
    display_frame,
    font=("Segoe UI", 28),
    bg="#1e293b",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white",
    width=22
)
entry.pack(ipady=20)

# ================= HISTORY =================

history_label = tk.Label(root, text="History",
                         font=("Segoe UI", 14, "bold"),
                         bg="#0f172a", fg="white")
history_label.pack()

history_box = tk.Text(root, height=8, width=60,
                      font=("Consolas", 10),
                      bg="#111827", fg="#10b981",
                      bd=0)
history_box.pack(pady=10)
history_box.config(state="disabled")

# ================= AI LABEL =================

ai_label = tk.Label(root, text="Scientific Calculator",
                    font=("Segoe UI", 15, "italic"),
                    bg="#0f172a", fg="#60a5fa")
ai_label.pack()

# ================= BUTTON FRAME =================

button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack()

# ================= COLORS =================

num_color = "#1e293b"
op_color = "#2563eb"
sc_color = "#7c3aed"
eq_color = "#10b981"
clr_color = "#ef4444"

# ============================================================
# ✔ FUNCTIONS (DETAILED EXPLANATION INSIDE CODE)
# ============================================================

# ------------------------------------------------------------
# ✔ click(value)
# PURPOSE:
#   Adds pressed button value into display screen
# USED WHEN:
#   Number or operator button is clicked
# ------------------------------------------------------------

def click(value):
    entry.insert(tk.END, value)

# ------------------------------------------------------------
# ✔ clear_display()
# PURPOSE:
#   Clears full calculator screen
# USED WHEN:
#   "C" button pressed
# ------------------------------------------------------------

def clear_display():
    entry.delete(0, tk.END)

# ------------------------------------------------------------
# ✔ backspace()
# PURPOSE:
#   Deletes last entered character
# USED WHEN:
#   "⌫" button pressed
# ------------------------------------------------------------

def backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

# ------------------------------------------------------------
# ✔ add_history(expression, result)
# PURPOSE:
#   Saves calculation in history panel with time
# USED WHEN:
#   After calculation completes
# ------------------------------------------------------------

def add_history(expression, result):
    history_box.config(state="normal")
    time = datetime.now().strftime("%H:%M:%S")
    history_box.insert(tk.END, f"[{time}] {expression} = {result}\n")
    history_box.config(state="disabled")
    history_box.see(tk.END)
# ------------------------------------------------------------
# ✔ calculate()
# PURPOSE:
#   Evaluates mathematical expression
# FLOW:
#   1. Read input
#   2. Calculate result
#   3. Show result
#   4. Save in history
#   5. Handle errors safely
# USED WHEN:
#   "=" button pressed
# ------------------------------------------------------------
def calculate():
    try:
        expr = entry.get()

        # Divide by zero check
        if "/0" in expr:
            raise ZeroDivisionError

        result = eval(expr)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

        add_history(expr, result)

    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")
        clear_display()

    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        clear_display()

# ------------------------------------------------------------
# ✔ scientific(func)
# PURPOSE:
#   Performs scientific calculations using math library
# SUPPORTED:
#   sqrt, sin, cos, tan, log, ln, square, cube, factorial
# USED WHEN:
#   Scientific buttons pressed
# ------------------------------------------------------------

def scientific(func):
    try:
        val = float(entry.get())

        if func == "sqrt":
            res = math.sqrt(val)
        elif func == "sin":
            res = math.sin(math.radians(val))
        elif func == "cos":
            res = math.cos(math.radians(val))
        elif func == "tan":
            res = math.tan(math.radians(val))
        elif func == "log":
            res = math.log10(val)
        elif func == "ln":
            res = math.log(val)
        elif func == "square":
            res = val ** 2
        elif func == "cube":
            res = val ** 3
        elif func == "factorial":
            res = math.factorial(int(val))
        elif func == "percent":
            res = val / 100

        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
        add_history(func, res)

    except:
        messagebox.showerror("Error", "Math Error")
        clear_display()

# ============================================================
# ✔ BUTTON CREATION FUNCTION
# ============================================================

def create_button(text, row, col, cmd, color, span=1):
    tk.Button(
        button_frame,
        text=text,
        command=cmd,
        font=("Segoe UI", 14, "bold"),
        bg=color,
        fg="white",
        bd=0,
        width=6,
        height=2
       ).grid(
       row=row,
       column=col,
       columnspan=span,
       padx=5,
       pady=5,
       sticky="nsew"
)
def clear_history():
    history_box.config(state="normal")
    history_box.delete(1.0, tk.END)
    history_box.config(state="disabled")
# ============================================================
# ✔ BUTTON LIST
# ============================================================

buttons = [

    ("C", 0, 0, clear_display, clr_color),
    ("⌫", 0, 1, backspace, clr_color),
    ("%", 0, 2, lambda: scientific("percent"), sc_color),
    ("/", 0, 3, lambda: click("/"), op_color),

    ("7", 1, 0, lambda: click("7"), num_color),
    ("8", 1, 1, lambda: click("8"), num_color),
    ("9", 1, 2, lambda: click("9"), num_color),
    ("*", 1, 3, lambda: click("*"), op_color),

    ("4", 2, 0, lambda: click("4"), num_color),
    ("5", 2, 1, lambda: click("5"), num_color),
    ("6", 2, 2, lambda: click("6"), num_color),
    ("-", 2, 3, lambda: click("-"), op_color),

    ("1", 3, 0, lambda: click("1"), num_color),
    ("2", 3, 1, lambda: click("2"), num_color),
    ("3", 3, 2, lambda: click("3"), num_color),
    ("+", 3, 3, lambda: click("+"), op_color),

    ("0", 4, 0, lambda: click("0"), num_color),
    (".", 4, 1, lambda: click("."), num_color),
    ("=", 4, 2, calculate, eq_color, 2),

    ("√", 5, 0, lambda: scientific("sqrt"), sc_color),
    ("sin", 5, 1, lambda: scientific("sin"), sc_color),
    ("cos", 5, 2, lambda: scientific("cos"), sc_color),
    ("tan", 5, 3, lambda: scientific("tan"), sc_color),

    ("log", 6, 0, lambda: scientific("log"), sc_color),
    ("ln", 6, 1, lambda: scientific("ln"), sc_color),
    ("x²", 6, 2, lambda: scientific("square"), sc_color),
    ("x³", 6, 3, lambda: scientific("cube"), sc_color),

    ("n!", 7, 0, lambda: scientific("factorial"), sc_color),
    ("C", 0, 0, clear_display, clr_color),
    ("⌫", 0, 1, backspace, clr_color),
    ("%", 0, 2, lambda: scientific("percent"), sc_color),
    ("/", 0, 3, lambda: click("/"), op_color),
    ("HCLR", 0, 4, clear_history, "#f97316"),
    

]

# ============================================================
# ✔ LOOP SYSTEM (AUTO BUTTON GENERATION)
# ============================================================

for b in buttons:
    if len(b) == 5:
        t, r, c, cmd, col = b
        create_button(t, r, c, cmd, col)
    else:
        t, r, c, cmd, col, sp = b
        create_button(t, r, c, cmd, col, sp)

# ============================================================
# ✔ GRID RESPONSIVENESS
# ============================================================

for i in range(8):
    button_frame.grid_rowconfigure(i, weight=1)

for j in range(5):
    button_frame.grid_columnconfigure(j, weight=1)

# ================= RUN APP =================

root.mainloop()