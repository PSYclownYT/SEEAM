import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from pathlib import Path

# Assuming name is fetched from a file
user_data_path = Path("assets/userdata.txt")
if user_data_path.exists():
    with open(user_data_path) as f:
        name = f.read()
else:
    name = "User"

# Setting up app assets directory
logo_path = Path("assets/SeeamLogo.png")

# Define primary color scheme
BG_COLOR = "#2c3e50"
BTN_COLOR = "#3498db"
TEXT_COLOR = "#ecf0f1"
TITLE_FONT = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Helvetica", 14)
LABEL_FONT = ("Helvetica", 12)

# Path to InstallGame.py
install_game_script = Path("ServerInstall.py")

def run_script(script_name):
    """Run a Python script located at script_name."""
    print(f'Running script: {script_name}')
    os.system(f'python "{script_name}"')

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
    extra_script_path = game_dir / "extras.py"

    # Thumbnail Image
    if thumbnail_path.exists():
        thumbnail_img = Image.open(thumbnail_path).resize((800, 400))
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

    # Extra Script Button (new button to run the additional script)
    if extra_script_path.exists():
        extra_script_button = tk.Button(
            main_content,
            text="Extras",
            command=lambda: run_script(extra_script_path),
            font=BUTTON_FONT,
            bg="#e74c3c",  # Red color for differentiation
            fg=TEXT_COLOR,
            relief="flat",
            bd=0,
            width=20
        )
        extra_script_button.pack(pady=10)

def create_buttons_with_sidebar_and_logo():
    # Main window setup
    window = tk.Tk()
    window.title("Epic App Launcher")
    window.geometry("1280x720")
    window.configure(bg=BG_COLOR)

    # Sidebar frame for game list
    sidebar = tk.Frame(window, width=300, bg="#1e272e")
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
        bg="#1e272e"
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
