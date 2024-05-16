from respostas import responder

# Função principal do chatbot
def main():
    print("Olá! Eu sou o ChatBot. Como posso ajudar?")
    while True:
        entrada = input("Você: ")
        if entrada.lower() == 'sair':
            print(responder("adeus"))
            break
        resposta = responder(entrada)
        print("ChatBot:", resposta)

# Iniciar o chatbot
if __name__ == "__main__":
    main()
