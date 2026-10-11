##TPC4
import random 
print("(1) Criar Lista")
print("(2) Ler lista")
print("(3) Soma")
print("(4) Média")
print("(5) Maior")
print("(6) Menor")
print("(7) estaOrdenada por ordem crescente")
print("(8) estaOrdenada por ordem decrescente")
print("(9) Procura um elemento")
print("(0) Sair")


def manip():
    n= int(input("Que deseja fazer (escolha o número correspondente))"))
    lista=[]
    while n!=0:
        if n==1:
            l=int(input("Quantos números deseja  ter na lista"))
            i=0
            if lista !=[]:
                lista.clear()
            while len(lista)<l:    
                i=random.randint(1,100)
                lista.append(i)
            print(lista)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==2:
            l2=int(input("Quantos números deseja  ter na lista"))
            i2=0
            if lista!=[]:
                lista.clear()
            while len(lista)<l2:
                i2=int(input("Introduza um número para ser colocado na lista"))
                lista.append(i2)
            print(lista)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==3:
            soma=0
            for x in lista:
                soma=soma+x
            print(soma)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==4:
            soma=0
            for x in lista:
                soma=soma+x
            med=soma/len(lista)
            print(med)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==5:
            maior=lista[0]
            for x in lista:
                if x> maior:
                    maior=x
            print(maior)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==6:
            menor=lista[0]
            for x in lista:
                if x< menor:
                    menor=x
            print(menor)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==7:
            def estaOrdenada(lista):
                i=0
                while i <len(lista)-1:
                    if lista[i]>lista[i+1]:
                        return "Não"
                    i=i+1
                return "Sim"
            print(estaOrdenada(lista))
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==8:
            def estaordenada(lista):
                i=0
                while i< len(lista)-1:
                    if lista[i]<lista[i+1]:
                        return "Não"
                    i=i+1
                return "Sim"
            print(estaordenada(lista))
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        elif n==9:
            elem=int(input(" Diga um número para verificar se este encontra-se na lista ou não"))
            pos=0
            encontrado=False
            for x in lista:
                if x==elem:
                    print(pos)
                    encontrado=True
                pos=pos+1
            if encontrado==False:
                print(-1)
            n=int(input("Que deseja fazer (escolha o número correspondente))"))
        else:
            print (lista)
manip()