from datetime import date, timedelta

hoje = date.today()
dois_dias_futuro = hoje + timedelta(days=2)
print(f"A data daqui a dois dias: {dois_dias_futuro}")
print(f"A data de hoje é: {hoje}")