notas = [7.5, 8.0, 6.5, 9.0]
media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)
print(f"As notas são: {notas}")
print(f"A média final é: {media:.2f}")
print(f"A maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")

if media >= 7:
  print("APROVADO")
else:
  nota_prova_final = 8.0
  notas.append(nota_prova_final)
  media = sum(notas) / len(notas)
  print(f"Nota da prova final adicionada: {nota_prova_final}")
  print(f"Nova média é: {media:.2f}")
  if media >= 5:
    print("APROVADO")
  else:
    print("REPROVADO")