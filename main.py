from fastapi import FastAPI, HTTPException
from dataclasses import dataclass

app = FastAPI()

@app.get("/hello")
async def get_hello() -> str:
    return "Hello World"


@app.get("/welcome/{name}", status_code=200)
async def get_welcome(name: str) -> str:
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")
    return f"Welcome {name}!"


"""
 Créer une route POST /students, qui prend dans le corps de la requête une liste d’objet
JSON qui a les attributs suivants :
- Reference, de type chaîne de caractères
- FirstName, de type chaîne de caractères
- LastName, de type chaîne de caractères
- Age, de type nombre entier

"""

@dataclass
class Students:
    References: str
    First_name: str
    Last_name: str
    age: int


@app.post("/students")
async def create_student(student: Students) -> Students:
    return student
