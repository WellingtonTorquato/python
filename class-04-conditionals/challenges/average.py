# Crie um programa que receba as notas ods alunos
# Faça uma função que calcule a sua média
# Apresente na tela se o aluno foi aprovado (média 7)

def calc_media(nota1, nota2):
  media = (nota1 + nota2) / 2
  return media

try:
  nota1 = float(input("Informe a Nota 1: "))
  nota2 = float(input("Informe a Nota 2: "))
  media = round(calc_media(nota1, nota2), 1)
  if media >= 7:
    print(f"Aprovado com {media}")
  else:
    print(f"Reprovado com {media}")
except ValueError:
    print("Formato inválido!")
except:
    print("Error!")