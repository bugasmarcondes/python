# Windows paths usam \
# Unix e Linux usam /

import os

# junta strings para montar caminho
    # myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
    # for filename in myFiles:
    #     print(os.path.join('C:/Users/asweigart', filename))

# pega caminho atual
    # print(os.getcwd())

# troca de pasta
    # os.chdir('/Users/bugasmarcondes/Projetos/Src/')
    # print(os.getcwd())

# criando pastas
    # os.makedirs('/Users/bugasmarcondes/Projetos/Src/Samples/python/0003-reading-writing-files/novaPasta')

# return a string of the absolute path of the argument
    # print(os.path.abspath('.'))
    # print(os.path.abspath('Scripts'))
# return True if the argument is an abso- lute path and False if it is a relative path
    # print(os.path.isabs('.'))
    # print(os.path.isabs(os.path.abspath('.')))
# return a string of a relative path from the start path to path
    # print(os.path.relpath(os.path.abspath('.'), '/Users'))
    # print(os.path.relpath('/Users', os.path.abspath('.')))
    # print(os.getcwd())
# basename & dirname
    # path = os.path.abspath('.')
    # print(os.path.basename(path)) #somente o que vem depois da última barra
    # print(os.path.dirname(path)) #tudo até antes da última barra
# retorna uma tuple de um diretório
    # calcFilePath = os.path.abspath('.')
    # print(os.path.split(calcFilePath))
    # print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))
# split em diretórios
    # print('/usr/bin'.split(os.path.sep))

# Finding File Sizes and Folder Contents
    # print(os.path.getsize(os.path.abspath('.'))) # size in bytes
    # print(os.listdir(os.path.abspath('.')))

# total size of all the files in this directory
    # totalSize = 0
    # for filename in os.listdir(os.path.abspath('.')):
    #     totalSize = totalSize + os.path.getsize(os.path.join(os.path.abspath('.'), filename))
    # print(totalSize)

# os.path.exists('C:\\Windows') # True
# os.path.exists('C:\\some_made_up_folder') # False
# os.path.isdir('C:\\Windows\\System32') # True
# os.path.isfile('C:\\Windows\\System32') # False
# os.path.isdir('C:\\Windows\\System32\\calc.exe') # False
# os.path.isfile('C:\\Windows\\System32\\calc.exe') # True

# lê conteúdo de um arquivo de texto
    # helloTxt = os.path.join(os.path.abspath('.'), 'hello.txt')
    # helloFile = open(helloTxt)
    # helloContent = helloFile.read()
    # print(helloContent) # retorna o texto simples
    # helloContentList = helloFile.readlines()
    # print(helloContentList) # retorna o texto em uma lista

# escreve em um arquivo
    # baconFile = open('bacon.txt', 'w') 
    # baconFile.write('Hello world!\n')
    # baconFile.close()

    # baconFile = open('bacon.txt', 'a')
    # baconFile.write('Bacon is not a vegetable.')
    # baconFile.close()

    # baconFile = open('bacon.txt')
    # content = baconFile.read()
    # baconFile.close()
    # print(content)

# grava dados em um arquivo binário do tipo shelf
    # import shelve
    # shelfFile = shelve.open('mydata') 
    # cats = ['Zophie', 'Pooka', 'Simon'] 
    # shelfFile['cats'] = cats
    # shelfFile.close()
# lê e retorna lista de dados gravados anteriormente
    # shelfFile = shelve.open('mydata')
    # print(type(shelfFile))
    # print(shelfFile['cats'])
    # shelfFile.close()
#lista os valores do shelve em list() form
    # shelfFile = shelve.open('mydata')
    # print(list(shelfFile.keys()))
    # print(list(shelfFile.values()))
    # shelfFile.close()

# cria programa python dinâmicamente
    # import pprint
    # cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}] 
    # print(pprint.pformat(cats))
    # fileObj = open('myCats.py', 'w')
    # fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
    # fileObj.close()
# importa módulo criado anteriormente em um novo programa python
    # import myCats
    # print(myCats.cats)
    # print(myCats.cats[0])
    # print(myCats.cats[0]['name'])

# ********************************** #
# REALIZAR EXERCICIOS PRÁTICOS - 186 #
# ********************************** #