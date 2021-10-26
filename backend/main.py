from fastapi import FastAPI, HTTPException, File, Form, UploadFile
from fastapi.datastructures import UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import File
from pydantic.networks import stricturl
from face_rec import perhitungan_face_recognition

from model import Todo

# app object
app = FastAPI()

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"Ping":"Pooong!"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}")
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404,f"there is no todo item with this title! {title}")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong hehe!")

@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc:str):
    response = await update_todo(title, desc)
    if response:
        if Todo(**response):
            return Todo(**response)
    raise HTTPException(404,f"there is no todo item with this title! {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        if Todo(**response):
            return "Successfully deleted todo item!"
    
    raise HTTPException(404,f"there is no todo item with this title! {title}")

@app.post("/api/recog")
def _file_upload(
        my_file: UploadFile = File(...),
        first: str = Form(...),
        second: str = Form("default value  for second"),
):
    result = perhitungan_face_recognition(my_file.file)
    return {
        "name": my_file.filename,
        "first": first,
        "second": second,
        "result": result
    }