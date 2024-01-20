from notifypy import Notify
from csv import reader
from random import choice
from os.path import expanduser, exists

QUOTES_PATH = expanduser("~/.quotidian/quotes.csv")

if not exists(QUOTES_PATH):
    quit()

quotes = []
with open(QUOTES_PATH) as quotes_file:
    file_reader = reader(quotes_file, delimiter=",")
    for row in file_reader:
        if len(row) == 3:
            quotes.append(row)
    quotes_file.close()

if not quotes:
    quit()

quote = choice(quotes)

notification = Notify()
notification.title = "Quote of the day"
notification.message = f'"{quote[0]}" - {quote[1]}, {quote[2]}\n'
notification.send(block=False)
