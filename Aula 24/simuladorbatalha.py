import random as r

def mostrar_batalha():
    print(f'Jogador 1 HP: {j1HP}            Jogador 2 HP: {j2HP}\n\n\n')

    print('   (°_°)-|==>                    <==|-(°_°)')
    print('==============================================\n//////////////////////////////////////////////')

    print('\n\n\n')
    escolha1 = int(input('Jogador 1:  ATACAR(1) / CURAR(2): '))
    escolha2 = int(input('Jogador 2:  ATACAR(1) / CURAR(2): '))

    agir(escolha1, escolha2)

def agir(escolha1, escolha2):
    match escolha1:
        case 1:
            dano = r.randint(1, 26)
            j2HP -= dano
            print(f'Jogador 1 causou {dano} de dano ao Jogador 2')
        case 2: 
            cura = r.randint(5, 16)
            j1HP += cura
            if j1HP > j1HPMAX:
                j1HP = j1HPMAX
                print('Jogador 1 se curou totalmente!')
            else:
                 print(f'Jogador 1 se curou em {cura} pontos')

    match escolha2:
        case 1:
            dano = r.randint(1, 26)
            j2HP -= dano
            print(f'Jogador 2 causou {dano} de dano ao Jogador 1')
        case 2: 
            cura = r.randint(5, 16)
            j2HP += cura
            if j2HP > j2HPMAX:
                j2HP = j2HPMAX
                print('Jogador 2 se curou totalmente!')
            else:
                print(f'Jogador 2 se curou em {cura} pontos')

    mostrar_batalha()

j1HP = 100
j1HPMAX = 100
j2HP = 100
j2HPMAX = 100

mostrar_batalha()
