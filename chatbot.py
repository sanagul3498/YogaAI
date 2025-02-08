import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, ToolMessage

llm = ChatOpenAI(
    temperature=0.5,
    )
PROMPT = """You are a funny yoga instructor. You could define the health benefits of yoga in a fuuny way.
you will always use emojis and jokes in your answers.
"""
messages = [SystemMessage(PROMPT)]

while True:
    question = input("You: ")
    messages.append(HumanMessage(question))
    response = llm.invoke(messages)
    messages.append(response)
    print("Chatbot:", response.content, "\n")

      