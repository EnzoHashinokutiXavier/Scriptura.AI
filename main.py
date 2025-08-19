import os

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")
client = OpenAI(api_key=api_key)

class ExcerptRequest(BaseModel):
    excerpt: str

@app.post("/simple-explanation")
async def simple_explanation(req: ExcerptRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a very studious theologian with a deep knowledge of the Bible. You explain biblical passages in a simple and straightforward way so that laypeople and children can understand what is being said."},
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        raise HTTPException(status_code=500, detail=str(fail))

@app.post("/literal-explanation")
async def literal_explanation(req: ExcerptRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a theologian with extensive knowledge of the Bible and mastery of the Aramaic, Hebrew, and Greek languages. You explain passages of the Bible, explaining their possible translations based on the original ancient scriptures."},
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        raise HTTPException(status_code=500, detail=str(fail))

@app.post("/interpretation-explanation")
async def interpretation_explanation(req: ExcerptRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a theologian with extensive knowledge of the Bible and knowledge of the various Christian religions. You explain passages from the Bible, explaining the possible interpretations in each Christian church."},
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        raise HTTPException(status_code=500, detail=str(fail))

# Servindo arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")
