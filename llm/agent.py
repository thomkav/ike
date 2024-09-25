from typing import List

from streamlit_ui.context_management import ChatMessage
from griptape.structures import Agent
from griptape.artifacts import TextArtifact
from griptape.memory.structure import Run, ConversationMemory
from griptape.tools import FileManagerTool


class IKEAgent:
    def __init__(
        self,
        chat_messages: List[ChatMessage],
    ):
        print("initializing ike agent")

        runs = []
        for message in chat_messages:

            text_artifact = f'Role {message.role}: {message.content}'

            run = Run(
                input=TextArtifact(value=text_artifact),
                output=TextArtifact(value=""),
            )
            runs.append(run)

        conversation_memory = ConversationMemory(
            runs=runs,
        )
        self.agent = Agent(
            conversation_memory=conversation_memory,
            tools=[FileManagerTool()],
        )

    @staticmethod
    def _get_latest_output_text(agent: Agent) -> str:
        memory = agent.conversation_memory
        assert memory

        last_run: Run = memory.runs[-1]
        return last_run.output.to_text()

    def send_message(
        self,
        chat_input: str,
    ) -> str:
        self.agent.run(chat_input)
        return self._get_latest_output_text(self.agent)
