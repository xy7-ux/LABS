import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


nr_letters = int(input("How many letters would you like in your password?\n"))
random_letters = random.choices(letters, k = nr_letters) #robi to liste z literami
password_letters = "".join(random_letters)
print(password_letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
random_symbols = random.choices(symbols, k = nr_symbols)
password_symbols = "".join(random_symbols)
print(password_symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
random_numbers = random.choices(numbers, k = nr_numbers)
password_numbers = "".join(random_numbers)
print(password_numbers)

password = password_letters + password_symbols + password_numbers
print(password)

shuffled_password = ''.join(random.sample(password,len(password)))
print(shuffled_password)


