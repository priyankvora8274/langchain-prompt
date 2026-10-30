from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_history = []

template = ChatPromptTemplate([
    ('system','You are virtual customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

with open('previous_customer_support_chat.txt') as f:
    chat_history.extend(f.readlines())
    
prompt = template.invoke({'chat_history':chat_history,'query':'What is the status of my refund?'})

print(prompt)