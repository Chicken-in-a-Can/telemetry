#!/usr/bin/python

# Import modules

# Tkinter for GUI window
import tkinter as tk
from tkinter import ttk
# OS for linux system interaction
import os
# Threading for multithreading for updating
import threading
# Time for wait commands to reduce system load
import time

# Define basic variables
no_update_str = "Tab hasn't currently updated. Oopsies"

# Methods

# Just close window
def close():
    root.quit()

# Update home tab. Update all text labels on home tab
def update_home():
    thecmd = os.popen("free -h").read()
    home_info_one.config(text = thecmd)

# Update main power tab. Update all text labels on main power tab
def update_main_power():
    thecmd = os.popen("date +'TIME: %T'").read()
    main_power_info_one.config(text = thecmd)

# Update aux power tab. Update all text labels on aux power tab
def update_aux_power():
    thecmd = os.popen("upower -i $(upower -e | grep BAT)").read()
    aux_power_info_one.config(text = thecmd)

# Permanantly run update switcher method every 1/10th of a second
def continueupdate():
    while True:
        tabupdatechanger()
        time.sleep(0.1)

# Only update labels on current tab to increase speed and reduce system load
def tabupdatechanger():
    # Get index position of current tab
    tab_index = tabControl.index(tabControl.select())
    # Match case for index of tab
    match tab_index:
        case 0:
            update_home()
        case 1:
            update_main_power()
        case 2:
            update_aux_power()

# Main code start

# Window Attributes

# Create main window
root = tk.Tk()

# Set title to 'Solar Car Telemetry'
root.title("Solar Car Telemetry")

# Set window to fullscreen
root.attributes("-fullscreen", True)

# Tab initialization

# Create tkinter notebook for tabs
tabControl = ttk.Notebook(root)

# Create new tabs
homeTab = ttk.Frame(tabControl)
powerTab = ttk.Frame(tabControl)
auxTab = ttk.Frame(tabControl)

# Place tabs in array for convenient adding to notebook
# Tabs in tabs and tabtitle must match indexes
tabs = [homeTab, powerTab, auxTab]
tabtitle = ["Home", "Main Power", "Auxiliary Power"]

# Add tabs to notebook through for loop
for i in range(len(tabs)):
    tabControl.add(tabs[i], text = tabtitle[i])


# Tab not specific items

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Times", 10), command=close, anchor = "w")
exit_button.grid(column = 10, row = 10, padx = 10, pady = 10)

# Home Tab

# First info label on home tab. Plain text
home_info_one = tk.Label(homeTab, text=no_update_str, font = ("Times", 10))
home_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)

# Main Power Tab

# First info label on main power tab. Plain text
main_power_info_one = tk.Label(powerTab, text=no_update_str, font = ("Times", 10))
main_power_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)

# Auxiliary Power Tab

# First info label on main power tab. Plain text
aux_power_info_one = tk.Label(auxTab, text=no_update_str, font = ("Times", 10))
aux_power_info_one.grid(column = 0, row = 5, padx = 10, pady = 10)

# End Assembly
tabControl.grid(column = 1, row = 0, padx = 10, pady = 10)

# Start thread for updating
update_thread = threading.Thread(target=continueupdate)
update_thread.start()

# Loop tkinter window (required)
root.mainloop()
