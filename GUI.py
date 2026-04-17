# setup a GUI for interacting with local LLM

import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Local LLM RAG System")
        self.root.geometry("600x500")

        # --- Button Bar (top) ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(side="top", fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="Send",       command=self.send).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Clear",      command=self.clear).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Load File",  command=self.load_file).pack(side="left", padx=4)
        tk.Button(btn_frame, text="Settings",   command=self.settings).pack(side="left", padx=4)

        # --- Output Box (middle, expands) ---
        tk.Label(self.root, text="Output:").pack(anchor="w", padx=10)
        self.output = tk.Text(self.root, state="disabled", wrap="word")
        self.output.pack(fill="both", expand=True, padx=10, pady=(0, 5))

        # --- Input Box (bottom, fixed height) ---
        tk.Label(self.root, text="Input:").pack(anchor="w", padx=10)
        self.input = tk.Text(self.root, height=5, wrap="word")
        self.input.pack(fill="x", padx=10, pady=(0, 10))

        self.root.mainloop()

    def send(self):
        user_text = self.input.get("1.0", "end").strip()
        if not user_text:
            return
        self.write_output(f"You: {user_text}\nLLM: (response here)\n\n")
        self.input.delete("1.0", "end")

    def clear(self):
        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")

    def load_file(self):
        self.write_output("[Load File clicked]\n")

    def settings(self):
        self.write_output("[Settings clicked]\n")

    def write_output(self, text):
        self.output.config(state="normal")
        self.output.insert("end", text)
        self.output.config(state="disabled")
        self.output.see("end")  # auto-scroll to bottom


Window()
