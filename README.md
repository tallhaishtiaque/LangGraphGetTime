# Time Bot with Gemini

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
