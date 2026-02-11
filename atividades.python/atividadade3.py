contador = 1
soma_notas = 0
while contador<= 4:
    nota = float(input(f"insira a nota do {contador} aluno"))
    soma_notas += nota
    contador +=1
média = soma_notas/4
print("média das  4 notas é:",média)