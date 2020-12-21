class Produto:
    __nome : str
    __descricao : str
    __preco : float
    __quantidade : int

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome = nome

    def get_descricao(self) -> str:
        return self.__descricao

    def set_descricao(self, descricao):
        if type(descricao) == str:
            self.__descricao = descricao

    def get_preco(self) -> float:
        return self.__preco

    def set_preco(self, preco):
        if type(preco) == float:
            self.__preco = preco

    def get_quantidade(self) -> int:
        return self.__quantidade

    def set_quantidade(self, quantidade):
        if type(quantidade) == int:
            self.__quantidade = quantidade

lista_de_produtos = []
print('Cadastro de Produtos\n')

while True:
    print('1 - Cadastrar \n2 - Alterar \n3 - Exibir \n4 - Excluir \n5 - Sair')

    opcao = input('Selecione a opção:')

    if opcao == '1':
        produto = Produto()
        produto.set_nome(input('Nome:'))
        produto.set_descricao(input('Descrição:'))
        produto.set_preco(float(input('Preço Unitário:')))
        produto.set_quantidade(int(input('Quantidade:')))
        lista_de_produtos.append(produto)
    elif opcao == '2':
        alterar = input('Digite o nome do produto que deseja editar: ')
        for indice in lista_de_produtos:
            if alterar == indice.get_nome():
                indice.set_nome(input('Nome:'))
                indice.set_descricao(input('Descrição:'))
                indice.set_preco(float(input('Preço Unitário:')))
                indice.set_quantidade(int(input('Quantidade:')))
    elif opcao == '3':
        for indice in lista_de_produtos:
            print('Nome: '+indice.get_nome()+
                  ' - Descrição: '+indice.get_descricao()+
                  ' - Preço: '+str(indice.get_preco())+
                  ' - Quantidade: '+str(indice.get_quantidade()))
    elif opcao == '4':
        excluir = input('Digite o nome do produto que deseja excluir: ')
        for indice in lista_de_produtos:
            if excluir == indice.get_nome():
                lista_de_produtos.remove(indice)
    elif opcao == '5':
        break
