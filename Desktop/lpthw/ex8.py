#Ex 8

formatter = "{} {} {} {}"

print(formatter.format(1 , 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "My name is Hector.",
    "And I have no fear.",
    "I have no fear because...",
    "there is nothing to fear."
))