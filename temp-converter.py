import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        label_result.config(text="Please enter a valid Celsius value!")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        label_result.config(text="Please enter a valid Fahrenheit value!")

# Function to clear all inputs and results
def clear_all():
    entry_celsius.delete(0, tk.END)
    entry_fahrenheit.delete(0, tk.END)
    label_result.config(text="")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x400")
root.resizable(False, False)

# Add a title label
label_title = tk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"))
label_title.pack(pady=10)

# Section for Celsius to Fahrenheit
frame_c_to_f = tk.Frame(root)
frame_c_to_f.pack(pady=10)

label_celsius = tk.Label(frame_c_to_f, text="Celsius (°C):", font=("Arial", 12))
label_celsius.grid(row=0, column=0, padx=10, pady=5)

entry_celsius = tk.Entry(frame_c_to_f, font=("Arial", 12), width=15)
entry_celsius.grid(row=0, column=1, padx=10, pady=5)

button_c_to_f = tk.Button(frame_c_to_f, text="Convert to Fahrenheit", font=("Arial", 12), command=celsius_to_fahrenheit)
button_c_to_f.grid(row=0, column=2, padx=10, pady=5)

# Section for Fahrenheit to Celsius
frame_f_to_c = tk.Frame(root)
frame_f_to_c.pack(pady=10)

label_fahrenheit = tk.Label(frame_f_to_c, text="Fahrenheit (°F):", font=("Arial", 12))
label_fahrenheit.grid(row=0, column=0, padx=10, pady=5)

entry_fahrenheit = tk.Entry(frame_f_to_c, font=("Arial", 12), width=15)
entry_fahrenheit.grid(row=0, column=1, padx=10, pady=5)

button_f_to_c = tk.Button(frame_f_to_c, text="Convert to Celsius", font=("Arial", 12), command=fahrenheit_to_celsius)
button_f_to_c.grid(row=0, column=2, padx=10, pady=5)

# Section for Result
label_result = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="blue")
label_result.pack(pady=20)

# Section for Clear Button
button_clear = tk.Button(root, text="Clear All", font=("Arial", 12), command=clear_all, bg="red", fg="white")
button_clear.pack(pady=10)

# Footer Label
label_footer = tk.Label(root, text="Created for Beginners in Python GUI Programming", font=("Arial", 10, "italic"), fg="gray")
label_footer.pack(side=tk.BOTTOM, pady=10)

# Run the application
root.mainloop()
