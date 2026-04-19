import ollama

class OllamaLoader:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "deepseek-r1:1.5b" 
        self.prompt = "What is Python?"
        self.response = None
        self.response_text = ""

        self.available_models = [m.model for m in ollama.list().models]


        # testing
        # Let's say I want to select a model from GUI with a drop down... I need to first see what models are available...
        for model in self.available_models:
            print (model)

    def generate(self, prompt):
        self.response = self.client.generate(model=self.model, prompt=prompt)
        self.response_text = self.response.response
        return self.response_text