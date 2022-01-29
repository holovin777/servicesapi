from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return [
        {
            "id": 0,
            "message": "Hello, world!",
        },
        {
            "id": 1,
            "message": "Testing second message.",
        },
    ]
