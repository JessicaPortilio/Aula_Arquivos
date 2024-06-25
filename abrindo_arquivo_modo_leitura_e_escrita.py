# 'w' - modo de escrita
# 'a' - modo de anexação
# 'r' - modo de leitura
# função tell() - obtem a posição atual do nosso porteiro no arquivo
# unção seek() - mover o ponteiro para uma determinada posição desejada

# 'r+' - modo leitura e escrita
# 'w+' - modo de escrita e leitura

with open('lendo_e_escrevendo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrevendo nossa primeira linha...\n')

with open('lendo_e_escrevendo.txt', 'r+', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo.strip())
    
    arquivo.write('Depois de ler, podemos escrever \n')

with open('lendo_e_escrevendo.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo.strip())