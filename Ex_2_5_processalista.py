def maior_impar(lista):
   return max(filter(lambda num : num%2 != 0, lista))
def menor_impar(lista):
   return min(filter(lambda num : num%2 != 0, lista))
def maior_menor_impar(lista):
   return maior_impar(lista), menor_impar(lista)
