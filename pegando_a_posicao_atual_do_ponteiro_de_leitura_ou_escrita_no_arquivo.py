with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    posicao = arquivo.tell()
    print(posicao)
    
    linha = arquivo.readline()
    print(linha.strip())
    
    
    posicao = arquivo.tell()
    print(posicao)