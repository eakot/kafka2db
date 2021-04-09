from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class Message(BaseModel):
    id: int
    name = 'Sample event'
    event_ts: Optional[datetime] = None
    tags: List[str] = []
