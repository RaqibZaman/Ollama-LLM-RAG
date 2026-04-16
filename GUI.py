# setup a GUI for interacting with local LLM

import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Local LLM RAG System")
        # self.root.attributes("-topmost", True)

        self.root.geometry("300x150")

        tk.Label(self.root, text="Enter your name: ").pack(pady=5)

        self.entry = tk.Entry(self.root, width=25)
        self.entry.pack()

        tk.Button(self.root, text="Greet", command=self.greet).pack(pady=5)

        self.label = tk.Label(self.root, text="")
        self.label.pack()

        self.root.mainloop()


    def greet(self):
            name = self.entry.get()
            self.label.config(text=f"Hello, {name}!")
