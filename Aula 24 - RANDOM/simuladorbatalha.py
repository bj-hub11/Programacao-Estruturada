import random as r

def mostrar_batalha(j1, j2):

    if j1 != None and j2 != None:
        j1HP = j1   
        j2HP = j2
        

    print(f'Jogador 1 HP: {j1HP}            Jogador 2 HP: {j2HP}\n\n\n')

    print('   (°_°)-|==>                    <==|-(°_°)')
    print('==============================================\n//////////////////////////////////////////////')

    print('\n\n\n')

    if j1HP <= 0:
        
        print(f'Jogador 1 HP: {j1HP}            Jogador 2 HP: {j2HP}\n\n\n')

        print('   (XoX)                    <==|-(°u°)')
        print('==============================================\n//////////////////////////////////////////////')
        print('\n JOGADOR 2 É O VENCEDOR!!')
        return

    elif j2HP <= 0:
            
        print(f'Jogador 1 HP: {j1HP}            Jogador 2 HP: {j2HP}\n\n\n')
    
        print('   (°u°)-|==>                        (XoX)')
        print('==============================================\n//////////////////////////////////////////////')
        print('\n JOGADOR 1 É O VENCEDOR!!')
        return
    
    escolha1 = [int(input('Jogador 1:  ATACAR(1) / CURAR(2): '))]
    if escolha1[0] == 1:
        escolha1.append(j2HP)
        j2HP = agir(escolha1)
    else:
        escolha1.append(j1HP)
        j1HP = agir(escolha1)
    escolha2 = [int(input('Jogador 2:  ATACAR(1) / CURAR(2): '))]
    if escolha2[0] == 1:
        escolha2.append(j1HP)
        j1HP = agir(escolha2)
    else:
        escolha2.append(j2HP)
        j2HP = agir(escolha2)  

    mostrar_batalha(j1HP, j2HP)

def agir(escolha):
    hp = escolha[1]
    match escolha[0]:
        
        case 1:
            dano = r.randint(1, 26)
            hp -= dano
            print(f'Jogador causou {dano} de dano!')
            return hp
        case 2: 
            cura = r.randint(5, 16)
            hp += cura
            if hp > 100:
                hp = 100
                print('Jogador se curou totalmente!')
            else:
                 print(f'Jogador se curou em {cura} pontos')
            return hp

    

mostrar_batalha(100, 100)
