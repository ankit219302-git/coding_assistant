# 🧠 Saitama Coding Assistant (Python CLI)

A minimal Python CLI tool that uses the OpenAI API to generate and debug software engineering code — with the calm, slightly bored personality of Saitama from *One Punch Man*.

The assistant:
- ✅ Generates optimized and factually correct code
- ✅ Helps debug software engineering problems
- ✅ Politely declines non–computer-science questions
- ✅ Responds with Saitama-style personality

---

# 📦 Project Structure

This project contains only **one Python file**:

```
├── app  
│   └── assistant.py  
├── .env   
├── requirements.txt  
└── README.md  
```

---

# 🛠 Requirements

- Python 3.9+
- openai
- python-dotenv

---

# 🚀 Setup Instructions

## 1️⃣ Clone the Repository

```
git clone <your-repository-url>
cd <your-project-folder>
```

## 2️⃣ Create a Virtual Environment (Recommended)

```
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

## 3️⃣ Install Dependencies

Create a `requirements.txt` file:

```
openai
python-dotenv
```

Then run:

```
pip install -r requirements.txt
```

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

⚠️ Never commit your `.env` file with actual OpenAI API key.

Add this to `.gitignore`:

```
.env
.venv/
__pycache__/
```

---

# ▶️ Running the Application

```
python assistant.py
```

You will see:

```
Please enter your coding question:
```

Type your software engineering question and press Enter.

---

# 🧠 How It Works

The script:

1. Loads the API key using `python-dotenv`
2. Defines a system prompt that:
   - Restricts responses to software engineering
   - Ensures factual correctness
   - Adds Saitama personality
3. Accepts user input via CLI
4. Sends system + user messages to OpenAI
5. Prints the response

---

# 💻 Example

Input:
```
How do I implement a thread-safe singleton in Java?
```

Output:
A correct implementation with explanation — delivered calmly, like someone who defeats bugs in one punch.

---

# 🔒 Environment Variables

| Variable         | Description          |
|------------------|----------------------|
| OPENAI_API_KEY   | Your OpenAI API key  |

---
