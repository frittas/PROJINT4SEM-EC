from chatterbot import ChatBot
from chatterbot.comparisons import levenshtein_distance
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement

# Crie um ChatBot
bot = ChatBot('MeuBot')

# Crie um adaptador lógico personalizado


class HighestConfidenceAdapter(LogicAdapter):
    def _init_(self, chatbot, **kwargs):
        super()._init_(chatbot, **kwargs)

    def process(self, statement, additional_response_selection_parameters):
        response = self.get_highest_confidence_response(statement)
        print(f'Pergunta recebida - {statement.text}')
        print(
            f'Resposta Selecionada - {response.text} | Confidence: {response.confidence}')
        return response

    def can_process(self, statement):
        return True

    def get_highest_confidence_response(self, statement):
        response = None
        max_confidence = -1

        response_list = self.get_all_response_options(statement)
        response_list.sort(key=lambda x: x.confidence, reverse=True)

        for response_statement in response_list:
            if response_statement.confidence > max_confidence:
                max_confidence = response_statement.confidence
                response = response_statement

        return response

    def get_all_response_options(self, statement):
        response_list = []
        # Lista apenas as perguntas com respostas da base do Mongo
        trained_list = list(filter(lambda list_item: list_item != None,
                                   self.chatbot.storage.filter()))
        for response in trained_list:
            # Calcula a confiança entre a entrada do usuário e cada resposta
            confidence = levenshtein_distance(statement, response)

            # Define a confiança na resposta
            response.confidence = confidence

            response_list.append(response)

        return response_list
