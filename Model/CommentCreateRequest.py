from pydantic import BaseModel
from uuid import UUID

class CommentCreateRequest(BaseModel):
    user_id: UUID
    content: str
    date : str
    post_id: UUID