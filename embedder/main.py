import os
from typing import List, Union
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from fastembed.embedding import FlagEmbedding as Embedding
import numpy as np
import uvicorn


class Prompt(BaseModel):
    prompt: str = Field(default="what time is it?")
    
class Document(BaseModel):
    document: List[str] = Field(default=["what time is it?","get the time","i want to debug"])

class Config(BaseModel):
    model: str = Field(default="BAAI/bge-small-en")
    max_length: int = Field(default=512)
    threads: int = Field(default=0)
    
cache_dir = os.getenv("CACHE_DIR", "./cache")

app = FastAPI()

@app.post("/embeddings/prompt")
def submit_prompt(body_json: Prompt):
    """Submit the prompt to the embedder."""
    if not hasattr(app.state, "embedding_model"):
        raise HTTPException(status_code=500, detail="Embedding model not loaded yet.")
    prompt_before = body_json.prompt
    embeddings: List[np.ndarray] = list(app.state.embedding_model.passage_embed(prompt_before)) # notice that we are casting the generator to a list 
    embeddings = [embedding.tolist() for embedding in embeddings]
    return embeddings[0]

@app.post("/embeddings/document")
def submit_document(body_json: Document):
    """Submit the prompt to the embedder."""
    if not hasattr(app.state, "embedding_model"):
        raise HTTPException(status_code=500, detail="Embedding model not loaded yet.")
    prompt_before = body_json.document
    embeddings: List[np.ndarray] = list(app.state.embedding_model.passage_embed(prompt_before)) # notice that we are casting the generator to a list 
    embeddings = [embedding.tolist() for embedding in embeddings]
    return embeddings

@app.post("/embeddings")
def setup(config: Config):
    try:
        # Sometimes the cache dir is not created, so we create it here
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        embedding_model = Embedding(model_name=config.model,max_length=config.max_length, cache_dir=cache_dir, threads=config.threads)
        app.state.embedding_model = embedding_model
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
if __name__ == "__main__":
    uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True
        )