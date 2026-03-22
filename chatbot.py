from openai import OpenAI

class Chatbot:
    def __init__(self):
        self.client = OpenAI()

    def get_response(self, message: str) -> str:
        try:
            response = self.client.responses.create(
                model="gpt-5.4",
                input=message
            )
            return response.output_text
        except Exception:
            # fallback if API fails
            return "I'm currently running in demo mode. Ask me about internships, coding, or AI!"