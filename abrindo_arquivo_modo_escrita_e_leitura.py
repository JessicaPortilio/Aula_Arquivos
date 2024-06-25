# 'w' - modo de escrita
# 'a' - modo de anexação
# 'r' - modo de leitura
# função tell() - obtem a posição atual do nosso porteiro no arquivo
# unção seek() - mover o ponteiro para uma determinada posição desejada
# 'r+' - modo leitura e escrita

# 'w+' - modo de escrita e leitura

with open('escrevendo_e_depois_lendo.txt', 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Estou escrevendo, para depois ler \n')
    
    arquivo.seek(0)
    conteudo = arquivo.read()
    print(conteudo.strip())
    

