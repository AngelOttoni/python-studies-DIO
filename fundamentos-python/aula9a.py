# 
# * Gere, copie, mova, escreva e leia informações de arquivos externos

# arquivo = open('teste.txt', 'w') # o 'w' é para escrever
arquivo = open('teste.txt', 'a') # o 'a' é para atualizar
arquivo.write('\nSegunda linha')
arquivo.close()