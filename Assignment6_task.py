import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400") # Example size

expression = ""

def on_button_click(char):
    global expression
    if char == '=':
        try:
            result = str(eval(expression))
            display_var.set(result)
            expression = result
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif char == 'C':
        expression = ""
        display_var.set("0")
    else:
        expression += str(char)
        display_var.set(expression)

display_var = tk.StringVar()
display_var.set("0")
display_entry = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=5, relief="ridge")
display_entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, font=("Arial", 18), padx=20, pady=20,command=lambda b=button_text: on_button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
		
root.mainloop()