# Crie um programa que você possa ler os produtos do arquivo, adicionar novos produtos e
# exibir a lista atualizada.

import csv

# Função para ler e exibir os dados do arquivo de texto do nosso arquivo .txt ou .csv
def ler_arquivo(nome_arquivo):
    produtos = []
    with open(nome_arquivo, 'r+', encoding='utf-8-sig', newline='') as arquivo:
        leitura = csv.DictReader(arquivo, delimiter=',')
        # Itera sobre cada linha do arquivo
        for linha in leitura:
            produtos.append({
                'ID': linha['ID'],
                'Nome': linha['Nome'],
                'Preço': linha['Preço'],
                'Quantidade': linha['Quantidade']
            })
    return produtos


def adicionar_produtos(nome_arquivo, novo_produto):
    with open(nome_arquivo, 'r+', encoding='utf-8-sig', newline='') as arquivo:
        leitura = csv.DictReader(arquivo, delimiter=',')
        ids_existentes = 0
        for linha in leitura:
            ids_existentes = int(linha['ID'])
        novo_produto['ID'] = str(ids_existentes + 1) if ids_existentes else '1'
        
        
    with open(nome_arquivo, 'a', encoding='utf-8-sig', newline='') as arquivo:
        escrevendo = csv.DictWriter(arquivo, fieldnames=['ID', 'Nome', 'Preço', 'Quantidade'], delimiter=',')
        escrevendo.writerow(novo_produto)

def main():
    # Definindo o nome do meu arquivo
    nome_arquivo = 'produtos.csv'
    
    # Chamando a função para ler os dados do meu arquivo
    produtos = ler_arquivo(nome_arquivo)
    
    # Imprindo os produtos do meu arquivo
    for produto in produtos:
        for chave, valor in produto.items():
            print(f'{chave}: {valor}')
        print()
    
    # Solicitar os dados do novo produto ao usuário
    novo_produto = {}
    novo_produto['Nome'] = input('Digite o nome do novo produto: ')
    novo_produto['Preço'] = input('Digite o preço do novo produto: ')
    novo_produto['Quantidade'] = input('Digite a quantidade do novo produto: ')
    print()
    # Adicionar os dados do novo produto ao usuário
    adicionar_produtos(nome_arquivo, novo_produto)

    # Exibir os dados atualizados do arquivo
    # Chamando a função para ler os dados do meu arquivo
    produtos = ler_arquivo(nome_arquivo)
    
    # Imprindo os produtos do meu arquivo
    for produto in produtos:
        for chave, valor in produto.items():
            print(f'{chave}: {valor}')
        print()
        
if __name__ == '__main__':
    main()
            