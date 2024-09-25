n1 = input("digite a primeira nota do aluno:")
n2 = input("digite a segunda nota do aluno:")
n3 = input("digite a terceira nota do aluno:")
n4 = input("digite a quarta nota do aluno:")

n1 = float (n1)
n2 = float (n2)
n3 = float (n3)
n4 = float (n4)


media = float (n1 + n2 + n3 + n4) / 4

if media >=6:
    print("aprovado")
elif media <- 4:
    print("reprovado")
else:
    print("recuperação")