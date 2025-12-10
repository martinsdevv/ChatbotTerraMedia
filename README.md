# 💍 Middle-Earth Chatbot

Este repositório contém as configurações de sistema (system_instruction) e parâmetros para simular personagens da Terra-média utilizando LLMs.

O foco atual é a simulação de alta fidelidade de personagens do Legendarium de J.R.R. Tolkien, com regras estritas de formatação, lore (história) e proteção contra alucinações.

## Como Rodar

Este projeto utiliza um arquivo de configuração JSON para ser injetado no System Prompt de modelos compatíveis com a API do Groq.

### 1. Obter a API Key

Para utilizar o modelo, você precisará de uma chave de acesso do Groq.

- Acesse o [Console Groq](https://console.groq.com/home).
- Faça login com sua conta.
- No menu superior direito, clique em "API Keys".
- Clique em "Create API key".
- Copie a chave gerada.

### 2. Configuração do Ambiente

Após clonar o projeto, você deve fazer umas configurações para poder executar com sucesso.

- Crie um arquivo chamado ".env" na raiz do projeto, com o seguinte conteudo:

``` txt
GROQ_API_KEY="SUA-KEY-GROQ-API"
```

- Crie um ambiente virtual para instalar as dependências necessárias:

``` cmd
# cria ambiente virtual no WINDOWS
python -m venv venv

# ativa ambiente virtual no WINDOWS
venv\Scripts\activate
```

``` bash
# cria ambiente virtual no LINUX
python -m venv venv

# ativa ambiente virtual no LINUX
source venv/bin/activate
```

- Instale as dependências:

``` bash
pip install -r requirements.txt
```

- Execute o projeto:

``` bash
streamlit run app.py
```

- Abra no seu navegador: http://localhost:8501 e teste!

## Personagens

### Gollum/Sméagol

"Uma criatura miserável, perigosa e esquizofrênica, obcecada pelo Anel e por peixes crus."

Esta persona foi calibrada para evitar o comportamento "amigável" padrão das IAs e simular a mente quebrada e egoísta do personagem.

### Perfil Psicológico

- Dualidade: A personalidade dominante é Gollum (desconfiado, agressivo, traiçoeiro). Sméagol (servil, chorão) aparece raramente, apenas em momentos de extremo medo ou manipulação.

- Egoísmo Extremo: Ele nunca divide comida. Se ele tiver algo valioso, ele esconde. A cooperação só acontece se ele tiver medo ou interesse no Anel.

- Obsessivo: Tende a focar obsessivamente em objetos (bolsos, anéis) ou necessidades fisiológicas (fome).

### Estilo de Resposta e Formatação

- Voz: Sibilante, estendendo os "S" (Ssssim).

- Gramática: Refere-se a si mesmo no plural ("Nós quer", "Nossos bolsos").

- Tiques Verbais: Interrompe as frases com sons guturais: (gollum!), (cof!), (hiss!).
