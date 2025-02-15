from pymongo import MongoClient, ASCENDING
from datetime import datetime
from langchain_core.messages import AIMessage, SystemMessage,HumanMessage


# connection_string = "mongodb://localhost:27017/"
connection_string = "mongodb+srv://sanagul3498:sAna-1988@cluster0.7frym.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def save_chat(data:dict):
    data['timestamp'] = datetime.now()
    with MongoClient(connection_string) as client:
        client['mus']['chat'].insert_one(data) 

def fetch_chat(user_id:str):
    with MongoClient(connection_string) as client:
        data = list(client['mus']['chat'].find({'user_id':user_id}).sort('timestamp', ASCENDING))

    messages = []

    for message in data:
        if message['role'] == 'assistant':
            messages.append(AIMessage(message['content']))
        elif message['role'] == 'user':
            messages.append(HumanMessage(message['content']))
    
    return messages
