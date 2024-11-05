import os

os.system('pip install -r requirements.txt')
try:
    os.mkdir('assets')
    os.mkdir('SeeamApps')
except:
    print('one of the dirs already exists!')
print('You might need to restart this file to continue!')
import requests
def getonlinefile(url, path):
    req = requests.get(url)
    with open(path, 'wb') as f:
        f.write(req.content)
getonlinefile('https://codeberg.org/psyclown/SEEAM/raw/branch/main/assets/SeeamLogo.png','assets/SeeamLogo.png')
getonlinefile('https://raw.githubusercontent.com/PSYclownYT/OpenWithSEEAM/refs/heads/main/main.py', 'main.py')
getonlinefile('https://raw.githubusercontent.com/PSYclownYT/OpenWithSEEAM/refs/heads/main/InstallGame.py','InstallGame.py')

import tkinter as tk

from tkinter import simpledialog

def prompt_for_name():
    # Open a dialog to prompt the user for their name
    user_name = simpledialog.askstring("Input", "Please enter your name:")
    
    if user_name:  # Check if a name was provided
        with open('assets/userdata.txt','w') as username:
            username.write(user_name)
            root.destroy()
            os.system('python main.py')

# Create the main application window
root = tk.Tk()
root.title("Name Prompt Example")

prompt_for_name()

# Label to display the greeting

# Start the Tkinter event loop
root.mainloop()
