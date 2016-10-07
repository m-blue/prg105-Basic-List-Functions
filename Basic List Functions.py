cars = []
car_input = "0"

while True:
    car_input = raw_input("Enter a type of car: ")
    if car_input == "done":
        break
    else: cars.append(input)

cars.sort()
print cars

print "Hello"
