import random

print(50 * '#')
print("Vamos jogar a adivinhação?")
print(50 * '#')

numero_secreto = random.randrange(1, 101)
total_tentativas = 3
#rodada = 1


for rodada in range(1, total_tentativas + 1):
    print(f'Tentativa {rodada} de {total_tentativas}')
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print(f'Você digitou o número: {chute}')
    

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    #rodada_t = rodada 
    game_over = (rodada ==3 and chute > numero_secreto or chute < numero_secreto)
    if(acertou):
        print("Parabéns!!! Você acertou!!!!")
        break
    else:
        if(maior):
            print('Você erro!!! o número que voçê informou e maior que o némero secreto')
        elif(menor):
            print('Você erro!!! o número que voçê informou e menor que o némero secreto')
    
        elif(game_over):
            print('GAME OVER')
            print(f"O número secreto foi {numero_secreto}")    

print('Fim do jogo')


