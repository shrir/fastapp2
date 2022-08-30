from fastapi import FastAPI, status, HTTPException
from .models.contact import Contact

app = FastAPI()
directory = {}


@app.post("/contact", status_code=status.HTTP_201_CREATED)
async def create_contact(contact: Contact):
    directory[contact.name] = contact.number
    return {
        contact.name: contact.number
    }


@app.get("/contact/{name}")
async def get_contact(name: str):
    try:
        return {
            name: directory[name]
        }
    except KeyError as key:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{key} not found"
        )


@app.get("/healthz")
async def healthz():
    return {
        "result": {
            "healthy": True
        }
    }
