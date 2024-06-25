with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    arquivo.seek(28, 0)
    
    # posicao = arquivo.tell()
    # print(posicao)
    
    linha = arquivo.readline()
    print(linha)