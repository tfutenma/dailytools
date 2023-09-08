import os
from PIL import Image

def convert_to_webp(source_folder, destination_folder):
    # Verifica se a pasta de origem e a pasta de destino existem
    if not os.path.exists(source_folder):
        print(f"A pasta de origem '{source_folder}' não existe.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Percorre todos os arquivos na pasta de origem
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            # Verifica se o arquivo é uma imagem (pode adicionar mais extensões, se necessário)
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                # Define o caminho de destino com a mesma estrutura de pastas
                destination_path = os.path.join(destination_folder, filename.replace(".jpg", ".webp").replace(".jpeg", ".webp").replace(".png", ".webp"))
                # Abre a imagem usando Pillow
                img = Image.open(source_path)
                # Converte a imagem para WebP com qualidade 75 (você pode ajustar esse valor conforme necessário)
                img.save(destination_path, "webp", quality=75)

if __name__ == "__main__":
    source_folder = input("Digite o caminho da pasta de origem: ")
    destination_folder = input("Digite o caminho da pasta de destino: ")

    convert_to_webp(source_folder, destination_folder)
    print("Conversão concluída.")
