import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from data_retriever import web_database


@tool
def get_web_data(question):
    """
    Returns the data from the web pages : data is about yoga postures as per age
    """
    return web_database(question)

tool = [
   get_web_data
]

llm = ChatOpenAI(
    temperature=0.5,
    )
PROMPT = """You are a yoga instructor.
You will greet the users in a nice way.
 You could define the health benefits of yoga.
You will always use emojis and jokes in your answers.
You will tell them how important yoga is for not only our physical health but mental health.
You will talk about different yoga postures suitable for different age types.
You will tell the famous and most suitable yoga postures for teens, men and women.
"""
messages = [SystemMessage(PROMPT)]

def chat(question):
    messages.append(HumanMessage(question))
    response = llm.invoke(messages)
    messages.append(response)

    if response.tool_calls:
       for tool_call in response.tool_calls:
            if tool_call['name'] == 'get_web_data':
            
               question = tool_call['args']['question']
               messages.append(ToolMessage(get_web_data.invoke(input=question),tool_call_id=tool_call['id']))
 

    response = llm.invoke(messages)
    messages.append(response)

    return response.content

print(chat("what is the most famous yoga pose?"))
      
