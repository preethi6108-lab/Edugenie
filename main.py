from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_path

app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    return FileResponse("templates/index.html")

@app.get("/qna")
def qna(question: str):
    return {"answer": answer_question(question)}

@app.get("/explain")
def explain(topic: str):
    return {"explanation": explain_concept(topic)}

@app.get("/quiz")
def quiz(topic: str):
    return generate_quiz(topic)

@app.get("/summarize")
def summarize(text: str):
    return {"summary": summarize_text(text)}

@app.get("/learning-path")
def learning_path(topic: str):
    return get_learning_path(topic)
