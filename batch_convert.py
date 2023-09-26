import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def select_input_directory():
    input_directory = filedialog.askdirectory()
    input_directory_entry.delete(0, tk.END)
    input_directory_entry.insert(0, input_directory)

def select_output_directory():
    output_directory = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, output_directory)

def convert_to_jpg():
    input_directory = input_directory_entry.get()
    output_directory = output_directory_entry.get()

    if not os.path.exists(input_directory):
        status_label.config(text="Input directory does not exist.", fg="red")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(('.png', '.gif', '.jpeg', '.jpg', '.bmp', '.tiff')):
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_directory, f"{os.path.splitext(file)[0]}.jpg")

                try:
                    image = Image.open(input_file)
                    image.save(output_file, "JPEG")
                except Exception as e:
                    status_label.config(text=f"Error converting {input_file}: {str(e)}", fg="red")
    
    status_label.config(text="Conversion complete.", fg="green")

# Create the main window
root = tk.Tk()
root.title("toJPEG")
root.geometry("230x170")

# Input directory label and entry
input_directory_label = tk.Label(root, text="Input Directory:")
input_directory_label.pack()
input_directory_entry = tk.Entry(root)
input_directory_entry.pack()
input_directory_button = tk.Button(root, text="Browse", command=select_input_directory)
input_directory_button.pack()

# Output directory label and entry
output_directory_label = tk.Label(root, text="Output Directory:")
output_directory_label.pack()
output_directory_entry = tk.Entry(root)
output_directory_entry.pack()
output_directory_button = tk.Button(root, text="Browse", command=select_output_directory)
output_directory_button.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_jpg)
convert_button.pack()

# Status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

# Run the app
root.mainloop()
