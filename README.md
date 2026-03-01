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

🔥 Step 3 — Start Ollama API Server

Start Ollama:
ollama serve
Ollama API runs at:- http://localhost:11434

This API is used by FastAPI backend.

📥 Step 4 — Install Python Dependencies

Open terminal inside project root folder.
Install all libraries using requirements file:- pip install -r requirements.txt

(No virtual environment required.)

▶️ Step 5 — Run FastAPI Server

Go inside App folder:
cd App
Start server:
uvicorn main:app --reload
Server starts at:- http://127.0.0.1:8000

📘 Step 6 — Open API Documentation

Open browser:- http://127.0.0.1:8000/docs
Swagger UI will open.
You can test APIs directly.
🔌 APIs & Their Work
✅ POST /summarize

Purpose: Generate summary

Work:

Accepts text
Sends prompt to Ollama
Runs Gemma model
Saves summary in database

✅ GET /history

Purpose: View all summaries
Work:
Returns saved summaries
Includes timestamp

✅ DELETE /history/{summary_id}

Purpose: Delete specific summary
Example:
/history/2

✅ DELETE /Delete_all_history

Purpose: Delete complete history
Removes all stored summaries.

🗄️ Database

Database used:
SQLite → summary.db
Automatically created.

Stores:

Original text
Summary text
Created time

🧠 Project Workflow
User Input
   ↓
FastAPI Backend
   ↓
Text Chunking
   ↓
Ollama API
   ↓
Gemma 2B Model
   ↓
Generated Summary
   ↓
SQLite Database
✅ Before Running Project

Make sure:

✔ Ollama installed
✔ Gemma model downloaded
✔ Ollama server running
✔ Dependencies installed
✔ FastAPI server started

👨‍💻 Developer

Developed by Ravi | AI & Backend Developer

⭐ Project Purpose

This project demonstrates:
FastAPI Backend Development
Local LLM Integration
REST API Design
AI Processing Workflow
Database Handling