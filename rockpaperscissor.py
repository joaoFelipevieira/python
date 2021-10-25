import random
vitoria_user = 0
vitoria_cpu = 0
options = ['pedra','papel','tesoura']

while True:
    escolha = input('digite pedra papel ou tesoura ,ou digite q para sair').lower()
    if (escolha) == ("q"):
        break

    if escolha  not in options:
        continue

    randomn= random.randint(0, 2)
    cpu_pick = options[randomn]
    print ("Computador escolheu",cpu_pick + ".")

    if escolha == "pedra"  and cpu_pick == "tesoura":
        vitoria_user += 1
        print ("Você ganhou" ,vitoria_user, "Vezes")
        continue
    elif escolha == "tesoura" and cpu_pick == "papel":
        vitoria_user += 1
        print("Você ganhou" ,vitoria_user, "Vezes")
        continue
    elif escolha == "papel"  and cpu_pick == "pedra":
        vitoria_user += 1
        print ("Você ganhou" ,vitoria_user, "Vez(es)")
        continue
    elif escolha == cpu_pick:
        print ("empatou")
        continue


    else :
        vitoria_cpu += 1
    print("Você perdeu", vitoria_cpu, "Veze(s)")


print ("Você ganhou" ,vitoria_user, "Vez(es)")
print ("Você Perdeu" ,vitoria_cpu , "Vez(es)")
print ("Adeus")