from typing import List
import streamlit as st
from llm.agent import IKEAgent
from streamlit_ui.context_management import Role, ChatMessage


DEFAULT_MESSAGES = [
    ChatMessage(Role.ASSISTANT, "How can I help you?"),
]


class Chat:

    def __init__(
        self,
        messages: List[ChatMessage] = DEFAULT_MESSAGES,
    ):

        self.messages = messages

        # Initialize the chat history
        st.session_state["messages"] = self.messages

        self.write_messages()

        if chat_input := st.chat_input("Chat with the assistant"):
            self.respond(chat_input)

    def get_messages(self) -> List[ChatMessage]:
        return [
            ChatMessage(msg.role, msg.content)
            for msg in st.session_state.messages
        ]

    def write_messages(self):
        for msg in self.messages:
            st.chat_message(msg.role).write(msg.content)

    def add_message_to_state_and_render(self, role: str, content: str) -> None:
        self.messages.append(ChatMessage(role, content))
        st.session_state.messages = self.messages

        print(f"Added message: {role}: {content}")
        st.chat_message(role).write(content)

    def get_latest_message(self) -> ChatMessage:
        return self.messages[-1]

    def respond(self, chat_input: str) -> None:

        self.add_message_to_state_and_render(Role.USER, chat_input)

        agent = IKEAgent(
            chat_messages=self.messages,
        )

        response = agent.send_message(chat_input)
        self.add_message_to_state_and_render(Role.ASSISTANT, response)
