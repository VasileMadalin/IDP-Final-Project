from pydantic import BaseModel


class TokenPayload(BaseModel):
    token: str
    message: str

class PayloadCommentRequest(BaseModel):
    token: str
    idtweet: int
    comment: str

class UsernamePasswordForm(BaseModel):
    username: str
    password: str
