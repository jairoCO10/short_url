
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app import models, crud
from app.Settings.database import  Connection, Connect
import uvicorn
app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


class URL(BaseModel):
    original_url: str


@app.post("/shorten")
def create_short_url(url: URL, db: Session = Depends(Connect.get_db)):
    short_url = crud.create_short_url(db, url.original_url)
    return {"short_url": f"http://localhost:8000/{short_url}"}

@app.get("/{short_url}")
def redirect_url(short_url: str, db: Session = Depends(Connect.get_db)):
    db_url = crud.get_original_url(db, short_url)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url)


@app.get("/")
def get_all(db:Session = Depends(Connect.get_db)):
    db_url = crud.getall(db)
    return db_url

