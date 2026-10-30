# LangChain Prompt Engineering

A hands-on collection of Python examples exploring **prompt engineering with LangChain**, from static prompts to conversational workflows with dynamic inputs and message history.

This repository is organized as a series of small learning exercises for understanding how prompts and messages can be structured when building applications powered by large language models (LLMs).

## Topics Covered

- **Static prompts:** Start with fixed instructions and prompt content.
- **Interview question tool:** Explore a prompt-driven interview question use case.
- **Console chatbot:** Experiment with a conversational interface in the terminal.
- **Message-based static prompts:** Learn how chat messages can be organized.
- **Dynamic prompts in multi-turn conversations:** Work with prompts that change based on inputs and conversation context.
- **Message placeholders:** Explore reusable templates that accommodate message sequences.

## Repository Structure

```text
langchain-prompt/
├── 1. Static Prompt/
├── 2. Interview Question tool/
├── 3. console_chatbot/
├── 4. messages (Static prompt)/
├── 5.Dynamic_prompt_in_multi_turn_convo/
├── 6. message_placeholder/
├── .gitignore
├── requirements.txt
└── README.md
```

Each numbered directory focuses on a different prompting concept. Explore them in order to progress from basic prompts to conversational prompt patterns.

## Tech Stack

- **Language:** Python
- **Framework:** LangChain (`langchain`, `langchain-core`)
- **LLM integrations listed in dependencies:** OpenAI, Anthropic, Google Generative AI, and Hugging Face
- **Additional libraries:** `python-dotenv`, NumPy, and scikit-learn

> The dependencies include multiple model providers; individual examples may use only a subset of them.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/priyankvora8274/langchain-prompt.git
cd langchain-prompt
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API credentials

Create or update your local `.env` file with the credentials required by the example you want to run:

```dotenv
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

You only need credentials for the providers used by the specific example. Check each script for its expected environment variable names.

**Security:** Never commit real API keys or secrets. Make sure `.env` is excluded by `.gitignore`. If a real key has already been committed, revoke or rotate it and remove it from Git history.

### 5. Explore and run an example

Open one of the numbered folders, inspect its Python files, and run the relevant script:

```bash
python path/to/example.py
```

Replace `path/to/example.py` with the actual script path. Some examples may require provider-specific configuration.

## Learning Objectives

By exploring these examples, you can practice:

1. Understanding the difference between fixed and parameterized prompts.
2. Structuring system, human, and assistant messages for chat models.
3. Working with conversation context across multiple turns.
4. Reusing prompt patterns with message placeholders.
5. Applying prompting techniques to interview tools and terminal-based chatbots.

## Possible Next Steps

- Add example inputs and outputs for each exercise.
- Compare responses from different LLM providers.
- Add validation, error handling, and tests.
- Expand the console chatbot with persistent conversation history.

## Author

**Priyank Vora**  
GitHub: [@priyankvora8274](https://github.com/priyankvora8274)

## Contributions

Suggestions, improvements, and pull requests are welcome.

---

*This repository is intended for learning and experimentation with LangChain prompt engineering.*
