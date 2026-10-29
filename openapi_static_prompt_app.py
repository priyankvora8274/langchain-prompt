from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOpenAI(model = 'gpt-5.2', max_completion_tokens=10)

st.title("Research Tool") 

user_input = st.text_input("Enter your prompt:")

if st.button("Send"):
   model_op = model.invoke(user_input)
   st.write(model_op.content) 
