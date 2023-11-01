from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from difflib import SequenceMatcher

ACCEPTANCE = 0.65


def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(None, message_text, candidate_text)
        similarity = round(similarity.ratio(), 2)
        if similarity < ACCEPTANCE:
            similarity = 0
            print(f"Similaridade menor que ", ACCEPTANCE)
        else:
            print(
                "Mensagem do usuário:",
                message_text,
                ", mensagem candidata:",
                candidate_message,
                ", nível de confiança:",
                similarity,
            )

    return similarity


database_uri = 'mongodb://localhost:27017/vet-database'


jarbas = ChatBot(
    "Jarbas",
    read_only=True,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    statement_comparison_function=comparate_messages,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
        }
    ],
    database_uri=database_uri
)

trainer = ChatterBotCorpusTrainer(jarbas)
trainer.train(
    "chatterbot.corpus.portuguese.greetings",
)
corpus = 'vet-bot'
corpusPath = ''

match corpus:
    case _:
        corpusPath = "data/vet.yml"

trainer.train(
    corpusPath
)


def getResponse(message):
    response = jarbas.get_response(message)
    if response.confidence > 0.0:
        return response
    else:
        return "Ainda não sei como responder essa pergunta :("


# while True:
#     chat_input = input(
#         "Digite alguma coisa...\n",
#     )
#     response = jarbas.get_response(chat_input)
#     if response.confidence > 0.0:
#         print(f"\n{jarbas.name}: {response}\n")
#     else:
#         print("Ainda não sei como responder essa pergunta :(")
#         print("Pergunte outra coisa...")
