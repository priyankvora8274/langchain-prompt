from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
        ('system', 'you are helpful {domain} expert'),
        ('human', 'Tell me about the {topic} in simple language')
    ]
)

prompt = chat_template.invoke({'domain':'Sports', 'topic':'superball'})

print(prompt)