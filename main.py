# body mass index is calculated using the formula mass / height squared

mass = int(input("Enter your mass in kilograms : "))
height = float(input("Enter your height in metres : "))
bmi = mass / height ** 2
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You are of normal weight")
elif bmi < 29.9:
    print("You are overweight")
elif bmi >= 30:
    print("You are obese")

