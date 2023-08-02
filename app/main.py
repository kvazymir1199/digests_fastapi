from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session

from crud import return_digest
from schemas import DigestBase
import models


def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/users/{user_id}/digest")
async def get_digest(
        user_id: int,
        rating: int = Query(gt=0, lt=11, default=0),
        db: Session = Depends(get_db)

) -> DigestBase:
    result = return_digest(
        user_id=user_id,
        rating=rating,
        db=db
    )

    return result
