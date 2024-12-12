import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import threading
from pathlib import Path
import preferredsoundplayer.preferredsoundplayer as psp
import json
import pickle

import pickle

# Load variables from the pickle file

def reduce_brightness(hex_color, factor=0.5):
    """Reduces the brightness of a given hex color.

    Args:
        hex_color (str): The hex color code (e.g., "#ff0000").
        factor (float): The factor to reduce brightness by (0.0 - 1.0).

    Returns:
        str: The new hex color code.
    """

    # Convert hex color to RGB values
    r, g, b = [int(hex_color[i:i + 2], 16) for i in range(1, 6, 2)]

    # Reduce brightness by multiplying each RGB component by the factor
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)

    # Convert RGB values back to hex color code
    return f"#{r:02x}{g:02x}{b:02x}"




def load_variables():
    try:
        with open("theme.pkl", "rb") as file:
            variables = pickle.load(file)
        return variables
    except FileNotFoundError:
        print("The file 'variables.pkl' does not exist. Using default values.")
        return {
            "BG_COLOR": "#2c3e50",
            "BTN_COLOR": "#3498db",
            "TEXT_COLOR": "#ecf0f1",
            "TITLE_FONT": ("Helvetica", 16, "bold"),
            "BUTTON_FONT": ("Helvetica", 14),
            "LABEL_FONT": ("Helvetica", 12)
        }

# Example usage
variables = load_variables()

# Access the loaded variables
BG_COLOR = variables["BG_COLOR"]
BTN_COLOR = variables["BTN_COLOR"]
TEXT_COLOR = variables["TEXT_COLOR"]
TITLE_FONT = variables["TITLE_FONT"]
BUTTON_FONT = variables["BUTTON_FONT"]
LABEL_FONT = variables["LABEL_FONT"]

SB_COLOR = reduce_brightness(BG_COLOR, 0.7)

# Assuming name is fetched from a file
user_data_path = Path("assets/userdata.txt")
if user_data_path.exists():
    with open(user_data_path) as f:
        name = f.read()
else:
    name = "User"

# Setting up app assets directory
logo_path = Path("assets/SeeamLogo.png")

# Path to InstallGame.py
install_game_script = Path("ServerInstall.py")

def run_script(script_name):
    """Run a Python script in a separate thread."""
    def target():
        try:
            psp.playsound('assets/launch.mp3')  # Play sound before starting the script
            os.system(f'python "{script_name}"')  # Run the script
        except Exception as e:
            print(f"Error running script {script_name}: {e}")

    # Create and start a new thread
    thread = threading.Thread(target=target)
    thread.daemon = True  # Ensure the thread will close when the main program exits
    thread.start()

# Adjust directory paths
games_dir = Path("SeeamApps")

def display_game_details_from_dir(game_name):
    """Update main content area to display selected game details based on directory structure."""
    for widget in main_content.winfo_children():
        widget.destroy()

    game_dir = games_dir / game_name
    thumbnail_path = game_dir / "thumbnail.png"
    description_path = game_dir / "description.txt"
    script_path = game_dir / "main.py"
    buttons_json = game_dir / "buttons.json"
    extras_path = game_dir / "extras.py"

    # Thumbnail Image
    if thumbnail_path.exists():
        thumbnail_img = Image.open(thumbnail_path).resize((800, 450))
        thumbnail_photo = ImageTk.PhotoImage(thumbnail_img)
        thumbnail_label = tk.Label(main_content, image=thumbnail_photo, bg=BG_COLOR)
        thumbnail_label.image = thumbnail_photo
        thumbnail_label.pack(pady=(10, 10))

    # Game Description
    if description_path.exists():
        with open(description_path, "r") as desc_file:
            description = desc_file.read()
    else:
        description = "No description available."

    description_label = tk.Label(
        main_content,
        text=description,
        font=LABEL_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR,
        wraplength=500,
        justify="left"
    )
    description_label.pack(pady=10)

    # Play Button
    play_button = tk.Button(
        main_content,
        text="Play",
        command=lambda: run_script(script_path),
        font=BUTTON_FONT,
        bg=BTN_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        bd=0,
        width=15
    )
    play_button.pack(pady=20)

    # Extra Buttons from buttons.json
    if buttons_json.exists():
        with open(buttons_json, "r") as file:
            buttons_data = json.load(file)  # Parse the JSON file

            # Loop through each button entry
            for key, button_info in buttons_data.items():
                color = button_info.get("Color", BTN_COLOR)
                text = button_info.get("Text", "Unnamed Button")
                file_path = button_info.get("File")

                # Check if file_path exists before creating the button
                if file_path:
                    extra_button = tk.Button(
                        main_content,
                        text=text,
                        command=lambda fp=game_dir / file_path: run_script(fp),
                        font=BUTTON_FONT,
                        bg=color,
                        fg=TEXT_COLOR,
                        relief="flat",
                        bd=0,
                        width=20
                    )
                    extra_button.pack(pady=10)
    elif extras_path.exists():
        extra_button = tk.Button(
            main_content,
            text="Extras",
            command=run_script("extras.py"),
            font=BUTTON_FONT,
            bg="red",
            fg=TEXT_COLOR,
            relief="flat",
            bd=0,
            width=20
        )
        extra_button.pack(pady=10)

def create_buttons_with_sidebar_and_logo():
    # Main window setup
    window = tk.Tk()
    window.title("Epic App Launcher")
    window.geometry("1280x720")
    window.configure(bg=BG_COLOR)

    # Sidebar frame for game list
    sidebar = tk.Frame(window, width=300, bg=SB_COLOR)
    sidebar.pack(side="left", fill="y")

    # Logo at the top of the sidebar
    if logo_path.exists():
        logo = Image.open(logo_path).resize((150, 75))
        logo_image = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(sidebar, image=logo_image, bg="#1e272e")
        logo_label.image = logo_image
        logo_label.pack(pady=(20, 10))

    # Sidebar label for "Available Games"
    sidebar_label = tk.Label(
        sidebar,
        text="Available Games",
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg=SB_COLOR
    )
    sidebar_label.pack(pady=(10, 20))

    # Dynamically add buttons for each game in the directory
    if games_dir.exists():
        for game_folder in games_dir.iterdir():
            if game_folder.is_dir():
                button = tk.Button(
                    sidebar,
                    text=game_folder.name,
                    command=lambda name=game_folder.name: display_game_details_from_dir(name),
                    font=BUTTON_FONT,
                    bg=BTN_COLOR,
                    fg=TEXT_COLOR,
                    relief="flat",
                    bd=0,
                    width=20
                )
                button.pack(pady=10)

    # Install Game Button - Always Visible on the Sidebar
    if install_game_script.exists():
        install_button = tk.Button(
            sidebar,
            text="Install More Games",
            command=lambda: run_script(install_game_script),
            font=BUTTON_FONT,
            bg="#1abc9c",  # Different color for installation
            fg=TEXT_COLOR,
            relief="flat",
            bd=0,
            width=20
        )
        install_button.pack(pady=(30, 10))  # Add padding to position it below the game list

    # Main content area
    global main_content
    main_content = tk.Frame(window, bg=BG_COLOR)
    main_content.pack(side="left", fill="both", expand=True)

    # Initial welcome message in main content area
    welcome_label = tk.Label(
        main_content,
        text=f'Welcome, {name}! Select a game to see details.',
        font=TITLE_FONT,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    welcome_label.pack(pady=20)
    window.attributes('-fullscreen', True)
    window.mainloop()

create_buttons_with_sidebar_and_logo()
