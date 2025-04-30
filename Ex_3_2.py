def generate_square_dict(n):
  output_dict = {}
  for num in range(1, n+1):
    output_dict[num] = num**2
  return output_dict

result = generate_square_dict(8)
print(result)