###TPC5
def programa():
    n=-1
    turma=[]
    while n!=0:
        print(" 1: Criar uma turma; \n 2: Inserir um aluno na turma; \n 3: Listar a turma;\n 4: Consultar um aluno por id;\n 5: Guardar a turma em ficheiro; \n 6: Carregar uma turma dum ficheiro;\n 0: Sair da aplicação")
        n=int(input("Que operação deseja fazer? "))
    
        if n==1:
            a=int(input("Quantos alunos pretende que esta turma tenha? "))
            turma=[]
            while len(turma)<a:
                nome=input("Qual o nome deste aluno?")
                id=int(input(f"Qual o id correspondente ao aluno {nome}"))
                notas=[]
                notatpc=float(input(f"Qual a nota dos TPC do aluno {nome}"))
                notaproj=float(input(f"Qual a nota do projeto do aluno {nome}"))
                notateste=float(input(f"Qual a nota do teste do aluno {nome}"))
                notas=[notatpc,notaproj,notateste]
                aluno=(nome,id,notas)
                turma.append(aluno)

        elif n==2:
            id=int(input("Qual é o id do aluno?"))
            existe=False

            for aluno in turma:
                if aluno[1] ==id:
                    existe=True
            if existe==False:
                nome=input("Qual o nome deste aluno?")
                notas=[]
                notatpc=float(input(f"Qual a nota dos TPC do aluno {nome}"))
                notaproj=float(input(f"Qual a nota do projeto do aluno {nome}"))
                notateste=float(input(f"Qual a nota do teste do aluno {nome}"))
                notas=[notatpc,notaproj,notateste]
                aluno=(nome,id,notas)
                turma.append(aluno)
            else:
                print("O aluno já se encontra neste turma")

        elif n==3:
            print("Lista de alunos nesta turma: ")
            for aluno in turma:
                print(f"Nome: {aluno[0]} | ID: {aluno[1]} | Notas TPC: {aluno[2][0]} | Nota projeto: {aluno[2][1]} | Nota teste: {aluno[2][2]}")

        elif n==4:
            id=int(input("Qual o id do aluno?"))
            encontrou=False

            for aluno in turma:
                if aluno[1]==id:
                    print (aluno)
                    encontrou=True
            if encontrou==False:
                print("Este aluno não se encontra nesta turma")

        elif n==5:
            def guardarTurma(turma, fnome):
                file = open(fnome, "w")

                for aluno in turma:
                    nome,id,notas=aluno
                    file.write(f"{nome} | {id} | {notas[0]} | {notas[1]} | {notas[2]}")
                    file.write("\n")

                file.close()

            guardarTurma(turma, "turma.txt")
            print("O ficheiro foi criado com sucesso")
        elif n==6:
            def carregarTurma(fnome):
                turma=[]
                file=open(fnome,"r")
                for aluno in file:
                    nome,id,notatpc,notaproj,notateste=aluno.strip().split("|")
                    turma.append((nome,int(id),float(notas[0]),float(notas[1]),float(notas[2])))
                file.close()
                return turma
            print(carregarTurma("turma.txt"))
        elif n==0:
            print("A encerrar")
        else:
            print("Introduza um número válido")
    if n==0:
        print("Até à próxima")
programa()