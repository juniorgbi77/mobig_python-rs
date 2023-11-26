# Arquivo principal para controlar a execução dos scripts

import generateQrCode
import WhatsappMessage


def main():
    print("Escolha a ação que deseja realizar:")
    print("1. Gerar QR codes a partir do arquivo CSV")
    print("2. Enviar mensagem no WhatsApp")
    choice = input("Digite o número da ação desejada: ")

    if choice == "1":
        generateQrCode.main()  # Chama a função principal do script generateQrCode.py
    elif choice == "2":
        WhatsappMessage.main()  # Chama a função principal do script WhatsappMessage.py
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
