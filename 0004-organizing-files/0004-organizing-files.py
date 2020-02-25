import shutil, os, send2trash

diretorioDaAula = '/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/'

# shutil, et you copy, move, rename, and delete files in your Python programs
    # folderFrom = '/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/from'
    # folderTo = '/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/to'
    # shutil.copy(folderFrom + '/spam.txt', folderTo)
    # shutil.copy(folderFrom + '/spam.txt', folderTo + '/spam2.txt')

# faz backup de pasta
    # os.chdir('/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/')
    # shutil.copytree('/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/from', '/Users/bugasmarcondes/Projetos/Src/Samples/python/0004-organizing-files/from-backup')

# move ou renomeia arquivo
    # shutil.move(diretorioDaAula + '/from/bacon.txt', diretorioDaAula + '/to/new-bacon.txt')

# 1. Calling os.unlink(path) will delete the file at path.
# 2. Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
# 3. Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

# remove permanentemente arquivos
    # for filename in os.listdir():
    #     if filename.endswith('.rxt'):
    #         print(filename)
    #         # os.unlink(filename)

# remove jogando para a lixeira
    # baconFile = open(diretorioDaAula + '/from/bacon.txt', 'a')
    # baconFile.write('Bacon is not a vegetable.')
    # baconFile.close()
    # send2trash.send2trash(diretorioDaAula + '/from/bacon.txt')

# for folderName, subfolders, filenames in os.walk(diretorioDaAula):
#     print('The current folder is ' + folderName)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#         for filename in filenames:
#             print('FILE INSIDE ' + folderName + ': '+ filename)
#             print('')