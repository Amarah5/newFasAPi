from fastapi import FastAPI, HTTPException
from dataclasses import dataclass
from pydantic import BaseModel


app = FastAPI()

@dataclass
class Students(BaseModel):
    References: str
    First_name: str
    Last_name: str
    age: int


@app.get("/hello")
async def get_hello() -> str:
    return "Hello World"


@app.get("/welcome/{name}", status_code=200)
async def get_welcome(name: str) -> str:
    if not name:
        raise HTTPException(status_code=400, detail="Name parameter is required")
    return f"Welcome {name}!"

list_student = [{}]

@app.post("/students/")
async def create_student(student: Students) -> Students:
    list_student.append(student) # type: ignore
    return student


@app.get("/students", status_code=200)
async def get_liste_student() -> list[Students]:
    return [Students(**b) for b in list_student]



@app.put("/students/{references}", status_code=200)
async def update_student(refereces: str):
    if Students.References == refereces:
        for student in list_student:
            if student.References == refereces: # type: ignore
                return student
            else:
                list_student.append(student)



