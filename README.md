# 🤖 AI Interview Question Repository

An AI-powered Python application that automatically generates interview questions for any subject or technology using an LLM and stores them in both **SQLite Database** and **JSON** format.

This project helps students, job seekers, and developers quickly create and maintain a repository of interview questions for learning and interview preparation.

---

## ✨ Features

* 🎯 Generate interview questions for any topic or technology
* 🤖 Uses an LLM to create relevant questions
* 💾 Store questions in an SQLite database
* 📄 Save questions in JSON format
* 🔍 Build a reusable repository of interview questions
* 🖥️ Simple command-line interface (CLI)
* 📚 Helpful for interview preparation and revision

---

## 🛠️ Tech Stack

* **Python**
* **SQLite3**
* **JSON**
* **Groq API / LLM**
* **python-dotenv**

---

## 📁 Project Structure

```text
Interview_Question_DB/
│
├── app.py                    # Main application
├── llm.py                    # Generates interview questions using LLM
├── database.py               # SQLite database operations
├── json_manager.py           # JSON file handling
├── requirements.txt          # Project dependencies
├── .env                      # API keys (not pushed to GitHub)
├── .gitignore
│
├── database/
│   └── interview_questions.db
│
└── data/
    └── questions.json
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Interview_Question_DB.git
cd Interview_Question_DB
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
python app.py
```

---

## 📖 How It Works

1. Enter a subject or technology.
2. The LLM generates interview questions.
3. Questions are displayed in the terminal.
4. Newly generated questions are stored in:

   * SQLite Database
   * JSON File
5. The repository keeps growing with every new topic.

---

## 💡 Example

```text
==================================================
AI Interview Question Repository
==================================================

Enter Subject or Topic: Python

Top 50 Interview Questions

1. What is Python?
2. What are Python data types?
3. What is a list in Python?
...
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Working with Large Language Models (LLMs)
* Database integration using SQLite
* Reading and writing JSON files
* Environment variable management
* Modular Python programming
* Building command-line applications
* Data persistence and repository management

---

## 🚀 Future Enhancements

* Streamlit web interface
* Search questions by topic
* Difficulty-based question generation
* Export questions to PDF
* Add answer generation feature
* Question tagging and filtering

---

## 👩‍💻 Author

**Bhakti Jadhav**

Aspiring Python Developer | AI & ML Learner | Building Projects One Step at a Time

⭐ If you found this project useful, consider giving it a star on GitHub!
