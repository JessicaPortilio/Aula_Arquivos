with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()
    while linha:
        print(linha.strip())
        linha = arquivo.readline()
