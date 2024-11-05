# Documentação do Projeto Chatbot Interativo

## Visão Geral
Este projeto é um chatbot interativo que utiliza um modelo de linguagem (LLM) para responder a perguntas dos usuários e verificar a veracidade das informações fornecidas. O chatbot armazena respostas consideradas verdadeiras em um banco de dados Weaviate.

## Tecnologias Usadas
[**- Streamlit**](https://docs.streamlit.io/develop): Para a interface do usuário.

[**- LangGraph**](https://langchain-ai.github.io/langgraph/tutorials/introduction/): Para manipulação e estruturação de dados.

[**- LangChain**](https://python.langchain.com/docs/tutorials/): Para integração com modelos de ]linguagem.

[**- Groq (Meta - LLaMA-3.1-70B Versatile)**](https://console.groq.com/docs/overview): Modelo de linguagem utilizado para gerar respostas e verificar a veracidade de afirmações.

[**- Weaviate**](https://weaviate.io/developers/weaviate): Banco de dados de vetores para armazenar respostas verificadas.


## Requisitos Necessários

1- Python 3.8 ou superior

2- Docker e Docker Compose

## Instalação
Para instalar as dependências do projeto, siga os passos abaixo:

**Clone o repositório:**

```
git clone https://seu-repositorio-url.git
cd nome-do-repositorio
```

## Configurar as Variaveis de Ambiente

Copiar o .env.example e renomear para .env
```
cp .env.example .env
```

**Adicionar sua chave Key do Groq no .env**

`GROQ_API_KEY="YOUR KEY"`

[Obter a chave key aqui](https://console.groq.com/keys).


## Execução da Aplicação
Para executar a aplicação, utilize o seguinte comando:

``` 
docker-compose up
```
Isso abrirá a aplicação em seu navegador padrão em http://localhost:8501.

**OBS:**
Para que o chatbot funcione corretamente, verifique se o nome do container do Weaviate é o mesmo que está no .env
`WEAVIATE_URL=http://chatbot-job-test-vector-db-1:8080`


## Estrutura do Projeto
A estrutura do projeto é a seguinte:


```
├── app.py               # Código principal da aplicação
├── vector_db.py         # Módulo do banco de dados Weaviate
├── verify_statement.py  # Módulo para verificar a veracidade das informações
├── llm.py               # Configurações do modelo de linguagem
├── requirements.txt     # Dependências do projeto
├── Dockerfile           # Criação das imagens
├── docker-compose.yml   # Execução dos containers
└── README.md            # Esta documentação
```

## Uso
Após iniciar a aplicação, você verá um campo de texto onde pode digitar suas perguntas. O chatbot responderá e, se a resposta for considerada verdadeira, será armazenada no banco de dados.

Digite sua pergunta no campo de entrada.
Pressione Enter ou clique no botão para enviar.
O chatbot retornará uma resposta e armazenará a resposta se for considerada verdadeira.


## Exemplos de Uso
Fazer uma pergunta: "Qual é a capital do Brasil?"

Verificação de afirmação: "O céu é verde?" — O chatbot irá verificar a veracidade dessa afirmação.