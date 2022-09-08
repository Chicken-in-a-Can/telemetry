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

def update_home():
    thecmd = os.popen("free -h").read()
    home_info_one.config(text = thecmd)

def update_main_power():
    thecmd = os.popen("date +'TIME: %T'").read()
    main_power_info_one.config(text = thecmd)

def update_aux_power():
    thecmd = os.popen("upower -i $(upower -e | grep BAT)").read()
    aux_power_info_one.config(text = thecmd)

def continueupdate():
    while True:
        tabupdatechanger()
        time.sleep(0.1)

def tabupdatechanger():
    tab_index = tabControl.index(tabControl.select())
    match tab_index:
        case 0:
            update_home()
        case 1:
            update_main_power()
        case 2:
            update_aux_power()

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

# Home Tab
home_info_one = tk.Label(homeTab, text=ram, font = ("Times", 10))
home_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)

exit_button = tk.Button(homeTab, text="Exit", font=("Times", 10), command=close, anchor = "w")
exit_button.grid(column = 10, row = 10, padx = 10, pady = 10)



# Main Power Tab
main_power_info_one = tk.Label(powerTab, text=ram, font = ("Times", 10))
main_power_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)



# Auxillary Power Tab
aux_power_info_one = tk.Label(auxTab, text=ram, font = ("Times", 10))
aux_power_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)



# End Assembly
tabControl.grid(column = 1, row = 0, padx = 10, pady = 10)

threading.Thread(target=continueupdate).start()
root.mainloop()
