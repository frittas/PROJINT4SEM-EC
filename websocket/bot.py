from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from difflib import SequenceMatcher

ACCEPTANCE = 0.6


def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(None, message_text, candidate_text)
        similarity = round(similarity.ratio(), 2)
        if similarity < ACCEPTANCE:
            pass
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


def select_response(message, list_response, storage=None):
    response = list_response[0]
    print("resposta escolhida:", response)

    return response


jarbas = ChatBot(
    "Jarbas",
    rea
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    statement_comparison_function=comparate_messages,
    response_selection_method=select_response,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
        }
    ],
    database_uri='mongodb://localhost:27017/chatterbot-database'

)

# trainer = ChatterBotCorpusTrainer(jarbas)
# trainer.train(
#     "chatterbot.corpus.english.greetings", "chatterbot.corpus.english.conversations"
# )


conversa = [
    "Oi",
    "Olá! Como posso ajudar você?",
    "Qual seu nome?"
    "Jarbas, muito prazer"
    "Qual é a idade ideal para castrar um gato?",
    "A castração em gatos geralmente é recomendada entre os 4 e 6 meses de idade. Isso pode variar, então é melhor consultar um veterinário para orientações específicas.",
    "Meu cachorro comeu chocolate. O que devo fazer?",
    "O chocolate é tóxico para cães. Se isso acontecer, entre em contato imediatamente com um veterinário ou um centro de intoxicações de animais para orientações.",
    "Como posso treinar meu cão a fazer as necessidades no lugar certo?",
    "O treinamento de higiene em cães requer paciência e consistência. Use reforço positivo, leve-o para fora regularmente e recompense-o quando ele fizer as necessidades no lugar certo.",
    "Qual é a melhor raça de cão para famílias com crianças?",
    "Raças como o Labrador Retriever, Golden Retriever e Beagle são geralmente boas escolhas para famílias com crianças, mas o temperamento individual do cão também é importante.",
    "Como posso ajudar meu gato a lidar com o estresse?",
    "Reduza o estresse proporcionando um ambiente calmo, brinquedos e arranhadores, e mantendo uma rotina. Em casos graves, consulte um veterinário para orientações adicionais.",
    "Meu coelho está fazendo barulhos estranhos. O que isso significa?",
    "Ruídos estranhos, como rangidos, podem ser sinais de desconforto ou dor em coelhos. Consulte um veterinário especializado em animais de pequeno porte para uma avaliação completa.",
    "Como cortar as unhas do meu gato sem machucá-lo?",
    "Cortar as unhas de um gato requer cuidado. Use um cortador de unhas específico para gatos e corte apenas a ponta afiada, evitando a área rosa chamada lâmina. Se não se sentir seguro, peça ajuda a um veterinário ou profissional de pet shop.",
    "Meu cachorro está coçando muito e tem feridas na pele. O que pode ser?",
    "Coceira e feridas na pele podem ser causadas por alergias, infestações de pulgas ou carrapatos, ou infecções cutâneas. Consulte um veterinário para um diagnóstico e tratamento adequados.",
    "Como faço para manter os dentes do meu cavalo saudáveis?",
    "A saúde bucal é importante para cavalos. Fornecer feno de qualidade e permitir que eles pastem ajuda a manter seus dentes saudáveis. Além disso, agende exames odontológicos regulares com um veterinário equino.",
    "Como identificar alergias alimentares em meu cão?",
    "Sinais de alergias alimentares em cães incluem coceira, erupções cutâneas e problemas digestivos. Consulte um veterinário para um teste de alergia e recomendações sobre dieta.",
    "Meu pássaro não está cantando como antes. Devo me preocupar?",
    "Mudanças no canto de um pássaro podem indicar problemas de saúde. Seu pássaro pode estar estressado, doente ou desnutrido. Consulte um veterinário de aves para avaliação.",
    "Como identificar sinais de envenenamento em um cão?",
    "Sintomas de envenenamento incluem vômitos, diarreia, salivação excessiva, tremores e letargia. Se você suspeita de envenenamento, contate um veterinário imediatamente.",
    "Meu hamster está perdendo peso rapidamente. O que devo fazer?",
    "Perda de peso rápida em hamsters pode ser um sinal de doença. Consulte um veterinário especializado em animais de pequeno porte para avaliação e tratamento.",
    "Como evitar que meu cão tenha medo de fogos de artifício?",
    "Para ajudar um cão com medo de fogos de artifício, considere usar treinamento de dessensibilização, criar um ambiente seguro em casa, ou consultar um veterinário sobre possíveis medicamentos para acalmar a ansiedade.",
    "Meu peixe está nadando de lado. O que isso significa?",
    "Nadar de lado pode ser um sinal de problemas na bexiga natatória ou outras questões de saúde em peixes. Consulte um veterinário especializado em animais aquáticos.",
    "Como prevenir a formação de tártaro nos dentes do meu gato?",
    "A escovação regular dos dentes do seu gato é importante para prevenir a formação de tártaro. Use escovas e pastas de dente específicas para gatos. Além disso, forneça brinquedos e alimentos que promovam a saúde dental.",
    "Como faço para cuidar dos dentes do meu cão?",
    "A escovação regular dos dentes do seu cão é uma parte importante da saúde bucal. Use uma escova de dentes e pasta de dente específicas para cães e escove os dentes do seu animal pelo menos três vezes por semana. Também é aconselhável fazer exames dentários regulares com um veterinário.",
    "Meu gato está vomitando com frequência. Isso é normal?",
    "Vômitos frequentes em gatos não são normais. Pode ser causado por várias razões, como alergias, problemas digestivos ou obstruções. Consulte um veterinário para avaliar a saúde do seu gato e determinar a causa dos vômitos.",
    "Meu pássaro está perdendo penas. O que devo fazer?",
    "A perda de penas em aves pode ser causada por várias razões, como estresse, doenças ou problemas de dieta. Agende uma consulta com um veterinário de aves para determinar a causa e receber orientações sobre como cuidar do seu pássaro.",
    "Como faço para prevenir pulgas e carrapatos em meu cachorro?",
    "Existem vários produtos antipulgas e anticarrapatos disponíveis no mercado, como coleiras, gotas tópicas e comprimidos. Consulte seu veterinário para determinar o melhor método de prevenção de pulgas e carrapatos para o seu cão.",
    "Meu coelho está fazendo xixi com sangue. Isso é normal?",
    "Não, o sangue na urina de um coelho não é normal e pode ser um sinal de infecção do trato urinário ou outras condições médicas. É importante consultar um veterinário imediatamente.",
    "Meu gato não está comendo bem. O que devo fazer?",
    "A falta de apetite em gatos pode ser um sinal de problemas de saúde. Verifique se não há alimentos estragados ou sujos no prato do gato. Se o problema persistir, agende uma consulta com um veterinário para avaliar a saúde do seu gato.",
    "O que devo fazer se meu cão estiver tossindo muito?",
    "A tosse persistente em cães pode ser um sinal de várias condições, como alergias, infecções respiratórias ou até mesmo problemas cardíacos. Recomendo que você agende uma consulta com um veterinário para um diagnóstico preciso.",
]


listTrainer = ListTrainer(jarbas)
listTrainer.train(conversa)


while True:
    chat_input = input(
        "Digite alguma coisa...\n",
    )
    response = jarbas.get_response(chat_input)

    if response.confidence > ACCEPTANCE:
        print(f"\n{jarbas.name}: {response}\n")
    else:
        print("Ainda não sei como responder essa pergunta :(")
        print("Pergunte outra coisa...")
