class Categoria:
    __id : int
    __nome : str

    def __init__(self, id):
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome = nome

class Produto:
    __id : int
    __nome : str
    __descricao : str
    __categoria : str
    __preco : float
    __quantidade : int

    def __init__(self, id):
        self.__id = id

    def get_id(self) -> int:
        return self.__id

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

    def get_categoria(self) -> str:
        return self.__categoria

    def set_categoria(self, categoria):
        if type(categoria) == str:
            self.__categoria = categoria

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
lista_de_categorias = []
cats = ''
product_id = 0
categoria_id = 0
subcategoria_id = 0
print('Cadastro de Produtos\n')

while True:
    print('1 - Cadastrar Produto\n2 - Cadastrar Categoria \n3 - Alterar \n4 - Exibir \n5 - Excluir\n6 - Sair')

    opcao = input('Selecione a opção:')

    if opcao == '1':
        produto = Produto(product_id)
        produto.set_nome(input('Nome:'))
        produto.set_descricao(input('Descrição:'))
        produto.set_preco(float(input('Preço Unitário:')))
        produto.set_quantidade(int(input('Quantidade:')))

        while True:
            for categorias in lista_de_categorias:
                print(str(categorias.get_id()) +' - '+ categorias.get_nome())

            id_categoria = int(input('Selecione o número da categoria:'))

            for categoria in lista_de_categorias:
                if id_categoria == categoria.get_id():
                    cats += categoria.get_nome() + ', '

            opt = input('Adicionar mais Categorias a este produto? <S/N>').lower()

            if opt == 'n':
                break
        produto.set_categoria(categorias)
        print(categorias)
        lista_de_produtos.append(produto)
        product_id += 1
    elif opcao == '2':
        categoria = Categoria(categoria_id)
        categoria.set_nome(input('Nome:'))
        lista_de_categorias.append(categoria)
        categoria_id += 1
    elif opcao == '3':
        alterar = int(input('Digite o id do produto que deseja editar: '))
        for indice in lista_de_produtos:
            if alterar == indice.get_id():
                indice.set_nome(input('Nome:'))
                indice.set_descricao(input('Descrição:'))
                indice.set_preco(float(input('Preço Unitário:')))
                indice.set_quantidade(int(input('Quantidade:')))

                while True:
                    for categorias in lista_de_categorias:
                        print(str(categorias.get_id()) +' - '+ categorias.get_nome())

                    id_categoria = input('Selecione o número da categoria:')

                    for categoria in lista_de_categorias:
                        if id_categoria == categoria.get_id:
                            categorias += (categoria.get_nome + ', ')

                    opt = input('Adicionar mais Categorias a este produto? <S/N>').lower()

                    if opt == 'n':
                        break
                produto.set_categoria(categorias)
    elif opcao == '4':
        for indice in lista_de_produtos:
            print('Id: '+str(indice.get_id())+
                  ' - Nome: '+indice.get_nome()+
                  ' - Descrição: '+indice.get_descricao()+
                  ' - Preço: '+str(indice.get_preco())+
                  ' - Quantidade: '+str(indice.get_quantidade())+
                  ' - Categorias: '+indice.get_categoria())
    elif opcao == '5':
        excluir = int(input('Digite o id do produto que deseja excluir: '))
        for indice in lista_de_produtos:
            if excluir == indice.get_id():
                lista_de_produtos.remove(indice)
    elif opcao == '6':
        break
