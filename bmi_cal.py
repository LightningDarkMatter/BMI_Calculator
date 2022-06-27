height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

h_float = float(height)
w_int = int(weight)

bmi = w_int / (h_float * h_float)

final_bmi = round(bmi)

result = print("Your BMI is: " + str(final_bmi))
