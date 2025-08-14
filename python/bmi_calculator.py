# BMI Calculator with Health Insights - Python Version

def calculate_bmi(weight, height, units="metric"):
    if units == "imperial":
        height = height * 0.0254  # inches to meters
        weight = weight * 0.453592  # lbs to kg
    return round(weight / (height ** 2), 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def healthy_weight_range(height):
    low = 18.5 * (height ** 2)
    high = 24.9 * (height ** 2)
    return round(low, 1), round(high, 1)

def estimate_body_fat(bmi, age, gender):
    if gender.lower() == "male":
        return round(1.20 * bmi + 0.23 * age - 16.2, 1)
    else:
        return round(1.20 * bmi + 0.23 * age - 5.4, 1)

def calculate_calories(weight, height, age, gender, activity_level="moderate"):
    if gender.lower() == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * (height * 100)) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * (height * 100)) - (4.330 * age)

    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }
    return round(bmr * activity_factors.get(activity_level, 1.55), 0)

if __name__ == "__main__":
    print("=== BMI Calculator ===")
    units = input("Enter units (metric/imperial): ").strip().lower()
    weight = float(input(f"Enter your weight ({'kg' if units == 'metric' else 'lbs'}): "))
    height = float(input(f"Enter your height ({'m' if units == 'metric' else 'inches'}): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")

    bmi = calculate_bmi(weight, height, units)
    category = bmi_category(bmi)
    low_wt, high_wt = healthy_weight_range(height if units == "metric" else height * 0.0254)
    body_fat = estimate_body_fat(bmi, age, gender)
    calories = calculate_calories(weight if units == "metric" else weight * 0.453592, height if units == "metric" else height * 0.0254, age, gender)

    print(f"\nYour BMI: {bmi} ({category})")
    print(f"Healthy weight range: {low_wt} kg - {high_wt} kg")
    print(f"Estimated body fat %: {body_fat}%")
    print(f"Recommended daily calories: {calories} kcal")
