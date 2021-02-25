
import sqlite3
import os
os.system('cls')


print('=============== BUSCA ===============')
print('| Buscar Aluno digite            (A)|',
'\n| Buscar Sala digite             (S)|',
'\n| Buscar Espaço de Café digite   (C)|')
op = str(input('| Opção: ')).upper()

#Busca Aluno.
if op == 'A':
    os.system('cls')
    print('---- Busca Aluno ----')
    busca = input('Nome do Aluno: ')
    for l in nome_sala:
        conn = sqlite3.connect(l)
        c = conn.cursor()
        c.execute("SELECT FILE_NAME FROM salas WHERE Nome_ Aluno ="+busca+"")
        print(c.fetchall())


#Busca Sala.
if op == 'S':
    os.system('cls')
    print('----Busca de Sala----')
    nomesala = str(input('Nome da sala: '))
    try:
        conn = sqlite3.connect(""+nomesala+".db")
        c = conn.cursor()
        c.execute("SELECT * FROM salas")
        print(c.fetchall())
    except:
        print(f'Não existe nenhuma sala com o nome "{nomesala}"')


#Busca Espaço do café.
if op == 'C':
    os.system('cls')
    print('----Busca de Espaço de Café----')
    print('1º horario sala 1: opção 1')
    print('1º horario sala 2: opção 2')
    print('2º horario sala 1: opção 3')
    print('2º horario sala 2: opção 4')
    cafeop = int(input('Opção: '))

    
    if cafeop == 1:
        conn = sqlite3.connect("Café.db")
        c = conn.cursor()
        c.execute("SELECT horario_um_sala_um FROM cafe WHERE horario_um_sala_um IS NOT NULL")
        print(c.fetchall())
    if cafeop == 2:
        conn = sqlite3.connect("Café.db")
        c = conn.cursor()
        c.execute("SELECT horario_um_sala_dois FROM cafe WHERE horario_um_sala_dois IS NOT NULL")
        print(c.fetchall())
    if cafeop == 3:
        conn = sqlite3.connect("Café.db")
        c = conn.cursor()
        c.execute("SELECT horario_dois_sala_um FROM cafe WHERE horario_dois_sala_um IS NOT NULL")
        print(c.fetchall())
    if cafeop == 4:
        conn = sqlite3.connect("Café.db")
        c = conn.cursor()
        c.execute("SELECT horario_dois_sala_dois FROM cafe WHERE horario_dois_sala_dois IS NOT NULL")
        print(c.fetchall())
    else:
        print('Opção')



