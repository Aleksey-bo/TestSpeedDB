from typing import Optional
import uuid

from pydantic import BaseModel, Field


class UserScheme(BaseModel):
    id: Optional[int] = None
    name: str
