# Library to interact with the system
import os

# Uses FastAPI to create the application and define routes, HTTPException returns HTTP erros
from fastapi import FastAPI, HTTPException
# Serve static files in the application
from fastapi.staticfiles import StaticFiles
# Returns HTML file to browser
from fastapi.responses import FileResponse
# Creates classes that represent and validate data
from pydantic import BaseModel
# ChatGPT library
from openai import OpenAI

# Starts the FastAPI aplication
app = FastAPI()

# Search for the key in the environment
api_key = os.getenv("OPENAI_API_KEY")
# Protects against missing key
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")
# Creates the authenticated client to use the API
client = OpenAI(api_key=api_key)

# A class that represents the body of a request
class ExcerptRequest(BaseModel):
    # Defines that the request must have a field called excerpt of type string
    excerpt: str

# Define a POST endpoint at /simple-explanation
@app.post("/simple-explanation")
async def simple_explanation(req: ExcerptRequest):
    try:
        # Call the OpenAI API to generate a chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # The model to be used
            messages=[
                # The system role sets the assistant's behavior and expertise
                {"role": "system", "content": "You are a very studious theologian with a deep knowledge of the Bible. You explain biblical passages in a simple and straightforward way so that laypeople and children can understand what is being said."},
                
                # The user provides the Bible excerpt to be explained
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        # Return the assistant's explanation as JSON
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        # If something goes wrong, return an HTTP 500 error with the details
        raise HTTPException(status_code=500, detail=str(fail))

# Define a POST endpoint at /literal-explanation
@app.post("/literal-explanation")
async def literal_explanation(req: ExcerptRequest):
    try:
        # Call the OpenAI API to generate a chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Model used for the response
            messages=[
                # The system role defines the assistant as a theologian
                # with expertise in Biblical languages (Aramaic, Hebrew, Greek)
                # and instructs it to provide explanations based on literal translations.
                {"role": "system", "content": "You are a theologian with extensive knowledge of the Bible and mastery of the Aramaic, Hebrew, and Greek languages. You explain passages of the Bible, explaining their possible translations based on the original ancient scriptures."},
                
                # The user provides the excerpt of the Bible to be explained
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        # Return the AI's explanation as a JSON response
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        # If any error occurs, raise an HTTP 500 with the error details
        raise HTTPException(status_code=500, detail=str(fail))


# Define a POST endpoint at /interpretation-explanation
@app.post("/interpretation-explanation")
async def interpretation_explanation(req: ExcerptRequest):
    try:
        # Call the OpenAI API to generate a chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Model used for generating the explanation
            messages=[
                # The system role sets the assistant's persona as a theologian
                # knowledgeable about the Bible and the doctrines of various
                # Christian denominations. The goal is to provide explanations
                # that cover different interpretations across Christian churches.
                {"role": "system", "content": "You are a theologian with extensive knowledge of the Bible and knowledge of the various Christian religions. You explain passages from the Bible, explaining the possible interpretations in each Christian church."},
                
                # The user provides the Bible excerpt to be explained
                {"role": "user", "content": f"Explain the excerpt: {req.excerpt}"}
            ]
        )
        # Return the explanation as a JSON response
        return {"explanation": response.choices[0].message.content}
    except Exception as fail:
        # If an error occurs, return an HTTP 500 with the error details
        raise HTTPException(status_code=500, detail=str(fail))


# Mount the 'static' directory to serve static files (CSS, HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a GET endpoint at the root URL "/"
@app.get("/")
async def root():
    # Return the 'index.html' file located in the 'static' folder
    return FileResponse("static/index.html")
