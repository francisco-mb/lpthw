i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

print('\n')
print('-' * 10)

def NumerosALista(LimiteSuperior):
    i = 0
    numbers.clear()

    while i < LimiteSuperior:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

NumerosALista(6)