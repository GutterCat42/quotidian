import re
import tkinter as tk
from tkinter import scrolledtext, constants

# Converts from name-date-quote hierarchical format to standard


def run_formatter():
    global input_box, output_box

    quote, date, person = None, None, None
    input_lines = input_box.get("1.0", constants.END).splitlines()
    formatted_quotes = ""

    for line in input_lines:
        if line != "":
            if line[0] == '"':
                quote = line[line.find('"')+1:line.rfind('"')]
            elif line[0] in list("1234567890/-"):
                date = line.split()[0]
            else:
                if "quotes" in line.lower():
                    person = line.split()[0]

            if quote and date and person:
                formatted_quotes = formatted_quotes + '"' + quote + '" - ' + person + ", " + date + "\n"
                quote = None

    output_box.config(state=constants.NORMAL)
    output_box.delete("1.0", constants.END)
    output_box.insert(constants.INSERT, str(formatted_quotes))
    output_box.config(state=constants.DISABLED)


root = tk.Tk()
root.title("Quotidian format converter")

input_box = scrolledtext.ScrolledText(root, font=("Segoe UI", 10))
input_box.grid(row=1, column=1)
output_box = scrolledtext.ScrolledText(root, font=("Segoe UI", 10))
output_box.grid(row=1, column=2)
output_box.config(state=constants.DISABLED)
format_button = tk.Button(root, text="Format", command=run_formatter)
format_button.grid(row=2, column=1, columnspan=2)

root.mainloop()
