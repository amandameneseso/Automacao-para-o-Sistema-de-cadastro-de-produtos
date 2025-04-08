import pyautogui
import time

# pausa entre os comandos
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("brave") # ou: pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # tempo para o navegador carregar

# Passo 2: Fazer login
pyautogui.press("tab") # ou pegando a posição do mouse: pyautogui.click(x=370, y=375)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3) # tempo para o navegador carregar

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto

# pyautogui.press("tab")
# codigo = "MOLO000251"
# pyautogui.write(codigo)

# pyautogui.press("tab") # passa para o próximo campo
# marca = "Logitech"
# pyautogui.write(marca)

# pyautogui.press("tab")
# tipo = "Mouse"
# pyautogui.write(tipo)

# pyautogui.press("tab")
# categoria = "1"
# pyautogui.write(categoria)

# pyautogui.press("tab")
# preco_unitario = "25.95"
# pyautogui.write(preco_unitario)

# pyautogui.press("tab")
# custo = "6.50"
# pyautogui.write(custo)

# pyautogui.press("tab")
# obs = ""
# pyautogui.write(obs)

# pyautogui.press("tab") # passa para o botão "enviar"
# pyautogui.press("enter")

# Passo 5: Repetir para todos os produtos

for linha in tabela.index:
    pyautogui.press("home") # ou: pyautogui.scroll(1000) -> rolar a página para cima

    pyautogui.click(x=821, y=254)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passa para o próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "NaN": # escreve obs apenas se não for vazio
        pyautogui.write(obs)

    pyautogui.press("tab") # passa para o botão "enviar"
    pyautogui.press("enter")



