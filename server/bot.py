from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response
from difflib import SequenceMatcher


class Bot:
    database_uri = None
    bot: ChatBot = None
    ACCEPTANCE = 0.65
    botName = None

    def __init__(self, name, train: bool, corpus: str, database_uri: str,  acceptance=None, ):
        self.botName = name
        self.database_uri = database_uri

        if acceptance is not None:
            self.ACCEPTANCE = acceptance

        self.bot = self.initBot(name, corpus, True)
        if train:
            self.train(self.bot, corpus)

    def initBot(self, name: str, database: str, readOnly: bool):
        return ChatBot(
            name,
            read_only=readOnly,
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            response_selection_method=self.select_response,
            statement_comparison_function=self.comparate_messages,
            logic_adapters=[{
                "import_path": "chatterbot.logic.BestMatch",
            }],
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace'
            ],
            database_uri=f'{self.database_uri}/{database}'
        )

    def train(self, bot: ChatBot, corpusName: str):
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train(
            "chatterbot.corpus.portuguese.greetings",
            f"data/{corpusName}.yml"
        )

    def select_response(self, message, list_response, storage=None):
        response = list_response[0]
        print("resposta escolhida:", response)
        return response

    def getResponse(self, message):
        response = self.bot.get_response(message)
        if response.confidence > 0.0:
            return response
        else:
            return "Ainda não sei como responder essa pergunta :("

    def comparate_messages(self, message, candidate_message):
        similarity = 0.0

        if message.text and candidate_message.text:
            message_text = message.text
            candidate_text = candidate_message.text

            similarity = SequenceMatcher(None, message_text, candidate_text)
            similarity = round(similarity.ratio(), 2)
            if similarity < self.ACCEPTANCE:
                similarity = 0
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
