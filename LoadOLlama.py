import ollama

class OllamaLoader:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "deepseek-r1:1.5b" 
        self.prompt = "What is Python?"
        self.response = None
        self.response_text = ""

    def generate(self, prompt):
        self.response = self.client.generate(model=self.model, prompt=prompt)
        self.response_text = self.response.response
        return self.response_text