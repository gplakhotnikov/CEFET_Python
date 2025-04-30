def convert_input_to_list_and_tuple(input_string):
  string_list = input_string.split(',')
  output_list = [item for item in string_list]
  output_tuple = tuple(string_list)
  return (output_list, output_tuple)

entrada = "3,6,5,3,2,8"
print(convert_input_to_list_and_tuple(entrada))