# ====４スキーマ=====
from pydantic import BaseModel, ConfigDict, Field

class ChatRequest(BaseModel):          # POST /chats で「受け取る」JSON
    question: str = Field(..., examples=["FastAPIとは何ですか？"])


class ChatResponse(BaseModel):         # POST /chats で「返す」JSON
    model_config = ConfigDict(from_attributes=True)

    answer: str


class ChatLogResponse(BaseModel):      # GET /chats で返すリストの「1件分」
    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    answer: str