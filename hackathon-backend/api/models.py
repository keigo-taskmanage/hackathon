#=== 3DBモデルの作成 ======
from sqlalchemy import Column, Integer, String

from api.database import Base


class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(1024))
    answer = Column(String(1024))
