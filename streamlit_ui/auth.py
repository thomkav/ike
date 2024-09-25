from dotenv import load_dotenv
import os

from griptape.structures import Agent
from griptape.memory.structure import Run
from custom_logging import getLogger

logger = getLogger(__name__)

load_dotenv()


def _assert_openai_api_key() -> None:

    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found in environment variables.")


def test_openai_response() -> str:

    _assert_openai_api_key()

    agent = Agent()

    agent.run("Hello, world!")

    memory = agent.conversation_memory
    assert memory

    last_run: Run = memory.runs[-1]

    return last_run.output.to_text()


if __name__ == "__main__":

    response = test_openai_response()

    logger.info(f"OpenAI API response: {response}")
