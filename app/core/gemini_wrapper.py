import logging 
import os 
from google import genai
from google.genai import types

class GeminiWrapper():
    def __init__(self, model_name: str = "gemini-1.5-flash", system_instruction: str = ""):
        self.client = genai.Client()
        self.model_name = model_name
        self.contents = []

        if system_instruction is not None:
            self.contents.append(
                types.Content(
                    role="system",
                    parts=[types.Part.from_text(text=system_instruction)]
                )
            )

    def run(self, user_message: str):
        """ Enter user message, run through gemini, track output and response and print response """
        # append user message to tracking array for history
        self.contents.append(
            types.Content(
                role='user', 
                parts=[types.Part.from_text(text=user_message)]
            )
        )
        # build config by providing the system instruction 
        config = types.GenerateContentConfig(
            system_instruction=self.system_instruction
        )
        try:
            # request compeltion using the tracked chat payload history 
            response=self.client.models.generate_content(
                model=self.model_name,
                contents=self.contents, 
                config=config
            )

            model_text=response.text

            # save the model's response to the chat hisotry
            self.contents.append(
                types.Content(
                    role="model",
                    parts=[types.Part.from_text(text=model_text)]
                )
            )
        except Exception as e: 
            logging.error(f"Gemini API invocation failed: {e}")
            # rollback the last message if it failed 
            self.contents.pop()
            raise e