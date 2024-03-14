"""
salario = int(input("Me diga o seu salario: "))
reducao = (salario * (5/100))
valor_atual = (salario-reducao)
print("Que pena o seu salario diminuiu para", valor_atual)


a=1.5
b=-20

tmp = a
a = b
b = tmp
print (a,b)


tipo = type(a)
print(tipo)
print(type(a))
"""
"""
total = (87426)
segundos = (total % 60)
minutos = (total//60)
horas = (minutos//60)
horas_e_minutos = (minutos%60)
print("O valor em segundos equivale a", total, "em horas equivale a", horas,
      "horas", horas_e_minutos, "minutos", segundos, "segundos")

dias = (horas/24)
meses = (dias//30)
anos = (dias//365)
print("a quantidade de dias é", dias,"a quantidade de meses é", meses,"quantidade de anos é", anos)


a = 4
b = 10
c = 5.0
d = 1
f = 5
print(c == f)


nota1 = float(input("Qual a nota da sua primeira prova? "))
nota2 = float(input("Agora me diga a nota da sua segunda prova: "))
nota3 = float(input("Me diga agora a sua ultima nota: "))

media = (nota1+nota2+nota3)/3

if media >= 6:
    print("aprovado")
if media < 6:
    print("reprovado")
"""

"""

salario = float(input("Me diga o seu salario: "))
if salario >= 3000:
     print("Seu emprestimo foi aprovado, parabens!")
if salario < 3000:
    print("Que pena seu emprestimo foi reprovado :(")
"""
"""

a = 3 > 1
b = 4 > 2
print(a and b) #mostra se é verdadeiro ou falso
"""
"""
teste = 9-4/2<=7+1 or (5*2-3)!=6
print(teste)

teste2 = 9/3==3*3 and 2*3-1>=8
print(teste2)
"""

idade = int(input("Me diga a sua idade: "))
salario = float(input("Me diga o seu salario atual: "))

if idade >= 20 and idade < 80 and salario >= 2500:
    print("Parabéns você tem direito a obter o nosso emprestimo!")
else :
    print("Oh não vemos que você não pode obter o emprestimo, que pena")
