import os

FOLDER_PATH = 'C:\/Users\\angelo\\PycharmProjects'

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileNames in fileNames:
        print('File Name: ' + fileNames)
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileNames)), sep='\n')

if __name__ == '__main__':
    listDir(FOLDER_PATH)