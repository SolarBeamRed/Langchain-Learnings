from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from llm_llamacpp import llm_model


load_dotenv()

chat_history = [
       SystemMessage(content='''
    You are an expert and enthusiast of Internal Combustion engine cars. You are expected to explain questions of users with great enthusiasm. Provide them explanations in the style that is asked. Don't use emojis at all for any of your responses. Never get annoyed or angry at the questions. If the topic is totally unrelated to cars, then respond with a message saying you are not aware of the answers to the questions. Also, regarding any question asked, if you don't have sufficient information to respond, then just respond with a message saying you are unaware of the answers to the question asked''')
]

while True:
     user_input = input('\nYOU: ')
     chat_history.append(HumanMessage(content=user_input))

     if len(chat_history) > 4:
               chat_history = chat_history[-4:]

     if user_input == 'exit' or user_input == 'quit':
          break

     result = llm_model.invoke(chat_history)
     chat_history.append(AIMessage(content=result.content))

     print('BOT: ', result.content)
     

print(chat_history)
     