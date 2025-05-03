from fastapi import FastAPI
from sqlmodel import SQLModel
from models import Score
import database
import uvicorn


app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})


@app.on_event("startup")
def on_startup():
    database.create_db()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/highscores")
def get_highscores():
    return database.get_all_scores()

@app.post("/score")
def post_highscore(score: Score):
    database.add_score(score)
    return score

if __name__ == "__main__":
    uvicorn.run(app)