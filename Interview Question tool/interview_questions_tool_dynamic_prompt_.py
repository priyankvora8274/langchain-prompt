from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model = 'gpt-5.2')
input_template = load_prompt("prompt_template.json")

st.title("Interview Question Generator") 

# take input from users
job_role_ip = st.selectbox("Job Role",["Software Engineer", "Data Engineer", "DevOps Engineer", "AI Engineer", "Data Analyst", "Cloud Engineer"])
difficulty_ip = st.selectbox("Difficulty of questions",["Beginner", "Intermediate", "Advanced"])
topic_ip = st.text_input("On which Topic you want qustions?")
count_ip =  st.selectbox("Number of Questions",[3, 5, 10, 15])

#invoke prompt template to configure with dynamoc input from users
prompt = input_template.invoke({
   "count":count_ip, 
   "difficulty":difficulty_ip, 
   "role":job_role_ip, 
   "topic":topic_ip
   }
)

if st.button("Send"):
   model_op = model.invoke(prompt)
   st.write(model_op.content) 
