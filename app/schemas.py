from pydantic import BaseModel


class PostBase(BaseModel):
    content: str


class DigestBase(BaseModel):
    posts: list[PostBase]
