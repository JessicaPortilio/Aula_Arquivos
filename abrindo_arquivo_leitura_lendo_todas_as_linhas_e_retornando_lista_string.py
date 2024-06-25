with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linha.strip())