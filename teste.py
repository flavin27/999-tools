import os

# Caminho para a pasta contendo os arquivos .fsb
folder_path = '../scr'
search_phrase = "creating"


# Função para procurar a frase em um arquivo
def search_in_file(file_path, phrase):
    with open(file_path, 'r', errors='ignore') as file:
        content = file.read()
        if phrase in content:
            print(f'Frase encontrada em: {file_path}')

# Iterar sobre todos os arquivos na pasta
for filename in os.listdir(folder_path):
    if filename.endswith('.fsb'):
        file_path = os.path.join(folder_path, filename)
        search_in_file(file_path, search_phrase)
