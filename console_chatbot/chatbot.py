from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model = 'gpt-5.2')

chat_memory = []
while True:
    input_text = input("You:")
    chat_memory.append(input_text)
    
    if input_text == "exit":
        break
    
    model_op = model.invoke(chat_memory)
    chat_memory.append(model_op.content)
    print("AI: ",model_op.content)
    
print(chat_memory)
    