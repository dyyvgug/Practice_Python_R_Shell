from math import factorial

num_elements = 20000
num_combinations = int(factorial(num_elements) / (factorial(num_elements - 2)*factorial(2)))

print(f"Number of C(20000,2) is {num_combinations}")