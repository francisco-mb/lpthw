from codecs import backslashreplace_errors
from turtle import back


tabby_cat = "\tI'm tabbed in."
persiona_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persiona_cat)
print(backslash_cat)
print(fat_cat)