import tkinter as tk
from tkinter.messagebox import askyesno
from csv import writer, reader
from datetime import date
from os.path import expanduser, exists
from tkinter import scrolledtext, constants

#QUOTES_PATH = expanduser("~/.quotidian/quotes.csv")
QUOTES_PATH = "quotes.csv"


def clean_csv():
    lines = []
    with open(QUOTES_PATH) as read_file:
        file_reader = reader(read_file)
        for row in file_reader:
            if len(row) == 3:
                lines.append(row)
        read_file.close()

    with open(QUOTES_PATH, "w") as write_file:
        file_writer = writer(write_file)
        file_writer.writerows(lines)
        write_file.close()


def confirm_new_quote(quote, quotee, date):
    if quote != "" and quotee != "" and date != "":
        new_dialog.destroy()
        with open(QUOTES_PATH, "a") as quotes_file:
            file_writer = writer(quotes_file)
            file_writer.writerow([quote, quotee, date])
            quotes_file.close()

        display_pretty_quotes_list()


def new_quote():
    global new_dialog

    new_dialog = tk.Tk()
    new_dialog.title("New quote")

    quote_label = tk.Label(new_dialog, text="Quote:")
    quote_label.grid(row=1, column=1)
    quote_entry = tk.Entry(new_dialog)
    quote_entry.grid(row=1, column=2)

    quotee_label = tk.Label(new_dialog, text="Quotee:")
    quotee_label.grid(row=2, column=1)
    quotee_entry = tk.Entry(new_dialog)
    quotee_entry.grid(row=2, column=2)

    date_label = tk.Label(new_dialog, text="Date:")
    date_label.grid(row=3, column=1)
    date_entry = tk.Entry(new_dialog)
    date_entry.insert(0, date.strftime(date.today(), "%d/%m/%y"))
    date_entry.grid(row=3, column=2)

    confirm_button = tk.Button(new_dialog, text="Confirm",
                               command=lambda: confirm_new_quote(quote_entry.get(), quotee_entry.get(),
                                                                 date_entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=2)


def display_pretty_quotes_list():
    global quotes_display

    pretty_list = ""
    with open(QUOTES_PATH) as quotes_file:
        file_reader = reader(quotes_file)
        for row in file_reader:
            if len(row) == 3:
                pretty_list = pretty_list + f'"{row[0]}" - {row[1]}, {row[2]}\n'

    quotes_display.config(state=constants.NORMAL)
    quotes_display.insert(constants.INSERT, "\n" + pretty_list)
    quotes_display.config(state=constants.DISABLED)


def confirm_edit_quote(index, quote, quotee, date):
    if quote != "" and quotee != "" and date != "":
        with open(QUOTES_PATH) as read_file:
            file_reader = reader(read_file)
            lines = []
            for row in file_reader:
                if len(row) == 3:
                    lines.append(row)
            read_file.close()

        index += 1
        if index == len(lines):
            index = 0
        lines[index] = [quote, quotee, date]

        with open(QUOTES_PATH, "w") as write_file:
            file_writer = writer(write_file)
            file_writer.writerows(lines)
            write_file.close()

        choose_edit_dialog.destroy()
        edit_dialog.destroy()
        display_pretty_quotes_list()


def choose_edit_quote():
    global choose_edit_dialog, edit_listbox

    quotes_list = []
    with open(QUOTES_PATH) as quotes_file:
        file_reader = reader(quotes_file)
        for row in file_reader:
            if len(row) == 3:
                quotes_list.append(row)
        quotes_file.close()

    index = -(edit_listbox.curselection()[0])

    choose_edit_dialog = tk.Tk()
    choose_edit_dialog.title("Edit quote details")

    quote_label = tk.Label(choose_edit_dialog, text="Quote:")
    quote_label.grid(row=1, column=1)
    quote_entry = tk.Entry(choose_edit_dialog)
    quote_entry.insert(0, quotes_list[index - 1][0])
    quote_entry.grid(row=1, column=2)

    quotee_label = tk.Label(choose_edit_dialog, text="Quotee:")
    quotee_label.grid(row=2, column=1)
    quotee_entry = tk.Entry(choose_edit_dialog)
    quotee_entry.insert(0, quotes_list[index - 1][1])
    quotee_entry.grid(row=2, column=2)

    date_label = tk.Label(choose_edit_dialog, text="Date:")
    date_label.grid(row=3, column=1)
    date_entry = tk.Entry(choose_edit_dialog)
    date_entry.insert(0, quotes_list[index - 1][2])
    date_entry.grid(row=3, column=2)

    confirm_button = tk.Button(choose_edit_dialog, text="Confirm",
                               command=lambda: confirm_edit_quote(index, quote_entry.get(), quotee_entry.get(),
                                                                  date_entry.get()))
    confirm_button.grid(row=5, column=1, columnspan=2)


def delete_quote(index):
    global edit_dialog, edit_listbox

    with open(QUOTES_PATH) as read_file:
        file_reader = reader(read_file)
        lines = []
        for row in file_reader:
            if len(row) == 3:
                lines.append(row)
        read_file.close()

    index += 1
    if index == len(lines):
        index = 0

    if askyesno(title="Confirm delete", default="no",
                message=f'Are you sure you want to permanently delete the quote "{lines[index][0]}" - {lines[index][1]}, {lines[index][2]}?'):
        lines[index] = []

        with open(QUOTES_PATH, "w") as write_file:
            file_writer = writer(write_file)
            file_writer.writerows(lines)
            write_file.close()

    edit_dialog.destroy()
    display_pretty_quotes_list()


def edit_quote():
    global edit_dialog, edit_listbox

    edit_dialog = tk.Tk()
    edit_dialog.title("Edit quote")

    edit_listbox = tk.Listbox(edit_dialog)
    with open(QUOTES_PATH) as quotes_file:
        file_reader = reader(quotes_file)
        for row in file_reader:
            if len(row) == 3:
                edit_listbox.insert(0, f'"{row[0]}" - {row[1]}, {row[2]}')
        quotes_file.close()
    edit_listbox.grid(row=0, column=0)

    buttons_frame = tk.Frame(edit_dialog)
    buttons_frame.grid(row=1, column=0)

    edit_button = tk.Button(buttons_frame, text="Edit", command=choose_edit_quote)
    edit_button.grid(row=1, column=0)

    delete_button = tk.Button(buttons_frame, text="Delete",
                              command=lambda: delete_quote(-(edit_listbox.curselection()[0])))
    delete_button.grid(row=1, column=1)


def confirm_preferences():
    with open("preferences.csv", "w") as pref_file:
        file_writer = writer(pref_file)
        file_writer.writerow([])
        pref_file.close()

    pref_dialog.destroy()


def edit_preferences():
    global pref_dialog

    pref_dialog = tk.Tk()
    pref_dialog.title("Preferences")

    pref_confirm = tk.Button(pref_dialog, text="Save settings", command=lambda: confirm_preferences())
    pref_confirm.grid(row=3, column=1, columnspan=2)


def show_help():
    pass


def show_about():
    pass


root = tk.Tk()
root.title("Quotidian")
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New quote", command=new_quote)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Edit quotes", command=edit_quote)
edit_menu.add_separator()
edit_menu.add_command(label="Preferences", command=edit_preferences)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="How to", command=show_help)
help_menu.add_command(label="About", command=show_about)

new_button = tk.Button(root, text="New quote", command=new_quote)
new_button.grid(row=1, column=1, columnspan=3)

quotes_display = scrolledtext.ScrolledText(root, font=("Segoe UI", 10))
quotes_display.grid(row=2, column=1, columnspan=3)
credit_label = tk.Label(root, text="Quotidian pre-release by Gutter Cat Software")
credit_label.grid(row=3, column=1, columnspan=3)

if not exists(QUOTES_PATH):
    open(QUOTES_PATH, "x")

display_pretty_quotes_list()

root.mainloop()
