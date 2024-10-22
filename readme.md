README
======

Setup Instructions
------------------

1. **Install Ollama and LLaMA 3.2**
   - First, install Ollama:
     ```
     pip install ollama
     ```
   - Pull the LLaMA 3.2 model using Ollama:
     ```
     ollama pull llama3.2
     ```
   - Run the LLaMA 3.2 model locally:
     ```
     ollama run llama3.2
     ```

2. **Install the Required Dependencies**
   - Install the required dependencies for the FastAPI application:
     ```
     pip install fastapi uvicorn python-dotenv duckduckgo-search swarm openai
     ```

3. **Run the FastAPI Server**
   - Start the FastAPI server using Uvicorn:
     ```
     uvicorn news_api:app --reload
     ```

4. **Make API Requests**
   - Make a POST request to the `/get-news/` endpoint with a JSON body containing the topic. For example:
     ```
     {
         "topic": "AI"
     }
     ```

Example
-------
To get news articles related to AI, you can use the following command:
```bash
curl -X POST "http://127.0.0.1:8000/get-news/" -H "Content-Type: application/json" -d '{"topic": "AI"}'
