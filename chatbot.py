from openai import OpenAI

class Chatbot:
    def __init__(self):
        self.client = OpenAI()

    def fallback_response(self, message: str) -> str:
        cleaned = message.strip().lower()

        if any(word in cleaned for word in ["hello", "hi", "hey"]):
            return "Hi! I'm currently in demo mode, but I can still help with internships, coding, and AI."

        if "internship" in cleaned or "internships" in cleaned:
            return "In demo mode: For internships, focus on building projects, practicing coding problems, tailoring your resume, and applying early."

        if "resume" in cleaned:
            return "In demo mode: A strong resume should highlight projects, technical skills, measurable impact, and role-specific keywords."

        if "interview" in cleaned:
            return "In demo mode: Prepare by practicing coding questions, reviewing data structures, and explaining your thought process clearly."

        if "coding" in cleaned or "code" in cleaned or "python" in cleaned or "java" in cleaned:
            return "In demo mode: Consistent coding practice, debugging, and building projects are some of the best ways to improve."

        if "api" in cleaned:
            return "In demo mode: APIs let applications communicate with each other and are essential in backend and AI integrations."

        if "ai" in cleaned or "llm" in cleaned or "machine learning" in cleaned:
            return "In demo mode: AI can automate tasks, improve decision-making, and power tools like chatbots, search assistants, and workflow automations."

        return "I'm currently running in demo mode. Ask me about internships, coding, resumes, interviews, APIs, or AI."

    def get_response(self, message: str) -> str:
        try:
            response = self.client.responses.create(
                model="gpt-5.4",
                input=message
            )
            return response.output_text
        except Exception:
            return self.fallback_response(message)