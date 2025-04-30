import math

def calculate_q_values_simples(d_values_string):
  C = 50
  H = 30
  d_values = d_values_string.split(',')
  q_values = []
  for d in d_values:
    d_float = float(d.strip())
    q = math.sqrt((2 * C * d_float) / H)
    q_rounded = round(q)
    q_values.append(str(q_rounded))
  return ",".join(q_values)

entrada = "100,150,180"
resultado = calculate_q_values_simples(entrada)
print(resultado)