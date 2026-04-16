### Useful Notes
# ollama list :: View local model names and size
# If I run the script, it takes a while to load the model into the memory. Then it runs. The loading takes like 10-12 seconds. I need a lighter weight model for quick answers, or keep the session open? i can make 2 scripts, one where session is kept open and another that is a quick job
# I think a lot of the time I want to run with a fresh context, need to look into how to refresh the context if I keep the model loaded
# Let's make a tkinter GUI!!! or the like :D
# Lighter weight models are only really good for single prompts and becomes "stuck" as the chat session continues

### Research & To Do
# How to keep session running?
    # In addition to keeping the script running (?), use keyword "keepalive"
# How to "reset" context, if I want to keep the model session running/loaded on memory
# tkinter gui?
# Highlight text on webpage, right-click, run AI script, load response into paste clipboard

import ollama
from GUI import Window

# Init GUI
Window()    # need to run the AI concurrently with the GUI

# Init ollama client
client = ollama.Client()

# Define model and input prompt

#model = "deepseek-r1:8b" # takes 10-12 seconds to load to memory
#model = "qwen3.5:4b"    # this model thinks WAAAY to much. Is trash.
model = "deepseek-r1:1.5b"  # this one is perfect for quick jobs, doesn't take too long at all.
prompt = "What is Python?"

# Send query to model
response = client.generate(model=model, prompt=prompt)

print("Response from Ollama:")
print(response.response)
