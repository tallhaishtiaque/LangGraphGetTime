# Time Bot with Gemini
![Screenshot_26-5-2025_175259_smith langchain com](https://github.com/user-attachments/assets/cfb84c00-60cb-4340-b091-5c010441bb88)

Chatbot using Google Gemini that answers time queries.

## Setup

1. Get Google API key:
   - Visit https://makersuite.google.com/app/apikey
   - Create API key if you don't have one
   - Similarly Get LangSmith API key:
     - https://smith.langchain.com/


2. Set environment variables in .env file:
   ```bash
    LANGSMITH_API_KEY='...'
    GOOGLE_API_KEY='...'
   ```
3.  Install & run:
   ```bash
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    langgraph dev
   ```

4.  Ask "What's the current time?" to test
