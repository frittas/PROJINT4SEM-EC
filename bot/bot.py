from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from difflib import SequenceMatcher

ACCEPTANCE = 0.70


def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(),2)
        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)

    return similarity

def select_response(message, list_response, storage=None):
    response = list_response[0]
    print("resposta escolhida:", response)

    return response

chatbot = ChatBot("Jarbas",
        read_only=True,
        statement_comparison_function=comparate_messages,
        response_selection_method=select_response,
        logic_adapters=[
            {
                "import_path":"chatterbot.logic.BestMatch",
            }
        ])

conversa = [
    'Oi?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Jarbas, seu amigo bot',
    'Por que seu nome é Kopelito?', 
    'Kopelito é meu nome, sou um chatbot criado para diversão',
    'Prazer em te conhecer', 
    'Igualmente meu querido',
    'Quantos anos você tem?', 
    'Eu nasci em 2020, faz as contas, rs.',
    'Você gosta de videogame?', 
    'Eu sou um bot, eu só apelo.',
    'Qual a capital da Islândia?', 
    'Reikjavik, lá é muito bonito.',
    'Qual o seu personagem favorito?', 
    'Gandalf, o mago.',
    'Qual a sua bebida favorita?', 
    'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 
    'Sou um chatbot e gosto de algoritmos',
    'Conte uma história', 
    'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
    'Você gosta de Game of Thrones?', 'Dracarys',
    'O que você faz?', 'Eu bebo e sei das coisas',
    'Errado', 'Você não sabe de nada, John Snow.'
    ]



listTrainer = ListTrainer(chatbot)
listTrainer.train(conversa)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.portuguese')

def getResponse(message):
    response = chatbot.get_response(message)
    return response




# trainer.export_for_training('./training_export.json')


# while True:
#     message = input("Eu: ")                # Campo de entrada
#     if any (x == 'stop' for x in message.split(" ")):
#         break
#     response = chatbot.get_response(message)   # Resposta do chatbot
#     print(f'\n{chatbot.name}: {response}\n')


# while True:
#     chat_input = input("Digite alguma coisa...\n",)
#     response = chatbot.get_response(chat_input)

#     if response.confidence > 0.0:
#         print(f'\n{chatbot.name}: {response}\n')
#     else:
#         print("Ainda não sei como responder essa pergunta :(")
#         print("Pergunte outra coisa...")
