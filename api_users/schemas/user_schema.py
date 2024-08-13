from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    phone: str
