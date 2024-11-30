import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        # Get weight, height, and age from user input
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert height from cm to meters
        age = int(age_entry.get())  # Get the age
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Update the result label with BMI
        result_label.config(text=f"BMI: {bmi:.2f}", font=("Arial", 24, "bold"))
        
        # Categorize the BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        category_label.config(text=f"Category: {category}", font=("Arial", 14, "bold"))
        age_label.config(text=f"Age: {age}", font=("Arial", 14, "bold"))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight, height, and age.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.config(bg="lightblue")

# Add a title label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=20)

# Weight entry
weight_label = tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="lightblue", fg="darkblue")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height entry
height_label = tk.Label(root, text="Height (cm):", font=("Arial", 12), bg="lightblue", fg="darkblue")
height_label.pack(pady=5)
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Age entry
age_label = tk.Label(root, text="Age:", font=("Arial", 12), bg="lightblue", fg="darkblue")
age_label.pack(pady=5)
age_entry = tk.Entry(root, font=("Arial", 12))
age_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), bg="green", fg="white", command=calculate_bmi)
calculate_button.pack(pady=20)

# BMI result label
result_label = tk.Label(root, text="BMI: ", font=("Arial", 24, "bold"), bg="lightblue", fg="darkblue")
result_label.pack(pady=10)

# BMI category label
category_label = tk.Label(root, text="Category: ", font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue")
category_label.pack(pady=10)

# Age display label
age_label = tk.Label(root, text="Age: ", font=("Arial", 14, "bold"), bg="lightblue", fg="darkblue")
age_label.pack(pady=10)

# Run the application
root.mainloop()
