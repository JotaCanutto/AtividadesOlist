from datetime import datetime

def ler_marketplaces() -> list:
    lista_marketplaces = []
    with open('MarketplaceWeb/marketplaces.txt', 'r') as arquivo:
        for linha in arquivo:
            linha_limpa = linha.strip()
            lista_marketplaces.append(linha_limpa)
    gravar_log('Acessada leitura de Marketplaces')
    return lista_marketplaces

def ler_categorias() -> list:
    lista_categorias = []
    lista_marketplaces = []
    lista_marketplaces_categorias = []
    with open('MarketplaceWeb/marketplaces.txt', 'r') as arquivo1, open('MarketplaceWeb/categorias.txt', 'r') as arquivo2:
        for linha_categoria in arquivo2:
            linha_categoria_limpa = linha_categoria.strip()
            lista_categorias.append(linha_categoria_limpa)
        for linha_mkt in arquivo1:
            linha_mkt_limpa = linha_mkt.strip()
            lista_marketplaces.append(linha_mkt_limpa)
        for linha in lista_marketplaces:
            linha_formatada = f'{linha}: {lista_categorias}'
            lista_marketplaces_categorias.append(linha_formatada)
    gravar_log('Acessada leitura de Categorias')
    return lista_marketplaces_categorias

def gravar_log(msg: str):
    data_hora = datetime.now().strftime('%H:%M:%S - %d/%m/%Y')

    with open('MarketplaceWeb/log.txt', 'a') as log:
        log.write(f'{data_hora} - {msg}\n')

