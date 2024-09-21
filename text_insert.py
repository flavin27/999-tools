import os

def update_fsb_with_translations(fsb_filename, txt_filename):
    try:
        with open(txt_filename, 'r', encoding='utf-8') as txt_file:
            lines = txt_file.readlines()

            # Lê o conteúdo do arquivo .fsb
            with open(fsb_filename, 'rb') as fsb_file:
                content = fsb_file.read().decode('latin-1', errors='replace')

            # Percorre as linhas do arquivo .txt em passos de 3
            for n in range(1, (len(lines) // 3) + 1):
                idx_3n_minus_1 = 3 * n - 2  # Linha 3n-1 (0-index)
                idx_3n = 3 * n - 1          # Linha 3n (0-index)

                if idx_3n_minus_1 < len(lines) and idx_3n < len(lines):
                    substring_to_replace = lines[idx_3n_minus_1].strip()  # Linha 3n-1
                    translation = lines[idx_3n].strip()                    # Linha 3n
                    
                    # Substitui a substring encontrada pela tradução
                    content = content.replace(substring_to_replace, translation)

            # Salva o conteúdo atualizado de volta no arquivo .fsb
            with open(fsb_filename, 'wb') as fsb_file:
                fsb_file.write(content.encode('latin-1', errors='replace'))

            print(f"Arquivo {fsb_filename} atualizado com as traduções do arquivo {txt_filename}.")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {fsb_filename} ou {txt_filename}")
    except Exception as e:
        print(f"Um erro ocorreu ao processar os arquivos: {e}")

def main():
    folder_path = "../scr"
    
    # Percorre todos os arquivos .txt na pasta
    for txt_filename in os.listdir(folder_path):
        if txt_filename.endswith('_output.txt'):  # Filtra apenas os arquivos .txt gerados
            full_txt_path = os.path.join(folder_path, txt_filename)
            # Define o nome do arquivo .fsb correspondente
            fsb_filename = txt_filename.replace('_output.txt', '.fsb')
            full_fsb_path = os.path.join(folder_path, fsb_filename)

            # Atualiza o .fsb com as traduções do .txt
            update_fsb_with_translations(full_fsb_path, full_txt_path)

if __name__ == "__main__":
    main()
