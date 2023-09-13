from fastapi import FastAPI,Request
import g4f
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    messages: list

@app.post("/v1/chat/completions")
async def root(item:Item):
    print(item.messages)
    messages = item.messages
    response = g4f.ChatCompletion.create(model=g4f.models.gpt_35_turbo, provider=g4f.Provider.Aichat, messages=messages)
    print(response)
    return response

@app.api_route("/{path_name:path}", methods=["GET","POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"], include_in_schema=False)
async def catch_all(request: Request, path_name: str):
    return {"request_method": request.method, "path_name": path_name}

