import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

# Данные сессии
user_session = {
    "session_token": "ALEX",
    "login_time": "2026-09-27T12:30:00",
    "last_active_time": "2026-09-27T12:30:00"  # Время последней активности
}

# Сохранение данных сессии в Redis с использованием hset
user_id = "user2004"
r.hset(f"session:{user_id}", mapping=user_session)

# Устанавливаем TTL для сессии (например, 30 минут)
r.expire(f"session:{user_id}", 30 * 60)

# Получаем данные сессии
session_data = r.hgetall(f"session:{user_id}")
if session_data:
    print("Session Data:", session_data)

# Обновление времени последней активности
r.hset(f"session:{user_id}", "last_active_time", "2026-12-24T15:00:00")

# Проверяем обновленные данные
updated_session_data = r.hgetall(f"session:{user_id}")
print("Updated Session Data:", updated_session_data)
