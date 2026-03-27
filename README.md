🚀 DevMind AI — AI Developer Assistant
🧠 Overview

DevMind AI is a full-stack AI-powered developer assistant inspired by tools like GitHub Copilot and ChatGPT. It enables users to generate code from natural language prompts, improve prompt quality using prompt engineering principles, and interact with an AI model through a simple and intuitive interface.

The system is designed to demonstrate real-world concepts such as AI integration, backend API development, prompt optimization, and secure application design.

🎯 Key Features
🧠 AI Code Generation
Generate code from natural language prompts using LLMs
✨ Prompt Optimization Engine
Improves user prompts using:
Single task focus
Specific instructions
Concise format
💬 Interactive Chat System
Maintains conversation context for better responses
🛡️ Safety Filtering
Detects and blocks unsafe or malicious prompts
📜 Context-Aware Responses
Uses previous interactions to improve output quality
⚡ Fast Backend API
Built with FastAPI for high performance
🧠 How It Works
User Input
   ↓
Prompt Engine (improves prompt)
   ↓
Safety Filter (checks validity)
   ↓
Context Manager (adds history)
   ↓
LLM API (Groq)
   ↓
Response Generated
   ↓
Frontend Display (Streamlit)
🧱 Tech Stack
🔹 Backend — FastAPI
High-performance API framework
Asynchronous support
Lightweight and scalable
🔹 Frontend — Streamlit
Rapid UI development
Minimal frontend complexity
Ideal for AI-based applications
🔹 AI Integration — Groq API (LLMs)
Fast inference
Free access tier
Supports modern LLMs
🔹 Language — Python
Strong ecosystem for AI & backend
Easy API integration
Clean and readable


⚙️ Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/sushanth1551/CodeMantra.git
cd CodeMantra
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key_here
▶️ Running the Project
🔹 Start Backend
python -m uvicorn backend.main:app --reload
🔹 Start Frontend (new terminal)
streamlit run frontend/app.py
🌐 Access App
http://localhost:8501
🧪 Example Usage
Input:
create login page in html
Output:
Improved prompt
Generated HTML code
🧠 Concepts Used
Prompt Engineering
Zero-shot prompting
API Integration
Backend Architecture
AI-assisted development
Context-aware systems
💡 Use Cases
Developers generating boilerplate code
Learning prompt engineering
Building AI-powered tools
Rapid prototyping
🚀 Future Improvements
📁 File upload (context-aware coding)
💬 Advanced chat UI (ChatGPT-style)
🧠 RAG (Retrieval-Augmented Generation)
🌐 Deployment (cloud hosting)
🔐 Advanced security filters
🔐 Security Note
API keys are stored in .env
.env is excluded using .gitignore
No sensitive data is exposed in repository
📌 Project Highlights
Combines AI + backend + prompt engineering
Simulates real tools like Copilot
Demonstrates production-level concepts
Built with scalable architecture
👨‍💻 Author

Sushanth Duggeni

GitHub: https://github.com/sushanth1551
⭐ Acknowledgment

Inspired by:

GitHub Copilot
ChatGPT
Modern AI developer tools
🔥 FINAL TIP

After adding this README:

👉 Add:

screenshots of your app
short demo video (optional)
🚀 NEXT STEP

If you want to go even stronger:

👉 say “upgrade to advanced version”

I’ll help you add:

File upload (Copilot-level)
Chat UI like ChatGPT
Context-aware AI (RAG)

That will make your project 🔥 top 1% level
