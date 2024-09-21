import os

def extract_and_write_texts_between_sequences(filename, sequence):
    # Converte a sequência de valores ASCII em bytes
    search_bytes = bytes(sequence)
    output_filename = f"{os.path.splitext(filename)[0]}_output.txt"

    try:
        with open(filename, 'rb') as file:  # Abre o arquivo em modo binário
            content = file.read()  # Lê todo o conteúdo do arquivo
            
            # Encontra todas as posições da sequência no conteúdo
            positions = []
            pos = content.find(search_bytes)
            while pos != -1:
                positions.append(pos)
                pos = content.find(search_bytes, pos + len(search_bytes))
            
            # Verifica se há pelo menos duas ocorrências da sequência para extrair texto
            if len(positions) < 2:
                print(f"Não foram encontradas duas sequências completas em {filename}.")
                return

            # Abre o arquivo de saída em modo de escrita
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                # Extrai e escreve o texto entre as sequências
                for i in range(len(positions) - 1):
                    start = positions[i] + len(search_bytes)
                    end = positions[i + 1]
                    if start < end:
                        # Converte os bytes entre as posições para texto
                        text_between = content[start:end].decode('latin-1', errors='replace')
                        output_file.write(f"Texto encontrado entre as sequências {i+1} e {i+2}:\n{text_between}\n\n")
            print(f"Texto extraído e salvo em {output_filename}.")
    
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado {filename}")
    except Exception as e:
        print(f"Um erro ocorreu ao processar {filename}: {e}")

def main():
    folder_path = "../scr"
    # Define a sequência de caracteres ASCII a ser procurada
    sequence = [129, 165, 0]
    
    # Percorre todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith('.fsb'):  # Filtra apenas arquivos .fsb
            full_path = os.path.join(folder_path, filename)
            extract_and_write_texts_between_sequences(full_path, sequence)

if __name__ == "__main__":
    main()
