import tkinter as tk
# main window 
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x600")
window.resizable(False, False)

# functions
def button_click(number):
    current = display_var.get()
    display_var.set(current + str(number))

def button_clear():
    display_var.set("")

def button_equal():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

def button_backspace():
    current = display_var.get()
    display_var.set(current[:-1])

# display

display_var = tk.StringVar()
display = tk.Entry(window, textvariable=display_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")

display.pack(fill="both", ipady=15)

# grid layout for buttons
button_frame = tk.Frame(window)
button_frame.pack(expand=True, fill="both")
buttons = [
    ("7", lambda: button_click(7)), ("8", lambda: button_click(8)),

    ("9", lambda: button_click(9)), ("/", lambda: button_click("/")),
 
    ("4", lambda: button_click(4)), ("5", lambda: button_click(5)),

    ("6", lambda: button_click(6)), ("*", lambda: button_click("*")),
 
    ("1", lambda: button_click(1)), ("2", lambda: button_click(2)),

    ("3", lambda: button_click(3)), ("-", lambda: button_click("-")),
 
    ("0", lambda: button_click(0)), (".", lambda: button_click(".")),

    ("=", button_equal),            ("+", lambda: button_click("+")),

    ("C", button_clear),            ("⌫", button_backspace),
]

# create buttons in grid layout
row = 0
col = 0
for(label , action) in buttons:
    btn = tk.Button(button_frame, text=label, font=("Arial", 18), command=action)
    btn.grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# configure grid weights
for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(row + 1):
    button_frame.rowconfigure(i, weight=1)

# keyboard bindings
def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        button_click(key)
    elif key == "/":
        button_click("/")
    elif key == "\r":  # Enter key
        button_equal()
    elif key == "\x08":  # Backspace key
        button_backspace()
    elif key.lower() == "c":
        button_clear()

def key_press_special(event):
    if event.keysym == "Return":
        button_equal()
    elif event.keysym == "BackSpace":
        button_backspace()
    elif event.keysym.lower() == "Escape":
        button_clear()

window.bind("<Key>", key_press)
window.bind("<Return>", lambda event: button_equal())
window.bind("<BackSpace>", lambda event: button_backspace())
window.bind("<Escape>", lambda event: button_clear())


# start the application
window.mainloop()