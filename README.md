# Programa_de_selecao
Desafio para seleção de empresa

# Programador
Não sou da Area de computação, estudo Administração. Comecei a estudar python no meio 
da pandemia por conta propria, fazendo exercicios e vendo videos, escolhi o python depois
de pesquisar muito. Nunca havia feito um programa com banco de dados, esse desafio
ajudou muito a me desenvolver na programação, pretendo continuar e aprimorar
cada vez mais meus conhecimentos com a programação.

# Programa
foram criado dois programas, um para Cadastro de alunos, salas e espaços para café,
e outro para pesquisar onde estão os alunos, nomes de alunos de uma sala e nomes de
alunos no espaço de café.

# Problema
depois de pesquisar muito acabei nao encontrando uma forma de pesquisar o nome de um
aluno, devolvendo o nome da sala e o espaço de cafe onde ele se encontra. tentei usar
o "from CADASTROS import nome_sala" porem ele estava importando o programa inteiro.
Minha ideia seria usar:

from CADASTROS import nome_sala

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
