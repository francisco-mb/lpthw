from sys import argv, orig_argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("I'm going to ask you for three lines and write these to the file.")

target.write(input("line 1: "))
target.write("\n")
target.write(input("line 2: "))
target.write("\n")
target.write(input("line 3: "))
target.write("\n")

print("And finally, we close it.")
target.close()