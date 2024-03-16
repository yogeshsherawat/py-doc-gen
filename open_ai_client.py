import os
from openai import OpenAI
from config import OPENAI_API_KEY

class OpenAIClient:
    """Manages interactions with the OpenAI API."""

    client = None

    @classmethod
    def get_client(cls):
        """Returns a singleton OpenAI client instance."""
        if cls.client is None:
            os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
            cls.client = OpenAI(api_key=OPENAI_API_KEY)
        return cls.client
