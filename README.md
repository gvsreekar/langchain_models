# 🧠 Research Paper Summarization Tool

A simple yet powerful research assistant built using **LangChain**, **OpenAI's GPT-4**, and **Streamlit**. It allows users to generate customized summaries of well-known AI research papers with selectable styles and lengths — perfect for both beginners and professionals.

---

## 🚀 Features

- 🔍 Choose from popular research papers (e.g., GPT-3, BERT, Transformers)
- 🎨 Select your preferred explanation style: Beginner-Friendly, Technical, Code-Oriented, or Mathematical
- 📏 Control the summary length: Short, Medium, or Long
- 🧠 Summaries are generated using OpenAI’s GPT-4 via LangChain
- ⚙️ Easy prompt customization using a `PromptTemplate` with JSON storage

---

## 📁 Project Structure

langchain_models/
│
├── research_tool.py # Streamlit UI and LangChain model logic
├── template_generator.py # Code to generate the prompt template
├── template.json # Serialized prompt template (auto-generated)
├── pyproject.toml # Poetry project & dependency manager file
└── .env # (Optional) API keys and secrets


---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gvsreekar/langchain_models.git
cd langchain_models

### 2️⃣ Install dependencies (using Poetry)
Make sure Poetry is installed.

```bash
poetry install

### 3️⃣ Set up your .env file
Create a .env file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here (Replace your OpenAI API key here)

### 🧪 Add or Update the Prompt Template
If you need to update or regenerate the prompt template, simply run:

```bash
poetry run python template_generator.py

### 🏃‍♂️ Run the App
Use Poetry to run your Streamlit app:

```bash
poetry run streamlit run research_tool.py

