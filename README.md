# Quotidian
*Meaning 'occuring daily'. A play on words because it sounds like 'quote'*

You know that feeling you get when one of your friends says something absolutely hilarious/outrageous/embarassing and you just know you have to write it down and save for later, and then before long you have >10 memos on your phone or laptop that take 2 minutes to load?

Well, this piece of software aims to act as a nice central place to document all your quotes for historical preservation. Oh, and as the name suggests, on startup it displays a randomly selected 'quote of the day' as a desktop notifications.

**This isn't done yet - while it functions, it is still not polished. Hold tight, I'm working on it... sometimes...**

## Compatibility
It's made in [Python 3.11](https://www.python.org/downloads/release/python-3110/) (although any other 3.x version should work) using tkinter (I know its ugly) because I dont know anything else. When I learn a better way of making GUIs then I might remake this.

**In this branch, `Win10Toast` and `notify2` have been ditched in favour of `notify-py`. If all goes well and I can get it to function on both linux and windows, then this shall become the main branch, and the linux branch can be deleted.**

## Dependecies
- Python 3.x (preferably Python 3.11) and packages (tkinter, csv, datetime, os, random)
- [notify-py](https://pypi.org/project/notify-py/)

## To do
- Implement preferences menu
- Implement help and about menus
- Implement CLI utility because why not
- Finish testing on both linux and windows, the superior OS
