# Sistema de Cadastro de Produtos - Automação com Python

[![Licença MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositório contém um script Python que automatiza o processo de preenchimento de formulário em um sistema web (https://amandameneseso.github.io/Sistema-de-cadastro-de-produtos/). A automação é realizada utilizando a biblioteca `pyautogui` e os dados são provenientes de um arquivo `.csv`.

## Conteúdo do Repositório

Este repositório contém os seguintes arquivos:

-   `interface.py`: O script principal em Python responsável por abrir o navegador, realizar o login no sistema web e preencher o formulário de cadastro de produtos com os dados do arquivo `produtos.csv`.
-   `produtos.csv`: Um arquivo no formato CSV que serve como base de dados, contendo as informações dos produtos a serem cadastrados automaticamente no sistema web.
-   `codigo.csv`: O código escrito inicialmente para implementação do projeto.

## Como Funciona?

O script `interface.py` simula as interações de um usuário humano com a interface web, realizando automaticamente as seguintes ações:

1.  **Abre o navegador web** (compatível com Chrome) e acessa o link do sistema de cadastro de produtos.
2.  **Realiza o login** no sistema web utilizando as credenciais (e-mail e senha) que podem ser escritos aleatoriamente.
3.  **Lê os dados do arquivo `produtos.csv`**, linha por linha, representando cada produto a ser cadastrado.
4.  **Preenche automaticamente os campos do formulário de cadastro** com os dados correspondentes de cada produto extraído do CSV.
5.  **Submete** cada produto individualmente, cadastrando-o no sistema.

##  Como Usar

Para utilizar este script de automação, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/amandameneseso/Automacao-para-o-Sistema-de-cadastro-de-produtos.git
    cd Automacao-para-o-Sistema-de-cadastro-de-produtos
    ```
    
2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * **No Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **No Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências:**
    ```bash
    pip install pyautogui pandas
    ```

5.  **Execute o script:**
    ```bash
    python interface.py
    ```
    *(Certifique-se de que o sistema web de cadastro (https://amandameneseso.github.io/Sistema-de-cadastro-de-produtos/) esteja aberto e na página de login antes de executar o script).*

## Tecnologias Utilizadas

Este projeto utiliza as seguintes tecnologias:

-   [Python](https://www.python.org/) 3.10+
-   [PyAutoGUI](https://pyautogui.readthedocs.io/)
-   [Pandas](https://pandas.pydata.org/)

##  Observações Importantes

-   Certifique-se de que o navegador web Chrome esteja instalado no seu sistema.
-   É crucial não interagir com o mouse ou teclado durante a execução do script, pois isso pode interferir na automação e causar erros.
-   Mantenha a resolução da tela do seu computador e a posição dos elementos (campos, botões) na página web consistentes com o esperado pelo código do script. Alterações na interface podem exigir ajustes no script.
-   O script assume que a página de login e o formulário de cadastro possuem uma estrutura específica. Qualquer modificação na interface web pode quebrar a funcionalidade do script.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Você é livre para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, sujeito às condições da Licença MIT.

## Interface Web do Sistema

A interface HTML do sistema de cadastro de produtos pode ser acessada separadamente em:

[https://amandameneseso.github.io/Sistema-de-cadastro-de-produtos](https://amandameneseso.github.io/Sistema-de-cadastro-de-produtos)

---
