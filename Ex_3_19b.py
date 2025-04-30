import random
def generate_random_numbers():
  return random.sample(range(150, 251), 5)

resultado = generate_random_numbers()
print(resultado)