from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "API health check successful",
        "success": True,
        "status_code": None
        }
