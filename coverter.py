import tkinter as tk
from tkinter import messagebox

def convert():
    input_value = entry.get()
    conversion_type = conversion_var.get()
    
    try:
        if conversion_type == "Binary to Text":
            text = ''.join(chr(int(b, 2)) for b in input_value.split())
            result_label.config(text=f"Result: {text}")
        elif conversion_type == "Text to Binary":
            binary = ' '.join(format(ord(c), '08b') for c in input_value)
            result_label.config(text=f"Result: {binary}")
        elif conversion_type == "ASCII to Text":
            text = ''.join(chr(int(a)) for a in input_value.split())
            result_label.config(text=f"Result: {text}")
        elif conversion_type == "Text to ASCII":
            ascii_values = ' '.join(str(ord(c)) for c in input_value)
            result_label.config(text=f"Result: {ascii_values}")
        else:
            messagebox.showerror("Error", "Invalid conversion type selected")
    except ValueError:
        messagebox.showerror("Error", "Invalid input format")

# Create main window
root = tk.Tk()
root.title("Binary & ASCII Converter")
root.geometry("400x250")

# Input field
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Dropdown for conversion type
conversion_var = tk.StringVar(value="Binary to Text")
conversion_menu = tk.OptionMenu(root, conversion_var, "Binary to Text", "Text to Binary", "ASCII to Text", "Text to ASCII")
conversion_menu.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()
