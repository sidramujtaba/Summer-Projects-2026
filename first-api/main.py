from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to my API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }