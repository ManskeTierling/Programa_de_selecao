import os
import sqlite3
alunos = []
alunos2 = []
salas = []
cafe = []
nome_sala = []
c = 0 
A = 0
#Cadastro Alunos.
continuar = 'S'
os.system('cls')
print('-- CADASTRO DE ALUNOS --')
while True:
    if continuar == 'S':
        A = A +1
        print(f'=====Aluno {A}=====')
        nome = input('Nome: ').capitalize()
        sobrenome = input('Sobrenome: ').capitalize()
        nome_completo = nome + ' ' + sobrenome
        alunos.append(nome_completo)
        alunos2.append(nome_completo)
        continuar = str(input('Deseja continuar? (S/N): ')).upper()
        
        #SQL Alunos
        nomesql = sqlite3.connect('Alunos.db')
        cursor = nomesql.cursor()
        if A == 1:
            cursor.execute("CREATE TABLE nomes (nome text)")
        cursor.execute("INSERT INTO nomes VALUES('"+nome_completo+"')")
        nomesql.commit()
    else:
        break

#Cadastro Salas.
os.system('cls')
print(f'Total de Alunos = {A}')
continuar = 'S'
c = 0
print(f'-- CADASTRO SALAS --')
print('\n\033[1;31mAs salas nao podem ter diferença de mais do que um aluno...',
'\n\033[1;31mDigite novamente',
'\n\033[1;97m')   
while True:
    if continuar == 'S':
        c = c + 1
        print(f'===Sala {c}===')
        sala = str(input('Nome: '))
        lotacao = int(input('Numero de alunos: '))
        continuar = str(input('Deseja continuar? (S/N): ')).upper()
        nome_sala.append(sala)
        #SQL Salas
        salasql = sqlite3.connect(""+sala+".db")
        cursor = salasql.cursor()
        cursor.execute("CREATE TABLE salas (Nome_Aluno text)")
        for k in alunos[0:lotacao]:
            cursor.execute("INSERT INTO salas VALUES('"+k+"')")
        del(alunos[0:lotacao])
        salasql.commit()      
    else: 
        break

#Cadastro do café
os.system('cls')
cafesql = sqlite3.connect("Café.db")
cursor = cafesql.cursor()
cursor.execute("CREATE TABLE cafe (horario_um_sala_um text, horario_um_sala_dois text, horario_dois_sala_um text, horario_dois_sala_dois text)")

print('-- ITERVALO DO CAFÉ --')
print(f'Total de Alunos: {A}')
print('Primeiro horario.')
cafe11 = int(input('Numero de alunos Sala 1: '))
for x in alunos2[0:cafe11]:
    cursor.execute("INSERT INTO cafe (horario_um_sala_um) VALUES('"+x+"')")
del(alunos2[0:cafe11])      
cafe12 = int(input('Numero de alunos Sala 2: '))
for w in alunos2[0:cafe12]:
    cursor.execute("INSERT INTO cafe (horario_um_sala_dois) VALUES('"+w+"')")
del(alunos2[0:cafe12])
os.system('cls')
print('-- ITERVALO DO CAFÉ --')
print('Segundo horario.')
cafe21 = int(input('Numero de alunos Sala 1: '))
for y in alunos2[0:cafe21]:
    cursor.execute("INSERT INTO cafe (horario_dois_sala_um) VALUES('"+y+"')")
del(alunos2[0:cafe21])
cafe22 = int(input('Numero de alunos Sala 2: '))
for z in alunos2[0:cafe22]:
    cursor.execute("INSERT INTO cafe (horario_dois_sala_dois) VALUES('"+z+"')")
cafesql.commit()



