🤖 AI Notes Summarizer with FastAPI

A simple AI Backend Project that summarizes long notes into bullet-point summaries using FastAPI + Ollama Local LLM.

Runs completely locally — no cloud API required.

📂 Project Structure
AI_Notes_Summarizer_with_Fast_API
│
├── App
│   ├── Data_Base
│   │   ├── database.py
│   │   └── models.py
│   ├── Schema
│   │   └── Pydantic_model.py
│   ├── main.py
│   └── summary.db
│
├── requirements.txt
└── README.md
📦 requirements.txt

🚀 What This Project Does

✅ Accepts long text notes
✅ Uses Local AI Model (Gemma 2B)
✅ Generates bullet summaries
✅ Saves history in SQLite database
✅ Provides REST APIs
✅ Delete history support

⚙️ Step 1 — Install Ollama

Download Ollama:

👉 https://ollama.com/download

Install normally.
Check installation:
ollama --version
If version appears → ✅ Installed.

🧠 Step 2 — Download AI Model

This project uses Gemma 2B.
Run:- ollama pull gemma:2b

Model will download locally.
(First time may take few minutes.)

