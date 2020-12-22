marketplaces = ['Mercado Livre', 'Americanas', 'Amazon', 'Submarino']
categorias = ['Eletrodomésticos', 'Alimentos', 'Petshop']
subcategorias = ['Celular', 'Notebook', 'Salgado', 'Doce', 'Coleira']

def exibir_marketplaces()-> str:
    lista = ''
    for mkt in marketplaces:
                lista += f'{mkt}, '
    return lista

def exibir_categorias()->str:
    lista = ''
    for mkt in marketplaces:
        lista += f'{mkt}: '
        for categoria in categorias:
            if categoria == categorias[len(categorias)-1]:
                lista += f'{categoria}.\n'
            else:
                lista += f'{categoria}, '
    return lista

def exibir_subcategorias()->str:
    lista = ''
    for categoria in categorias:
        lista += f'{categoria}: '
        for subcategoria in subcategorias:
            if subcategoria == subcategorias[len(subcategorias)-1]:
                lista += f'{subcategoria}.\n'
            else:
                lista += f'{subcategoria}, '
    return lista

