#Problem 1 - BMI

# Input
weight_pounds = float(input("Enter weight (pounds): "))
height_inches = float(input("Enter height (inches): "))

# Processing
bmi_imperial = (weight_pounds / (height_inches ** 2)) * 703

weight_kgs = weight_pounds * 0.453592
height_meters = height_inches * 0.0254

bmi_metric = weight_kgs / (height_meters ** 2)

# Output
print(f"BMI Imperial value for a person height (in) of {height_inches} and of weight (lbs) {weight_pounds} =", round(bmi_imperial, 1))
print("BMI Metric value =", round(bmi_metric, 1))


#Problem 2 - Vehicule Routing

# Input
time_hrs = float(input("Enter total duration of trip (hours): "))
speed_mph = float(input("Enter average speed of car (mph): "))

# Processing
distance = time_hrs * speed_mph

# Display
print(f"Total distance travelled is {distance} miles")

# The shortest route type is local