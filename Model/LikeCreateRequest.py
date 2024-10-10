from pydantic import BaseModel
from uuid import UUID

class LikeCreateRequest(BaseModel):
    user_id: UUID
    post_id: UUID