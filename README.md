# PROJINT4SEM-EC

Projeto Integrador 4Sem Engenharia Comp - Unisal  

Desenvolvimento de uma plataforma de chat utilizando Python, WebComponent, WebSocket e a Library Chatterbot.


https://chatterbot.readthedocs.io/en/stable/


## Checklist

- [x] Instalar as bibliotecas necessárias: Chatterbot, WebComponent e WebSocket.
- [x] Parametrização do ChatterBot.
- [x] Criação do Bot.
- [x] Integração com DataBase.
- [x] Exposição do Bot Via WebSocket.
- [x] Criação do WEBCOMPONENT.
- [x] Testes Integrados.



## Get started


### Pré Requisitos

1. Instalar [ChatterBot](https://chatterbot.readthedocs.io/en/stable/setup.html)
2. Instalar ChatterBot executando o comando no terminal:
  ```bash
  pip install chatterbot
  ```

### Clonar o Repositório

```shell
git clone https://github.com/frittas/PROJINT4SEM-EC
cd PROJINT4SEM-EC
```

### Instalar as dependências NPM na pasta chat-bubble e inicializar o webcomponent

Instalar os packages `npm` contidos no arquivo `package.json` e verificar se tudo corre como esperado:

```shell
cd chat-bubble
npm install
npm start
```


## Inicializar o servidor websocket python

Executar 
```shell
cd server
python app.py
``` 
para iniciar o servidor websocket e consequentemente a instância do bot.
