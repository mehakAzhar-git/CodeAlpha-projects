import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def select_source():
    folder = filedialog.askdirectory(
        title="Select Source Folder"
    )

    if folder:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder)


def select_destination():
    folder = filedialog.askdirectory(
        title="Select Destination Folder"
    )

    if folder:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder)


def move_jpg_files():

    source = source_entry.get()
    destination = destination_entry.get()

    if not source or not destination:
        messagebox.showwarning(
            "Missing Folder",
            "Please select both folders."
        )
        return

    if not os.path.exists(source):
        messagebox.showerror(
            "Error",
            "Source folder does not exist."
        )
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    moved_files = 0

    for filename in os.listdir(source):

        if filename.lower().endswith(".jpg"):

            source_file = os.path.join(
                source,
                filename
            )

            destination_file = os.path.join(
                destination,
                filename
            )

            shutil.move(
                source_file,
                destination_file
            )

            moved_files += 1

    result_label.config(
        text=f"{moved_files} JPG file(s) moved successfully."
    )

    messagebox.showinfo(
        "Task Complete",
        f"{moved_files} JPG file(s) moved successfully!"
    )


# Main Window
root = tk.Tk()

root.title("JPG File Automation")
root.geometry("700x450")
root.resizable(False, False)


title = tk.Label(
    root,
    text="JPG FILE AUTOMATION",
    font=("Arial", 24, "bold")
)

title.pack(pady=25)


# Source folder
source_label = tk.Label(
    root,
    text="Source Folder",
    font=("Arial", 14, "bold")
)

source_label.pack(pady=5)


source_frame = tk.Frame(root)
source_frame.pack()


source_entry = tk.Entry(
    source_frame,
    width=50,
    font=("Arial", 11)
)

source_entry.pack(side=tk.LEFT, padx=5)


source_button = tk.Button(
    source_frame,
    text="Browse",
    command=select_source,
    width=10
)

source_button.pack(side=tk.LEFT)


# Destination folder
destination_label = tk.Label(
    root,
    text="Destination Folder",
    font=("Arial", 14, "bold")
)

destination_label.pack(pady=(25, 5))


destination_frame = tk.Frame(root)
destination_frame.pack()


destination_entry = tk.Entry(
    destination_frame,
    width=50,
    font=("Arial", 11)
)

destination_entry.pack(side=tk.LEFT, padx=5)


destination_button = tk.Button(
    destination_frame,
    text="Browse",
    command=select_destination,
    width=10
)

destination_button.pack(side=tk.LEFT)


# Move button
move_button = tk.Button(
    root,
    text="MOVE JPG FILES",
    font=("Arial", 14, "bold"),
    command=move_jpg_files,
    width=20
)

move_button.pack(pady=35)


# Result
result_label = tk.Label(
    root,
    text="Ready to automate...",
    font=("Arial", 13)
)

result_label.pack()


root.mainloop()


