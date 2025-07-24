from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/hello")
async def get_hello() -> str:
    return "Hello World"


@app.get("/welcome/{name}", status_code=200)
async def get_welcome(name: str) -> str:
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")
    return f"Welcome {name}!"




