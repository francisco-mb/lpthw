name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Conversión a SMD
height_cm = round(height * 2.54, 2)
weight_kg = round(weight * 0.4535924, 2)

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimetes tall.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffe.")

# this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")