import random
def generate_even_numbers():
  even_numbers = [num for num in range(150, 251) if num % 2 == 0]
  return random.sample(even_numbers, 5)

resultado = generate_even_numbers()
print(resultado)