import os
import io
import zipfile
import requests
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from urllib.parse import urlparse
#i messed something up





BG_COLOR = "#527687"
BTN_COLOR = "#3498db"
TEXT_COLOR = "#ecf0f1"
TITLE_FONT = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Helvetica", 14)
LABEL_FONT = ("Helvetica", 12)



class ZipDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seeam Game Installer")
        self.root.geometry("400x250")
        self.root.configure(bg="#527687")  # Light gray background

        self.create_widgets()

    #runScript Function




    def create_widgets(self):
        # URL input
        self.url_label = tk.Label(self.root, text="ZIP URL:", bg=BG_COLOR, font=("Arial", 12))
        self.url_label.pack(pady=(20, 5))

        self.url_entry = tk.Entry(self.root, width=50, font=("Arial", 12), bd=2, relief="solid")
        self.url_entry.pack(pady=5)

        self.command = 'UploadInstall.py'
        # Download & Extract Button
        self.download_button = tk.Button(self.root, text="Download and Extract", command=self.download_and_extract, 
                                          bg='#38bdff', fg="white", font=("Arial", 12), bd=0, padx=10, pady=5)
        self.download_button.pack(pady=(20, 10))

        #upload & extract button
        self.upload_button = tk.Button(self.root, text="Upload From My Device", command=self.run_script, 
                                          bg='#38bdff', fg="white", font=("Arial", 12), bd=0, padx=10, pady=5)
        self.upload_button.pack(pady=(20, 10))

        # Status Label
        self.status_label = tk.Label(self.root, text="", bg=BG_COLOR, font=("Arial", 10))
        self.status_label.pack(pady=5)

    def download_and_extract(self):
        url = self.url_entry.get().strip()
        
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        directory = self.get_directory_from_url(url)

        if not directory:
            messagebox.showwarning("Input Error", "Unable to determine the download directory.")
            return

        try:
            self.download_zip(url, directory)
            self.status_label.config(text=f"Files extracted to {directory}", fg="white")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Download Error", f"Failed to download ZIP file: {e}")
            self.status_label.config(text="", fg="red")
        except zipfile.BadZipFile:
            messagebox.showerror("Extraction Error", "The downloaded file is not a valid ZIP file.")
            self.status_label.config(text="", fg="red")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            self.status_label.config(text="", fg="red")


    def run_script(self):
        os.system('python ' + self.command)



    def get_directory_from_url(self, url):
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path).replace('%20', ' ').rstrip('.zip')
        return os.path.join('SeeamApps', filename)

    def download_zip(self, url, directory):
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error on HTTP errors
        
        # Load the ZIP file in-memory
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist
            zip_file.extractall(directory)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipDownloaderApp(root)
    root.mainloop()
