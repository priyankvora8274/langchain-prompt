# AI Interview Question Generator

A simple AI application built with **Streamlit**, **LangChain**, and **OpenAI**. Users select a job role, difficulty, topic, and number of questions. The application dynamically generates interview questions with **one-sentence answers**.

## Why use LangChain PromptTemplate instead of Python f-strings?

Python f-strings are useful for simple string formatting, but LangChain's `PromptTemplate` provides a structured, reusable prompt component that integrates with the rest of a LangChain application.

### 1. Template validation and input checking

LangChain identifies input variables in a template and checks that required values are provided when formatting or invoking it. You can also enable template validation to catch certain template/input-variable mismatches during construction.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Generate {count} {difficulty} interview questions about {topic}.",
    input_variables=["count", "difficulty", "topic"],
    validate_template=True,
)

# Missing 'topic' raises an error when formatting.
# prompt.format(count=5, difficulty="Beginner")
```

**Important:** This is *not* full validation of user input or AI-generated answers. Validate free-text topics separately, and use structured output or application checks when you need strict response formatting.

### 2. Reusable and maintainable prompts

Define a prompt once, then reuse it with different inputs instead of duplicating long f-strings throughout the codebase. Templates can also be stored in a separate Python module or text file and loaded by the application.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Generate {count} {difficulty} interview questions for a {role} focusing on {topic}. "
    "Give exactly one concise sentence as the answer to each question."
)

first = prompt.format(count=3, difficulty="Beginner", role="Data Engineer", topic="SQL")
second = prompt.format(count=5, difficulty="Advanced", role="DevOps Engineer", topic="Kubernetes")
```

You can keep the template in `prompts.py` and import it anywhere in your project. For a plain-text file, load its contents and pass them to `PromptTemplate.from_template(...)`.

### 3. Native integration with the LangChain ecosystem

Prompt templates work directly with LangChain models, output parsers, and chains. The `|` operator composes these components into a reusable pipeline.

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

prompt = PromptTemplate.from_template(
    "Generate {count} {difficulty} interview questions for a {role} about {topic}. "
    "Format each as Q: [question] followed by Answer: [one concise sentence]."
)

model = ChatOpenAI(model="gpt-4.1-mini")
chain = prompt | model | StrOutputParser()

result = chain.invoke({
    "count": 3,
    "difficulty": "Beginner",
    "role": "Data Engineer",
    "topic": "SQL",
})
print(result)
```

## Comparison: f-strings vs. PromptTemplate

| Feature | Python f-string | LangChain PromptTemplate |
|---|---|---|
| Variable substitution | Yes | Yes |
| Required-input checks | Python evaluates referenced expressions | Checks template variables during formatting/invocation |
| Template validation | No dedicated template validator | Optional template validation |
| Reuse across calls | Possible with functions | Built-in reusable prompt object |
| Save in separate files | Possible with additional code | Straightforward to store and load |
| LangChain chain composition | Needs wrapping/adaptation | Direct support for `prompt \| model \| parser` |