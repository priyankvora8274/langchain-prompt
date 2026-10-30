from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model='gpt-5.2')

chat_history = [
    SystemMessage(content="You are helpful assistant, act as an AI Engineer"),
    HumanMessage(content="Tell me about OpenAI in 2 lines")
]

model_op = model.invoke(chat_history)
chat_history.append(AIMessage(content=model_op.content))

print(chat_history)