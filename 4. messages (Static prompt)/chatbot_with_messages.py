from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model = 'gpt-5.2')

chat_memory = [SystemMessage(content="You are helpful virtual chat assistant")]
while True:
    input_text = input("You:")
    chat_memory.append(HumanMessage(content=input_text))
    
    if input_text == "exit":
        break
    
    model_op = model.invoke(chat_memory)
    chat_memory.append(AIMessage(content=model_op.content))
    print("AI: ",model_op.content)
    
print(chat_memory)
    