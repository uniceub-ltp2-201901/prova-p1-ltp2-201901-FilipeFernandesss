def get_listar_prof(cursor):
    cursor.execute(f'Select id_professor, nome from professor;')

    listar = cursor.fetchall()

    cursor.close()
    return listar

def get_exibir_prof(cursor, id_professor):
    cursor.execute(f'Select P.nome, P.data_nasc, P.nome_mae, P.titulacao, D.nome_disciplina from professor P, disciplina D where P.id_professor = "{id_professor}" and P.id_professor = D.id_professor;')
    exibir = cursor.fetchall()
    cursor.close()
    disciplinas = []
    retorno = []

    for disci in exibir:
        disciplinas.append(disci[4])
        print(disci[4])

    retorno.append(exibir)
    retorno.append(disciplinas)
    print(retorno)
    return retorno

def get_titulacao(cursor, titulacao):
    cursor.execute(f'select nome, titulacao from professor where titulacao = "{titulacao}";')

    titulacao = cursor.fetchall()
    print(titulacao)
    return titulacao

def get_computacao(cursor, curso):
    cursor.execute(f'select P.nome, D.nome_disciplina from professor P, disciplina D where D.curso = "{curso}" and P.id_professor = D.id_professor')

    professores = cursor.fetchall()

    print(professores)
    return professores

def get_calculo(cursor, nome):
    cursor.execute(f'select carga_horaria from disciplina D, professor P where D.id_professor = P.id_professor AND P.nome = "{nome}";')
    valor = cursor.fetchall()
    return valor