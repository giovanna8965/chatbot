import random

# Dicionário de respostas do chatbot
respostas = {
    "oi": ["Olá!", "Oi, como posso ajuda-lo?", "E aí, tudo bem?"],
    "como você está?": ["Estou bem, obrigado por perguntar!", "Estou ótimo, e você?"],
    "qual é o seu nome?": ["Meu nome é ChatBot!", "Pode me chamar de ChatBot.", "Eu sou o ChatBot!"],
    "adeus": ["Até mais!", "Tchau! Volte sempre!", "Até logo!"],
    "o que você pode fazer?": ["Posso responder perguntas, conversar, e muito mais!", "Estou aqui para ajudar com qualquer dúvida que você tiver!", "Posso conversar, contar piadas e até mesmo ajudar com algumas informações."],
    "você é um robô?": ["Sim, sou um chatbot!", "Sim, sou um programa de computador projetado para conversar com pessoas.", "Correto, sou uma inteligência artificial."],
    "você gosta de música?": ["Não posso ouvir música, mas posso falar sobre!", "Eu não tenho preferências musicais, mas posso recomendar algumas!"],
    "me conte uma piada": ["Por que o computador foi à escola? Porque queria ser um "smart"-board!", "Por que o programador comprou um ar condicionado? Porque ele queria abrir janelas.", "Qual é o cúmulo da paciência? Sentar em cima de uma formiga e esperar ela tossir!"],
    "obrigado": ["De nada!", "Por nada!", "Não há de quê!"],
    "default": ["Desculpe, não entendi.", "Não tenho certeza do que você quis dizer.", "Pode repetir, por favor?"],
}

# Função para responder às mensagens do usuário
def responder(mensagem):
    mensagem = mensagem.lower()  # Converter a mensagem para minúsculas para tornar a correspondência não sensível a maiúsculas
    if mensagem in respostas:
        return random.choice(respostas[mensagem])
    else:
        return random.choice(respostas["default"])
