meteo=[]
n=int(input("Bem-vindo! Este programa permite analisar os registos das temperaturas e de precipitação ao londo dos dias. Quantos dias pretende analisar? "))
def analisar(): 
    while len(meteo)<n:
        data=input("Que dia deseja analisar? (ano,mes,dia)")
        t_max=float(input(f"Introduza a temperatura máxima registada no dia {data} "))
        t_min=float(input(f"Introduza a temperatura minima registada no dia {data} "))
        pre=float(input(f"Introduza a precepitação registada no dia {data}"))
        meteo.append((data,t_max,t_min,pre))
    print("Escolha o que pretende fazer: \n 0) sair do programa \n 1) Temperatura média \n 2) Guardar a tabela metereologica num ficheiro de texto \n 3) Carregar uma tabela metereologica de um ficheiro \n 4) Temperatura mínima mais baixa da tabela metereologica \n 5) Amplitude térmica \n 6) Dia em que a precipitação teve o valor máximo \n 7) Dias em que a precipitação foi superior a um certo valor \n 8) Número de dias consecutivos em que a precipitação foi abaixo de um certo valor \n 9) Gráfico da temperatura mínima, máxima e da pluvosidade \n 10) Colocar tudo numa aplicação externa ao notebook ")
    
    e=-1
    while e!=0:
        e=int(input("Que operação deseja fazer?"))
        if e==1:
            def medias(meteo):
                res = []
                for x in meteo:
                    data, t_max, t_min, *_=x
                    media=(t_max+t_min)/2
                    res.append((data,media))
                return res
            print(medias(meteo))
        elif e==2:
            def guardaTabMeteo(t, fnome):
                file=open(fnome,"w")
                for x in t:
                    data,t_max,t_min,pre=x
                    file.write(f"{data} | {t_max} | {t_min} | {pre}")
                    file.write("\n")
                file.close
                return file
            guardaTabMeteo(meteo, "meteorologia.txt")
            print("O ficheiro foi criado com sucesso!")
        elif e==3:
            def carregaTabMeteo(fnome):
                res = []
                file=open(fnome,"r")
                for x in file:
                    data,t_max,t_min,pre=x.strip().split("|")
                    res.append((data,float(t_max),float(t_min),float(pre)))
                file.close()
                return res
            print(carregaTabMeteo("meteorologia.txt"))
        elif e==4:
            def minMin(meteo):
                minima = meteo[0][1]
                for registo in meteo:
                    if registo[1] < minima:
                        minima = registo[1]
                return minima
            print(minMin(meteo))
        elif e==5:
            def amplTerm(meteo):
                res = []
                for x in meteo:
                    data,t_max,t_min,*_=x
                    amp=t_max-t_min
                    res.append((data,amp))
                return res 
            print(amplTerm(meteo))
        elif e==6:
            def maxChuva(meteo):
                max_prec=float(meteo[0][3])
                for registo in meteo:
                    max_data=registo[0]
                    if registo[3]> max_prec:
                        max_prec=registo[3] 
                return (max_data, max_prec)
            print(maxChuva(meteo))
        elif e==7:
            def prec(meteo):
                res = []
                p = float(input("Escolha um valor máximo para a precipitação: "))
                for registo in meteo:
                    prec_m = registo[3]
                    m_data = registo[0]
                    if prec_m > p:
                        res.append((m_data, prec_m))
                return res
            print(prec(meteo))
        elif e==8:
            p = float(input("Escolha um valor máximo para a precipitação: "))
            def maxPeriodoCalor(meteo, p):
                maximo=0
                i=0
                for registo in meteo:
                    prec=registo[3]
                    if prec<p:
                        i=i+1
                        if i> maximo:
                            maximo=i
                        else:
                            i=0
                return maximo
            print(maxPeriodoCalor(meteo,p))
        elif e==9:
            def grafTabMeteo(t):
                y_min=[t_min for data,t_max,t_min,*_ in t]
                y_max=[t_max for data,t_max,*_ in t]
                x=[f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
                print(y_min)
                print(x)

                plt.plot(x,y_min,color="purple", marker="o", label="Temperatura minima ºC")
                plt.plot(x,y_max,color="purple", marker="o", label="Temperatura minima ºC")
                plt.legend()
                plt.grid()
                plt.show()
                return
            grafTabMeteo(meteo)
        else:
            print("Introduza um numero válido")
analisar()