from openai import OpenAI

class Chatbot:
    def __init__(self):
        self.client = OpenAI()

    def get_response(self, message: str) -> str:
        try:
            response = self.client.responses.create(
                model="gpt-5.4",
                input=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI career assistant for a computer science student. Give clear, concise, encouraging answers about internships, coding, resumes, interviews, and AI engineering."
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )
            return response.output_text
        except Exception as e:
            return f"Error: {str(e)}"