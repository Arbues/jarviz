import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Environment Variables
API_KEY = os.getenv("GROQ_API_KEY")


# Initialize Model
def init_model():
    return ChatGroq(model="llama3-8b-8192", temperature = 0.2)


# Conversation History
conversation_history = [
    ("system", "Eres un asistente virtual de la Asociación Científica Especializada en Computación, llamada Acecom. "
               "Tu nombre es LemurIA. Responderás de manera amable, concisa y dialogando con el usuario"
               "Vas a recibir a la entrada de miembros de Acecom al local con un mensaje de bienvenida agradable."),
    ("human", "Responde a {usuario}.")
    # ("ai", "¡Hola! Soy Lemuria, el asistente virtual de Acecom. ¡Es un placer recibirte {usuario}! ¿En qué puedo ayudarte hoy?")
]


# Handle Query
def handle_query(query):
    # Init model chain
    llm = init_model()
    prompt = ChatPromptTemplate.from_messages(conversation_history)
    groq_chain = prompt | llm

    # Generate response
    response = groq_chain.invoke({"usuario": query})

    # Actualize conversation history
    conversation_history.append(("human", query))
    conversation_history.append(("ai", response.content))
    return response.content

if __name__ == "__main__":
    print(handle_query("Andre"))