import { Component, Element, Host, Prop, h } from '@stencil/core';

@Component({
  tag: 'chat-bubble',
  styleUrl: 'chat-bubble.css',
  shadow: true,
})
export class ChatBubble {
  @Prop() botName: string;
  @Prop() chatName: string;
  @Prop() corpus: string; //Vai pro servidor pela conexao do WS
  @Prop() backgroundUrl: string;
  @Prop() botImg: string;
  @Prop() personImg: string;
  @Prop() personName: string = 'Cliente';
  @Prop() tolerancia: string = '0.65';

  @Element() el: HTMLElement;

  msgerInput: HTMLElement;
  msgerChat: HTMLElement;
  socket: WebSocket;

  componentDidLoad() {
    this.socket = new WebSocket(`ws://localhost:5000?params={"corpus":"${this.corpus}", "tolerance":"${this.tolerancia}", "botName":"${this.botName}"}`);

    this.socket.addEventListener('open', event => {
      console.log('Connection Established', event);
    });

    this.socket.addEventListener('message', event => {
      console.log(event);
      this.appendMessage(this.botName, this.botImg, 'left', event.data);
    });
    this.msgerInput = this.get('.msger-input');
    this.msgerChat = this.get('.msger-chat');
  }

  sendMessage() {
    const msgText = (this.msgerInput as HTMLInputElement).value;
    if (!msgText) return;
    this.appendMessage(this.personName, this.personImg, 'right', msgText);
    (this.msgerInput as HTMLInputElement).value = '';
    this.socket.send(msgText);
  }

  get(selector: string) {
    return this.el.shadowRoot.querySelector(selector) as HTMLElement;
  }

  generateMessageElement(side: string, name: string, text: string, img: string) {
    return `
      <div class="msg ${side}-msg">
        <div class="msg-img" style="background-image: url(${img})"></div>
  
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">${name}</div>
            <div class="msg-info-time">${this.formatDate(new Date())}</div>
          </div>
  
          <div class="msg-text">${text}</div>
        </div>
      </div>
    `;
  }

  appendMessage(name, img, side, text) {
    this.msgerChat.insertAdjacentHTML('beforeend', this.generateMessageElement(side, name, text, img));
    this.msgerChat.scrollTop += 500;
  }

  formatDate(date) {
    const h = '0' + date.getHours();
    const m = '0' + date.getMinutes();
    return `${h.slice(-2)}:${m.slice(-2)}`;
  }

  render() {
    return (
      <Host>
        <section class="msger">
          <header class="msger-header">
            <div class="msger-header-title">
              <i class="fas fa-comment-alt"></i> {this.chatName}
            </div>
            <div class="msger-header-options">
              <span>
                <i class="fas fa-cog"></i>
              </span>
            </div>
          </header>

          <main class="msger-chat" style={{ backgroundImage: 'url(' + this.backgroundUrl + ')' }}>
            <div class="msg left-msg">
              <div class="msg-img" style={{ backgroundImage: 'url(' + this.botImg + ')' }}></div>

              <div class="msg-bubble">
                <div class="msg-info">
                  <div class="msg-info-name">{this.botName}</div>
                </div>

                <div class="msg-text">Oi, bem vindo ao {this.chatName}! Vá em frente e me envie uma mensagem. 😄</div>
              </div>
            </div>

            <div class="msg right-msg"></div>
          </main>

          <div class="msger-inputarea">
            <input type="text" class="msger-input" placeholder="Digite sua mensagem..." />
            <button class="msger-send-btn" onClick={this.sendMessage.bind(this)}>
              Enviar
            </button>
          </div>
        </section>
      </Host>
    );
  }
}
