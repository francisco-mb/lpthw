cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Lo que es interesante de estas llamadas es que no es necesario
#  poner espacios a la derecha e izquierda del texto, se insertan
# automáticamente.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "pople today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, 
    "in each car.")