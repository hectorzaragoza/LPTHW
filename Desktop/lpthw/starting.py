#Exercise 1
print("Hello, World!")
print("Hello Again!")
print("I like typing this.")
print("This is fun.")
print("Yay! Printing.")
print("I'd mych rather you 'not'.")
print('I "said" do not touch this.')

#Exercise 2
print("I will now count my chickens:")

print("Hens", int(25 + 30 / 6))
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

#Exercise 3
cars = 100
carspace = 4
drivers = 30
passengers = 90
cars_notdriven = cars - drivers
driven_cars = drivers
carpool_capacity = driven_cars * carspace
avg_passenger_per_car = passengers / driven_cars

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_notdriven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about",int(avg_passenger_per_car), "in each car.")