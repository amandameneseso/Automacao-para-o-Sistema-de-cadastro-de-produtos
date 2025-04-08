import pyautogui
import time
import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog

# Variável para armazenar o caminho do CSV
caminho_csv = ""

def selecionar_csv():
    global caminho_csv
    caminho_csv = filedialog.askopenfilename(
        title="Selecione a base de produtos (CSV)",
        filetypes=[("Arquivos CSV", "*.csv")]
    )
    if caminho_csv:
        label_csv.config(text=f"Selecionado:\n{caminho_csv}")

def iniciar_automacao():
    if not caminho_csv:
        messagebox.showwarning("Atenção", "Selecione o arquivo CSV primeiro.")
        return

    try:
        pyautogui.PAUSE = 0.5

        # Passo 1: Entrar no sistema
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")
        pyautogui.write("https://amandameneseso.github.io/Sistema-de-cadastro-de-produtos/")
        pyautogui.press("enter")
        time.sleep(3)

        # Passo 2: Fazer login
        pyautogui.press("tab")
        pyautogui.write("teste@gmail.com")
        pyautogui.press("tab")
        pyautogui.write("senha123")
        pyautogui.press("tab")
        pyautogui.press("enter")
        time.sleep(3)

        # Passo 3: Importar a base de dados
        tabela = pd.read_csv(caminho_csv)

        # Passo 4 e 5: Cadastrar os produtos
        for linha in tabela.index:
            pyautogui.press("home")
            pyautogui.click(x=821, y=254)
            pyautogui.write(tabela.loc[linha, "codigo"])

            pyautogui.press("tab")
            pyautogui.write(tabela.loc[linha, "marca"])

            pyautogui.press("tab")
            pyautogui.write(tabela.loc[linha, "tipo"])

            pyautogui.press("tab")
            pyautogui.write(str(tabela.loc[linha, "categoria"]))

            pyautogui.press("tab")
            pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

            pyautogui.press("tab")
            pyautogui.write(str(tabela.loc[linha, "custo"]))

            pyautogui.press("tab")
            obs = str(tabela.loc[linha, "obs"])
            if obs.lower() != "nan":
                pyautogui.write(obs)

            pyautogui.press("tab")
            pyautogui.press("enter")

        messagebox.showinfo("Sucesso", "Automação concluída com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Interface
janela = tk.Tk()
janela.title("Automação de Cadastro")
janela.geometry("400x300")

titulo = tk.Label(janela, text="Cadastro Automático", font=("Arial", 16))
titulo.pack(pady=10)

botao_arquivo = tk.Button(janela, text="Selecionar CSV", command=selecionar_csv, font=("Arial", 12))
botao_arquivo.pack(pady=5)

label_csv = tk.Label(janela, text="Nenhum arquivo selecionado", font=("Arial", 10), wraplength=350)
label_csv.pack(pady=5)

botao_iniciar = tk.Button(janela, text="Iniciar Automação", command=iniciar_automacao, bg="#4CAF50", fg="white", font=("Arial", 12))
botao_iniciar.pack(pady=20)

janela.mainloop()
