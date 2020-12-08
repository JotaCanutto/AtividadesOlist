class Categoria:
    __id : int
    __nome : str
    __lista_subcategorias : str

    def __init__(self, id):
        self.__id = id

    def get_id(self) -> int:
        return self.__id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome = nome

    def get_lista_subcategorias(self) -> str:
        return self.__lista_subcategorias

    def set_lista_subcategorias(self, lista_subcategorias):
        if type(lista_subcategorias) == str:
            self.__lista_subcategorias = lista_subcategorias

class Produto:
    __id : int
    __nome : str
    __descricao : str
    __categoria : str
    __subcategoria : str
    __preco : float
    __quantidade : int
    __peso : float
    __altura : float
    __largura : float
    __comprimento : float

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

    def get_peso(self) -> float:
        return self.__peso

    def set_peso(self, peso):
        if type(peso) == float:
            self.__peso = peso

    def get_altura(self) -> float:
        return self.__altura

    def set_altura(self, altura):
        if type(altura) == float:
            self.__altura = altura

    def get_largura(self) -> float:
        return self.__largura

    def set_largura(self, largura):
        if type(largura) == float:
            self.__largura = largura

    def get_comprimento(self) -> float:
        return self.__comprimento

    def set_comprimento(self, comprimento):
        if type(comprimento) == float:
            self.__comprimento = comprimento

lista_de_produtos = []
lista_de_categorias = []
lista_de_subcategorias = []
cats = []
product_id = 0
categoria_id = 0
print('Cadastro de Produtos\n')

while True:
    print('1 - Cadastrar Produto\n2 - Cadastrar Categoria \n3 - Alterar \n4 - Exibir \n5 - Excluir\n6 - Sair')

    opcao = input('Selecione a opção:')

    if opcao == '1':
        produto = Produto(product_id)
        produto.set_nome(input('Nome:'))

        while True:
            desc = input('Descrição:')

            if len(desc) < 20:
                print('A descrição deve conter pelo menos 20 caracteres')
            else:
                produto.set_descricao(desc)
                break

        while True:
            preco = float(input('Preço Unitário:'))

            if type(preco) != float:
                print('Preço inválido, favor digitar novamente')
            else:
                produto.set_preco(preco)
                break

        while True:
            peso = float(input('Peso Unitário:'))

            if type(peso) != float:
                print('Peso inválido, favor digitar novamente')
            else:
                produto.set_peso(peso)
                break

        while True:
            altura = float(input('Altura:'))

            if type(altura) != float:
                print('Altura inválida, favor digitar novamente')
            else:
                produto.set_altura(altura)
                break

        while True:
            largura = float(input('Largura:'))

            if type(largura) != float:
                print('Largura inválida, favor digitar novamente')
            else:
                produto.set_largura(largura)
                break

        while True:
            comprimento = float(input('Comprimento:'))

            if type(comprimento) != float:
                print('Comprimento inválido, favor digitar novamente')
            else:
                produto.set_comprimento(comprimento)
                break

        while True:
            qtde = int(input('Quantidade:'))

            if type(qtde) != int:
                print('Quantidade inválida, favor digitar novamente')
            else:
                produto.set_preco(qtde)
                break

        while True:
            for categorias in lista_de_categorias:
                print(str(categorias.get_id()) +' - '+ categorias.get_nome())

            id_categoria = int(input('Selecione o número da categoria:'))

            for categoria in lista_de_categorias:
                if int(id_categoria) == categoria.get_id():
                    cats.append(categoria.get_nome())

            opt = input('Adicionar mais Categorias a este produto? <S/N>').lower()

            if opt == 'n':
                break
        produto.set_categoria(', '.join(cats))
        lista_de_produtos.append(produto)
        product_id += 1
        cats = ''
    elif opcao == '2':
        categoria = Categoria(categoria_id)
        categoria.set_nome(input('Nome:'))

        while True:
            sub = input('Nome da subcategoria:')
            lista_de_subcategorias.append(sub)
            categoria_id += 1
            subcategoria = Categoria(categoria_id)
            subcategoria.set_nome(sub)
            lista_de_categorias.append(subcategoria)

            op = input('Adicionar mais subcategorias a esta categoria? <S/N>').lower()

            if op == 'n':
                break
        categoria.set_lista_subcategorias(', '.join(lista_de_subcategorias))
        lista_de_categorias.append(categoria)
        categoria_id += 1
    elif opcao == '3':
        alterar = int(input('Digite o id do produto que deseja editar: '))
        for indice in lista_de_produtos:
            if alterar == indice.get_id():
                indice.set_nome(input('Nome:'))
                indice.set_descricao(input('Descrição:'))
                
                while True:
                    desc = input('Descrição:')

                    if len(desc) < 20:
                        print('A descrição deve conter pelo menos 20 caracteres')
                    else:
                        produto.set_descricao(desc)
                        break

                while True:
                    preco = float(input('Preço Unitário:'))

                    if type(preco) != float:
                        print('Preço inválido, favor digitar novamente')
                    else:
                        produto.set_preco(preco)
                        break

                while True:
                    peso = float(input('Peso Unitário:'))

                    if type(peso) != float:
                        print('Peso inválido, favor digitar novamente')
                    else:
                        produto.set_peso(peso)
                        break

                while True:
                    altura = float(input('Altura:'))

                    if type(altura) != float:
                        print('Altura inválida, favor digitar novamente')
                    else:
                        produto.set_altura(altura)
                        break

                while True:
                    largura = float(input('Largura:'))

                    if type(largura) != float:
                        print('Largura inválida, favor digitar novamente')
                    else:
                        produto.set_largura(largura)
                        break

                while True:
                    comprimento = float(input('Comprimento:'))

                    if type(comprimento) != float:
                        print('Comprimento inválido, favor digitar novamente')
                    else:
                        produto.set_comprimento(comprimento)
                        break

                while True:
                    qtde = int(input('Quantidade:'))

                    if type(qtde) != int:
                        print('Quantidade inválida, favor digitar novamente')
                    else:
                        produto.set_preco(qtde)
                        break

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
                  ' - Peso: '+str(indice.get_peso())+
                  ' - Altura: '+str(indice.get_altura())+
                  ' - Largura: '+str(indice.get_largura())+
                  ' - Comprimento: '+str(indice.get_comprimento())+
                  ' - Categorias: '+indice.get_categoria())
    elif opcao == '5':
        excluir = int(input('Digite o id do produto que deseja excluir: '))
        for indice in lista_de_produtos:
            if excluir == indice.get_id():
                lista_de_produtos.remove(indice)
    elif opcao == '6':
        break
