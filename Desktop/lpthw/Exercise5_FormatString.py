#Exercise 5
#More Variables and Printing
# Format String - How to make strings with embedded variables.
#You embed variables inside a string using the curly brackets {} and then put the variable you want inside the {} characters. 
#You must also start the string with the letter f for "format". The f tells python to insert variable value in the {}
#e.g. f"Hello {somevar}

name = "Hector"
age = 33
height = 1.75
weight = 200 
eyes = "brown"
teeth = "white"
my_hair = "black"

print(f"Hi, my name is {name}.")
print(f"I am {age} years old.")
print(f"I am about {weight} pounds.")
print("And that is actually not that heavy.")
print(f"My eyes are {eyes}, my teeth are {teeth} and my hair is {my_hair}.")


american_height = height * round(39.3701)
print(f"My height in America is {american_height}.")
