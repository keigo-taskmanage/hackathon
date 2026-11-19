from fastapi import APIRouter, Depends
from openai import OpenAI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_db
from api.models import Chat
from api.schemas import ChatLogResponse, ChatRequest, ChatResponse

router = APIRouter()

client = OpenAI()

@router.post("/chats", response_model=ChatResponse)
async def create_chat(
    chat_request: ChatRequest,
    db: AsyncSession = Depends(get_db),
) -> ChatResponse:
    # リクエストから送られてきた質問テキストを取り出す
    user_question = chat_request.question

    # OpenAI API を呼び出す
    ##多分ここを編集して関西弁にする。一度送るメッセージに項目を一つ増やしてみた。
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_question},
            {"role":"system","content": "あなたは関西人です。語尾はやでみたいな感じで"}
        ],
    )

    # APIの回答テキストを取得
    ai_answer = response.choices[0].message.content or ""

    # DBに質問と回答を保存する
    record = Chat(
        question=user_question,
        answer=ai_answer,
    )
    db.add(record)
    await db.commit()
    await db.refresh(record)

    # 定義した ChatResponse の形式で返却
    return ChatResponse(answer=ai_answer)

@router.get("/chats",response_model=list[ChatLogResponse])
async def get_chats(db: AsyncSession = Depends(get_db)) -> list[ChatLogResponse]:
    statement = select(Chat).order_by(Chat.id.desc())   # SQL: SELECT * FROM chats ORDER BY id DESC
    result = await db.execute(statement)                 # DBに問い合わせる
    chats = result.scalars().all()                       # 結果を Chat オブジェクトのリストにする

    return chats   # Chat のリスト → from_attributes で ChatLogResponse のリストに自動変換される

