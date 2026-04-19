# setup a GUI for interacting with local LLM

import tkinter as tk
from tkinter import filedialog, ttk
import pypdf

class Window:
    def __init__(self, llama):
        self.llama = llama
        
        self.root = tk.Tk()
        self.root.title("Local LLM RAG System")
        self.root.geometry("600x700")

        # --- Data Variables ---
        self.loaded_file_data = ""
        self.selected_model = tk.StringVar()
        
        # --- Button Bar (top) ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side="top", fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="Clear",      command=self.clear).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Load File",  command=self.load_file).pack(side="left", padx=4)
        # tk.Button(btn_frame, text="Settings",   command=self.settings).pack(side="left", padx=4)
        dropdown = ttk.Combobox(btn_frame, textvariable=self.selected_model, values=llama.available_models, state="readonly", width=40)
        dropdown.pack(side="left", padx=4)
        dropdown.current(0)


        # --- Output Box (middle, expands) ---
        tk.Label(self.root, text="Output:").pack(anchor="w", padx=10)
        self.output = tk.Text(self.root, state="disabled", wrap="word")
        self.output.pack(fill="both", expand=True, padx=10, pady=(0, 5))

        # --- Input Box/ Prompt Area (bottom, fixed height) ---
        prompt_frame = tk.Frame(self.root)
        prompt_frame.pack(side="bottom", fill="both", padx=10, pady=5)

        tk.Button(prompt_frame, text="Send", command=self.send).pack(side="right", padx=4)
        
        tk.Label(prompt_frame, text="Prompt:").pack(anchor="w")
        self.input = tk.Text(prompt_frame, height=5, wrap="word")
        self.input.pack(fill="both", pady=(0, 5))

        # --- 

        self.root.mainloop()

    def send(self):
        input_text = self.input.get("1.0", "end").strip()
        prompt_text = input_text
        if not input_text:
            return
        # use LLM to generate response from user_text

        # basic implementation of RAG, but there is a better way to do this I believe using embedding
        if self.loaded_file_data:
            prompt_text += " " + self.loaded_file_data

        output_text = self.llama.generate(prompt_text)
        
        self.write_output(f"You: {input_text}\nLLM: {output_text}\n\n")
        self.input.delete("1.0", "end")

    def clear(self):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")

    def load_file(self):
        # 1. I need to open and choose the right file
        # 2. Save file to class variable
        # 3. I'd like to show that a file is loaded?
        self.write_output("[File Loaded]\n")
        filepath = filedialog.askopenfilename()
        print(filepath)

        if (filepath.endswith(".pdf")):
            with open(filepath, "rb") as f:
                reader = pypdf.PdfReader(f)
                content = ""
                for page in reader.pages:
                    content += page.extract_text()
                print(content)
                self.loaded_file_data = content
        else:
            with open(filepath, "r") as f:
                content = f.read()
                print(content)
                self.loaded_file_data = content


    def settings(self):
        self.write_output("[Settings clicked]\n")

    def write_output(self, text):
        self.output.config(state="normal")
        self.output.insert("end", text)
        self.output.config(state="disabled")
        self.output.see("end")  # auto-scroll to bottom
