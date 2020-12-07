class Pessoa:
    __nome : str
    __sobrenome : str
    __idade : int

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome = nome

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def set_sobrenome(self, sobrenome):
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome

    def get_idade(self) -> int:
        return self.__idade

    def set_idade(self, idade):
        if type(idade) == int:
            self.__idade = idade

pessoa = Pessoa()
pessoa.set_nome('Joao')
#pessoa.set_nome('Thiago')
pessoa.set_sobrenome('Canutto')
#pessoa.set_sobrenome(10)
pessoa.set_idade(23)
#pessoa.set_idade('teste')

print(pessoa.get_nome() + ' ' + pessoa.get_sobrenome() + ' ' + str(pessoa.get_idade()) + ' anos.')
print(pessoa.get_nome())
print(pessoa.get_sobrenome())
print(pessoa.get_idade())