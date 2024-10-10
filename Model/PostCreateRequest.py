from pydantic import BaseModel
from uuid import UUID
class PostCreateRequest(BaseModel):
    user_id: UUID
    content: str