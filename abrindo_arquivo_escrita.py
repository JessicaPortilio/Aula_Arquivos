# 'w' - modo de escrita - vai abrir o arquivo se ele existir 
# e vai limpar tudo que tem dentro dele, se não existir ele cria.

arquivo = open('exemplo.txt', 'w')

arquivo.write('Bem-vindos ao nosso canal \n')
arquivo.write('Nunca desista de seus sonhos... \n')

arquivo.close()
