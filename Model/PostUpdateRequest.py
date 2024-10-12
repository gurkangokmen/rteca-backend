from pydantic import BaseModel
from uuid import UUID

class PostUpdateRequest(BaseModel):
    post_id: UUID
    content: str
    date : str