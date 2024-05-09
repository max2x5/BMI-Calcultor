import tkinter as tk
import maleFunc as m
import femaleFunc as f
import questions as q

def calculate_bmi():
    gender = gender_var.get()
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100

    bmi = weight / height**2
    if gender == 'male':
        result = m.match_age(age, bmi)
    else:
        result = f.match_age(age, bmi)

    bmi_value_label.config(text=f"BMI: {bmi:.2f}")
    interpretation_label.config(text=f"Interpretation: {result}")

root = tk.Tk()
root.title("BMI Calculator")

header_label = tk.Label(root, text="BMI Calculator", font=("Helvetica", 24, "bold"))
header_label.pack(pady=20)

gender_label = tk.Label(root, text="Gender:")
gender_label.pack(anchor="w", padx=20)  # Wyrównanie do lewej krawędzi z odstępem po lewej

gender_var = tk.StringVar()
gender_var.set("male")
male_button = tk.Radiobutton(root, text="Male", variable=gender_var, value="male")
male_button.pack(anchor="w", padx=20)  # Wyrównanie do lewej krawędzi z odstępem po lewej
female_button = tk.Radiobutton(root, text="Female", variable=gender_var, value="female")
female_button.pack(anchor="w", padx=20)  # Wyrównanie do lewej krawędzi z odstępem po lewej

age_label = tk.Label(root, text="Age:")
age_label.pack(anchor="w", padx=20)
age_entry = tk.Entry(root)
age_entry.pack(anchor="w", padx=20)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(anchor="w", padx=20)
weight_entry = tk.Entry(root)
weight_entry.pack(anchor="w", padx=20)

height_label = tk.Label(root, text="Height (cm):")
height_label.pack(anchor="w", padx=20)
height_entry = tk.Entry(root)
height_entry.pack(anchor="w", padx=20)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

bmi_value_label = tk.Label(root, text="", font=("Helvetica", 12))
bmi_value_label.pack()
interpretation_label = tk.Label(root, text="", font=("Helvetica", 12))
interpretation_label.pack()

root.mainloop()
