from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from news_workflow import run_news_workflow

# FastAPI instance
app = FastAPI()

# Pydantic model for request body
class NewsRequest(BaseModel):
    topic: str
    max_results: Optional[int] = 5

# FastAPI route to get news articles
@app.post("/get-news/")
def get_news(request: NewsRequest):
    try:
        result = run_news_workflow(request.topic)
        return {"edited_news": result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


# Example of usage:
# Run the FastAPI server and make a POST request to /get-news/ with JSON body: {"topic": "AI"}
