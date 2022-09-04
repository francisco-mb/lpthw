# Declara una varible de tipo string
types_of_people = 10
# Declara un string-f
x = f"There are {types_of_people} types of people."

# Declara dos variables de tipo string
binary = "binary"
do_not = "don't"
# Declara un string-f con dos variables
y = f"Those who know {binary} and those who {do_not}."

# Imprime las dos string-f anteriores
print(x)
print(y)

# Imprime string-f cuyo argumento es otro string-f
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Declaración de boolean
hilarious = False
# Declaración de un string que admite un parámetro pero este está sin
# asignar
joke_evaluation = "Isn't that joke so funny?! {}"
# Imprime el string pasado sustituyendo argumentos por el pasado
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# Concatenación de string
print(w + e)