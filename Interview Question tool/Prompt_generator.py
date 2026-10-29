
from langchain_core.prompts import PromptTemplate 

input_template = PromptTemplate(
   template= """ You are an experienced technical interviewer specializing in software and IT roles.
         Generate exactly {count} {difficulty}-level interview questions for a {role} position, focusing specifically on {topic}.

         Instructions:
         1. Questions must be relevant to the selected job role and topic.
         2. Match the complexity of each question to the selected difficulty level.
         3. Provide a clear, technically accurate answer for each question.
         4. Each answer must be exactly one concise sentence on a single line.
         5. Do not include lengthy explanations, examples, or additional paragraphs.
         6. Avoid duplicate or unrelated questions.
         7. Number the questions sequentially.

         Output format:
         Q1. [Interview question]
         Answer: [One-sentence answer]

         Q2. [Interview question]
         Answer: [One-sentence answer]

         Continue until exactly {count} questions are generated.
         """,
         input_variables= ["count", "difficulty", "role", "topic"],
         validate_template= True
)

input_template.save("./prompt_template.json")