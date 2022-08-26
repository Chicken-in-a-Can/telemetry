# Import modules

# Tkinter for GUI window
import tkinter as tk
from tkinter import ttk
# OS for system interaction
import os

# System Vars
usbs = os.popen("lsusb").read()


# Methods


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


# End Assembly
tabControl.grid(column = 1, row = 0, padx = 10, pady = 10)
root.mainloop()
