from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.database import db
from pydantic import BaseModel
from app.cors import add_middleware
from bson.objectid import ObjectId

app = FastAPI()

add_middleware(app)

def stringifyEntity(entity):
    output = {}
    for key in entity:
        if key == '_id':
            output[key] = str(entity[key])
        else:
            output[key] = entity[key]
    return output

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head>
                <title>Key-value api</title>
            </head>
            <body>
                <p>go to <a href="/entries">/entries</a>
            </body>
        </html>
        """

@app.get("/entries")
async def entries():
    # TODO: perhaps hide this route
    entries = db.entries.find({})
    result = [stringifyEntity(entry) for entry in entries]
    return result

@app.get("/entries/{id}")
async def entryById(id):
    entry = db.entries.find_one({ '_id': ObjectId(id) })
    if entry:
        return stringifyEntity(entry)
    return None


class Entry(BaseModel):
    value: str

@app.post("/entries")
async def postEntry(entry: Entry):
    result = db.entries.insert_one({ 'value': entry.value })
    return str(result.inserted_id)
