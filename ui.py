import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from lexer import json_analyze

def create_ui():
    def select_file():
        path = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    input_text.delete(1.0, tk.END)
                    input_text.insert(tk.END, content)
                    result_text.config(state=tk.NORMAL)
                    result_text.delete(1.0, tk.END)
                    result_text.config(state=tk.DISABLED)
                    lexically_analyze()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    # Faz a análise léxica
    def lexically_analyze():
        content = input_text.get(1.0, tk.END)
        try:
            tokens, errors = json_analyze(content)
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)

            if errors:
                result_text.insert(tk.END, "Erros encontrados:\n", "error")
                for e in errors:
                    result_text.insert(tk.END, e + "\n", "error")
                # result_text.insert(tk.END, "\n")

            for token in tokens:
                result_text.insert(tk.END, token + "\n")
            result_text.config(state=tk.DISABLED)
        except SyntaxError as e:
            messagebox.showerror("Erro Léxico", str(e))

    window = tk.Tk()
    window.title("Analisador Léxico de JSON")
    window.geometry("800x900")

    select_file_button = tk.Button(window, text="Selecionar arquivo JSON", command=select_file)
    select_file_button.pack(pady=10)

    input_label = tk.Label(window, text="Conteúdo do JSON:")
    input_label.pack()
    input_text = scrolledtext.ScrolledText(window, height=15)
    input_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    analyze_button = tk.Button(window, text="Analisar", command=lexically_analyze)
    analyze_button.pack(pady=10)

    result_label = tk.Label(window, text="Tokens gerados:")
    result_label.pack()
    result_text = scrolledtext.ScrolledText(window, height=15)
    result_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    result_text.config(state=tk.DISABLED)

    window.mainloop()