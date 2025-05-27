from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from fastapi_app.models import news, users
from fastapi_app.schemas import NewsCreate, UserCreate, News
from fastapi_app.database import database

#def get_user_by_id(db: Session, user_id: str):
#    return db.query(models.User).filter(models.User.id == user_id).first()

async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name)
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}

async def get_users():
    query = users.select()
    return await database.fetch_all(query)

async def create_news(news: NewsCreate):
    try:
        # Создаем новую запись на основе данных
        new_news = News(
            title=news.title,
            content=news.content,
            author=news.author,
            user_id=news.user_id
        )
        # Добавляем в сессию и коммитим
        async with database.session() as session:  # session — это асинхронная сессия
            session.add(new_news)
            await session.commit()  # Фиксируем изменения в базе
            return {"id": new_news.id, **news.dict()}
    except Exception as e:
        # В случае ошибки возвращаем 500
        raise HTTPException(status_code=500, detail=f"Error creating news: {str(e)}")

async def patch_news(news_id, title):
    query = news.update().where(news.c.id == news_id).values(title=title)
    await database.execute(query)
    return {"id": news_id, "title": title}

async def delete_news(news_id):
    query = news.delete().where(news.c.id == news_id)
    await database.execute(query)
    return {"deleted": news_id}