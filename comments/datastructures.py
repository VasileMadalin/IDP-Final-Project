from pydantic import BaseModel


class PayloadCommentRequest(BaseModel):
    token: str
    idtweet: int
    comment: str
