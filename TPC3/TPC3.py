###TPC3

import random

print("(1) O computador começa")
print("(2) Tu começas")

n=int(input("Quem começa o jogo?"))

def jogo(n):
    if n=="1":
        def computador():
            soma=1
            i=1
            j=0
            print(f"O computador jogou {i}")
            while soma<100:
                print(f"A soma está em: {soma}")
                j=int(input("Que número de 1 a 10 deseja somar?"))
                print(f"Jogou o número: {j}")
                soma=soma+j
                i=11-j
                soma=soma+i
                print(f"O computador jogou {i}")
                if soma <100 and soma>90:
                    i=100-soma
                    print(f"O computador jogou {i}")
                    soma=soma+i
            print("O computador ganhou!")
        computador()
    else:
        def eu():
            soma=0
            estrategia=[1,12,23,34,45,56,67,78,89,100]
            while soma<100:
                j=int(input("Que número é que jogas"))
                soma=soma+j
                print(f"Jogaste o número: {j}")
                print(f"A soma está em: {soma}")
                if soma==100:
                    print("Ganhaste!")
                    return
                
                i=0
                for x in estrategia:
                    if soma <x and x-soma<=10 and i==0:
                        i=x-soma
                
                if i==0:
                    i=random.randint(1,10)
                print(f"O computador jogou: {i}")
                soma=soma+i
                print(f"A soma está em: {soma}")

                if soma==100:
                    print("O computador ganhou!")
                    return
        eu()
jogo(n)