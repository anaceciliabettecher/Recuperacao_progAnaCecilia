class Aluno:
    __pid: int
    __nome: str
    __email: str
    __siape: str
    __idade: int

    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid: int):
        self.__pid = pid

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: int):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: int):
        self.__email = email

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade: int):
        self.__idade = idade


    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)