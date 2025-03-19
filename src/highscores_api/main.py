from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/highscores")
def get_highscores():
    return {"player": "Will", "score": 1000}

@app.post("/score")
def post_highscore():
    return "success"
if __name__ == "__main__":
    uvicorn.run(app)