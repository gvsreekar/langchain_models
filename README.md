# 🧠 Research Tool using LangChain + Streamlit + OpenAI

This is a simple research summarization tool built with **LangChain**, **Streamlit**, and **OpenAI GPT-4**. It generates tailored summaries of popular research papers based on user preferences like explanation style and length.

---

## 📁 Project Structure

├── research_tool.py # Streamlit app interface
├── template_generator.py # Script to generate the prompt template
├── template.json # Prompt template generated from script
├── pyproject.toml # Poetry dependency manager file
├── .env # Contains the OpenAI API key (not to be committed)

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gvsreekar/langchain_models.git
cd langchain_models
2️⃣ Install dependencies (using Poetry)
Make sure Poetry is installed.

bash
Copy
Edit
poetry install
3️⃣ Set up your .env file
Create a .env file in the root directory and add:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
🔐 Never commit your .env file to GitHub. Add it to .gitignore.

🧪 Generate or Update the Prompt Template
Run the following to generate or update template.json:

bash
Copy
Edit
poetry run python template_generator.py
🚀 Run the Streamlit App
bash
Copy
Edit
poetry run streamlit run research_tool.py
Then open the link shown in your terminal (typically http://localhost:8501).
