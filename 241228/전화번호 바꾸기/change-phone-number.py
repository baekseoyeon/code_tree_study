number = input()
number = number.split("-")
number[1],number[2] = number[2],number[1]
new_number = "-".join(number)
print(new_number)