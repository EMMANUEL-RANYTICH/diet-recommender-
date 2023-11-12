import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161
    return bmr

def recommend_diet_plan(bmi, bmr):
    if bmi < 18.5:
        return "Underweight - Recommended diet: Increase calorie intake and focus on nutrient-dense foods."
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight - Recommended diet: Maintain a balanced diet with a variety of fruits, vegetables, whole grains, and lean proteins."
    elif bmi >= 25 and bmi < 30:
        return "Overweight - Recommended diet: Reduce calorie intake, limit processed foods, and increase physical activity."
    else:
        return "Obese - Recommended diet: Consult a healthcare professional for personalized advice."

def calculate_and_recommend():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        gender = gender_var.get()

        bmi = calculate_bmi(weight, height)
        bmr = calculate_bmr(weight, height, age, gender)
        diet_plan = recommend_diet_plan(bmi, bmr)

        result = f"BMI: {bmi:.2f}\nBMR: {bmr:.2f}\nDiet Plan: {diet_plan}"
        messagebox.showinfo("Result", result)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid input.")

# Create the main window
window = tk.Tk()
window.title("BMI and BMR Calculator")

# Create and place labels and entry fields
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (m):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar()
gender_var.set("Male")
gender_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
gender_male.pack()
gender_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
gender_female.pack()

calculate_button = tk.Button(window, text="Calculate and Recommend", command=calculate_and_recommend)
calculate_button.pack()

# Start the main event loop
window.mainloop()