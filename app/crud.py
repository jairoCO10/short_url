from sqlalchemy.orm import Session
from app.models import URL
import string, random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def create_short_url(db: Session, original_url: str):
    short_url = generate_short_url()
    db_url = URL(short_url=short_url, original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return short_url

def get_original_url(db: Session, short_url: str):
    return db.query(URL).filter(URL.short_url == short_url).first()


def getall(db:Session):
    responses =  db.query(URL).all()
    urlresponse = []
    for response in responses:
        data ={
                "shortURL":response.short_url,
                "originURL":response.original_url
                }
        urlresponse.append(data)
    return urlresponse

