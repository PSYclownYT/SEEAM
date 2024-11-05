# Tkinter GUI for Uploading and Extracting ZIP Files

import tkinter as tk
from tkinter import filedialog
import zipfile
import os


def upload_and_extract():
    zip_file_path = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if zip_file_path:
        zip_file_name = os.path.basename(zip_file_path).replace('.zip', '')
        extract_path = os.path.join(os.getcwd(), "SeeamApps", zip_file_name)
        os.makedirs(extract_path, exist_ok=True)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            return("Extraction Complete!")

upload_and_extract()