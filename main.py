from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import uuid
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

N8N_WEBHOOK_URL = "https://iamsajid.app.n8n.cloud/webhook-test/test-webhook"

class ArticleRequest(BaseModel):
    email: str
    article_url: str

@app.post("/process-article")
async def process_article(request: ArticleRequest):
    session_id = str(uuid.uuid4())
    
    payload = {
        "session_id": session_id,
        "email": request.email,
        "article_url": request.article_url
    }
    
    try:
        response = requests.post(N8N_WEBHOOK_URL, json=payload)
        return {
            "message": "Workflow started!",
            "session_id": session_id,
            "n8n_status": response.status_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)