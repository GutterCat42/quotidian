import notify2
from csv import reader
from random import choice
from os.path import expanduser, exists

#QUOTES_PATH = expanduser("~/.quotidian/quotes.csv")
QUOTES_PATH = "quotes.csv"

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

notify2.init("Quotidian")
notification = notify2.Notification("Quote of the day", f'"{quote[0]}" - {quote[1]}, {quote[2]}\n')
notification.set_timeout(5000)
notification.show()
