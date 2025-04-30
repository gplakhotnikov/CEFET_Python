class InputOutString:
  def __init__(self):
    self.s = ""

  def get_string(self):
    self.s = input("Digite um string: ")

  def print_string(self):
    print(self.s.upper())

def test_input_out_string():
  str_obj = InputOutString()
  print("Executando método get_string")
  str_obj.get_string()
  print("Executando método print_string")
  str_obj.print_string()

test_input_out_string()