from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import csv


def get_two_first_names(name):
    words = name.split()

    if len(words) < 2:
        return words[0]

    if (len(words[0]) <= 3) and (words >= 3):
        return f"{words[0]} {words[1]} {words[2]}"

    return f"{words[0]} {words[1]}"


def generate_qr_img(info, name, overlay_img_name, filename):
    base = Image.open('base_img.png')
    text_color = (255, 192, 0)

    img = Image.new('RGBA', base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    fontinfo = ImageFont.truetype('FRAHV.TTF', 30)
    fontname = ImageFont.truetype('FRAHV.TTF', 56)

    text_bbox = draw.textbbox((0, 0), info, font=fontinfo)
    text_width = text_bbox[2] - text_bbox[0]
    x = (img.width - text_width) // 2
    y = 680
    draw.text((x, y), info, font=fontinfo, fill=text_color)

    text_bbox = draw.textbbox((0, 0), name, font=fontname)
    text_width = text_bbox[2] - text_bbox[0]
    x = (img.width - text_width) // 2
    y = 715
    draw.text((x, y), name, font=fontname, fill=text_color)

    overlay_img = Image.open(overlay_img_name)

    # Calcular a posição para centralizar a imagem inserida
    x = (img.width - overlay_img.width) // 2
    y = (img.height - overlay_img.height) // 2

    # Colar a imagem inserida na nova imagem
    img.paste(overlay_img, (x, y), overlay_img)

    img.save(filename, "PNG")


def override_img(old_file, filename):
    base = Image.open('base_img.png')
    overlay_img = Image.open(old_file)

    new = Image.new("RGBA", overlay_img.size)

    new.paste(overlay_img, (0, 0))

    # Compor a segunda imagem sobreposta à primeira
    nova_imagem = Image.alpha_composite(new.convert("RGBA"), base.convert("RGBA"))

    # Salvar a imagem resultante
    new.save(filename, "PNG")


def main():
    temp_directory = 'temp/'
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)

    done_directory = 'qrImagesDone/'
    if not os.path.exists(done_directory):
        os.makedirs(done_directory)

    # Caminho para o arquivo CSV
    csv_file = 'users_test.csv'

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extrair informações necessárias do CSV
            number = row['number']
            city = row['city']

            info = f"{number} - {city}".upper()
            name = get_two_first_names(row['name']).upper()

            # Nome do arquivo da imagem
            old_filename = f"{temp_directory}{number}.png"
            filename = f"{done_directory}{number}.png"
            overlay_img_name = f"qrImages/{number}.png"

            # Gerar QR code com o valor de hash e salvar como imagem
            generate_qr_img(info, name, overlay_img_name, old_filename)
            override_img(old_filename, filename)

if __name__ == "__main__":
    main()
