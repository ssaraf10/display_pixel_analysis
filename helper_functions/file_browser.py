import tkinter as tk
from tkinter import filedialog


def browse_file_dialog():
    root = tk.Tk()
    root.withdraw()
    filetypes = (("All files", "*.*"))

    file_path = filedialog.askopenfilename(title=f"select image file", filetypes=filetypes)
    return file_path
