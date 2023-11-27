import csv
import qrcode
import os


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=2
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filename)


def main():
    root_directory = 'qrImages/'
    if not os.path.exists(root_directory):
        os.makedirs(root_directory)

    # Caminho para o arquivo CSV
    csv_file = 'users_test.csv'

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extrair informações necessárias do CSV
            number = row['number']
            hash_value = row['hash']

            # Nome do arquivo da imagem
            filename = f"{root_directory}{number}.png"

            # Gerar QR code com o valor de hash e salvar como imagem
            generate_qr_code(hash_value, filename)


if __name__ == "__main__":
    main()
