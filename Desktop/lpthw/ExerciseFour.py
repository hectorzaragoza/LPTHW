#Exercise 6 Strings and Text

PeopleTypes = 10
x = f"There are {PeopleTypes} types of people."

binary = "binary"
do_not = "dont"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w)
print(e)
print(w + e)