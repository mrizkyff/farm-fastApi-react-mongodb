from abc import abstractproperty
from model import Todo

# mongoDB driver hehe
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.todo

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    if document != None:
        return Todo(**document)
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    # await collection.update_one({"title":title},{"$set":{
    #     "description":desc
    # }})
    # document = await collection.find_one({"title":"title"})
    result = await collection.find_one_and_update({"title":title},{"$set":{
        "description": desc
    }})
    return result

async def remove_todo(title):
    # result = await collection.delete_one({"title": title})
    result = await collection.find_one_and_delete({"title":title})
    return result