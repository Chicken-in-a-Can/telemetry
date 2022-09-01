#!/usr/bin/python
# Import modules

# Tkinter for GUI window
import tkinter as tk
from tkinter import ttk
# OS for system interaction
import os

# System Vars
usbs = os.popen("cat /etc/os-release").read()
pings = os.popen("lsusb").read()


# Methods
def close():
    root.quit()

def update():
    thecmd = os.popen("lsusb").read()
    lsusb.config(text = thecmd)

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

lsusb = tk.Label(homeTab, text=pings, font = ("Times", 10))
lsusb.grid(column = 0, row = 5, padx = 10, pady = 10)

the_button = tk.Button(homeTab, text="update", command = update)
the_button.grid(column = 1, row = 10, padx = 10, pady = 10)

exit_button = tk.Button(homeTab, text="Exit", font=("Times", 10), command=close)
exit_button.grid(column = 10, row = 10, padx = 10, pady = 10)

# End Assembly
tabControl.grid(column = 1, row = 0, padx = 10, pady = 10)

def updater():
    try:
        ping2 = os.popen("lsusb").read()
        if pings != ping2:
            update()
            pings = os.popen("lsusb")
        ping2 = os.popen("lsusb").read()
    except NameError:
        pings = os.popen("lsusb").read()

root.after(1000, updater())
root.mainloop()
