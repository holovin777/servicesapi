from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        {
            "id": 2,
            "message": "Testing third message.",
        },
        {
            "id": 3,
            "message": "Testing fourth message.",
        },
    ]

@app.get("/{service_id}")
async def read_service(service_id):
    return {"service_id": service_id}
