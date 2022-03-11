from model.Aluno import Aluno


class AlunoDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarAlunos(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM aluno ORDER BY pid'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            aluno = Aluno()
            aluno.pid = item[0]
            aluno.nome = item[1]
            aluno.email = item[2]
            aluno.idade = item[3]

            lista.append(aluno)

        return lista

    def selecionarAluno(self, pid) -> Aluno:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM aluno WHERE pid = {pid}")
        recset = c.fetchone()
        c.close()

        print(recset)

        aluno = Aluno()
        aluno.pid = recset[0]
        aluno.nome = recset[1]
        aluno.email = recset[2]
        aluno.idade = recset[3]
        

        return aluno

    def inserirAluno(self, aluno: Aluno) -> Aluno:
        c = self.connection.cursor()
        c.execute("""
            insert into aluno(nome, email, idade)
            values('{}', '{}', '{}') RETURNING pid
        """.format(aluno.nome, aluno.email, aluno.idade))

        self.connection.commit()

    def alterarAluno(self, aluno: Aluno) -> Aluno:
        c = self.connection.cursor()
        c.execute("""
            update aluno
            SET nome = '{}', email = '{}', idade = '{}'
            WHERE pid = '{}';
        """.format(aluno.nome, aluno.email, aluno.idade, aluno.pid))

        self.connection.commit()

    def excluirAluno(self, aluno: Aluno) -> Aluno:
        c = self.connection.cursor()
        c.execute("""
            delete from aluno
            where pid = '{}'
        """.format(aluno.pid))
        self.connection.commit()