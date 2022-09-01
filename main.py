#!/usr/bin/python

# Import modules

# Tkinter for GUI window
import tkinter as tk
from tkinter import ttk
# OS for system interaction
import os
# Threading for multithreading for updating
import threading
# Time for wait commands
import time

# System Vars
ram = os.popen("free -h").read()

# Methods
def close():
    root.quit()

def update():
    thecmd = os.popen("free -h").read()
    freeram.config(text = thecmd)

def continueupdate():
    while True:
        update()
        time.sleep(0.1)

# Main code start

# Window Attributes
root = tk.Tk()
root.title("Solar Car Telemetry")
root.attributes("-fullscreen", True)

# Tab initialization
tabControl = ttk.Notebook(root)
homeTab = ttk.Frame(tabControl)
powerTab = ttk.Frame(tabControl)
auxTab = ttk.Frame(tabControl)

tabs = [homeTab, powerTab, auxTab]
tabtitle = ["Home", "Main Power", "Auxillary Power"]

for i in range(len(tabs)):
    tabControl.add(tabs[i], text = tabtitle[i])

freeram = tk.Label(homeTab, text=ram, font = ("Times", 10))
freeram.grid(column = 0, row = 5, padx = 10, pady = 10)

exit_button = tk.Button(homeTab, text="Exit", font=("Times", 10), command=close)
exit_button.grid(column = 10, row = 10, padx = 10, pady = 10)

# End Assembly
tabControl.grid(column = 1, row = 0, padx = 10, pady = 10)

threading.Thread(target=continueupdate).start()
root.mainloop()
