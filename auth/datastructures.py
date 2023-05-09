from pydantic import BaseModel

class UsernamePasswordForm(BaseModel):
    username: str
    password: str
