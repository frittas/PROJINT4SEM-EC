/* eslint-disable */
/* tslint:disable */
/**
 * This is an autogenerated file created by the Stencil compiler.
 * It contains typing information for all components that exist in this project.
 */
import { HTMLStencilElement, JSXBase } from "@stencil/core/internal";
export namespace Components {
    interface ChatBubble {
        "backgroundUrl": string;
        "botImg": string;
        "botName": string;
        "chatName": string;
        "corpus": string;
        "personImg": string;
        "personName": string;
        "tolerancia": string;
    }
}
declare global {
    interface HTMLChatBubbleElement extends Components.ChatBubble, HTMLStencilElement {
    }
    var HTMLChatBubbleElement: {
        prototype: HTMLChatBubbleElement;
        new (): HTMLChatBubbleElement;
    };
    interface HTMLElementTagNameMap {
        "chat-bubble": HTMLChatBubbleElement;
    }
}
declare namespace LocalJSX {
    interface ChatBubble {
        "backgroundUrl"?: string;
        "botImg"?: string;
        "botName"?: string;
        "chatName"?: string;
        "corpus"?: string;
        "personImg"?: string;
        "personName"?: string;
        "tolerancia"?: string;
    }
    interface IntrinsicElements {
        "chat-bubble": ChatBubble;
    }
}
export { LocalJSX as JSX };
declare module "@stencil/core" {
    export namespace JSX {
        interface IntrinsicElements {
            "chat-bubble": LocalJSX.ChatBubble & JSXBase.HTMLAttributes<HTMLChatBubbleElement>;
        }
    }
}
