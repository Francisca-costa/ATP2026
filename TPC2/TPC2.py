###TPC2

import random 
print("(1) O computador escolhe o número")
print("(2) Eu escolho o número")

a=int(input("Deseja jogar em que modo?"))
n1=random.randint(1,100)
def jogo(a):
    if a==1:
        def computador(n1):
        
            palpite=int(input("Diga que número é que acha que o computador escolheu."))
            i=1
            while palpite!=n1:
                if palpite<n1:
                    print(f"O número que escolhi é maior que: {palpite}")
                    palpite=int(input("Diga que número é que acha que o computador escolheu."))
                    i=i+1
                else:
                    print(f"O número quee escolhi é menor que: {palpite}")
                    palpite=int(input("Diga que número é que acha que o computador escolheu."))
                    i=i+1
            if palpite==n1:
                print(f"O número que escolhi é: {n1}")
                print(f"Número de tentativas: {i}")
        computador(n1)
    else:    
        def eu():
            minimo=1
            maximo=100
            n2=int(input("Que número é que escolhe"))
            palpite2=random.randint(minimo,maximo)
            print(f"O computador acha que escolheu o número: {palpite2}")
            i=1
            pergunta=input(f"O número que escolheu é igual,maior ou menor que {palpite2}.(i/M/m) ")
            acertou=False
            while not acertou:
                if pergunta=="I" or pergunta=="i":
                    acertou=True
                elif pergunta=="M":
                    print(f"O número que escolhi é maior que: {palpite2}")
                    minimo=palpite2+1
                    palpite2=random.randint(minimo,maximo)
                    i=i+1
                    pergunta=input(f"O número que escolheu é igual,maior ou menor que {palpite2}.(i/M/m) ")
                else:
                    print(f"O número que escolhi é mis pequeno que: {palpite2}")
                    maximo=palpite2-1
                    palpite2=random.randint(minimo,maximo)
                    i=i+1
                    pergunta=input(f"O número que escolheu é igual,maior ou menor que {palpite2}.(i/M/m) ")
            print(f"Acertei! O número que escolheu é: {palpite2}")
            print(f"Número de tentativa:{i}")
        eu()
jogo(a)
