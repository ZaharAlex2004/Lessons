import redis
import json
from flask import Flask, jsonify
from redis.exceptions import RedisError, ConnectionError, TimeoutError

app = Flask(__name__)


def serialize_data(data):
    """
    Сериализация данных в формат JSON
    :param data:
    :return:
    """
    try:
        return json.dumps(data)
    except (TypeError, ValueError) as e:
        print(f"Ошибка сериализации данных: {e}")
        raise


def deserialize_data(data):
    """
    Десериализация данных из формата JSON
    :param data:
    :return:
    """
    try:
        return json.loads(data) if data else {}
    except (TypeError, ValueError) as e:
        print(f"Ошибка десериализации данных: {e}")
        raise


pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# Пример сложных данных сессии
user_session = {
    "session_token": "ALEX",
    "login_time": "2026-09-27T12:30:00",
    "last_active_time": "2026-09-27T12:30:00"
}

user_id = "user2004"


@app.route('/')
def index():
    try:
        pipe = r.pipeline()

        if r.exists(f"session:{user_id}") and r.type(f"session:{user_id}") != "hash":
            r.delete(f"session:{user_id}")

        pipe.hset(f"session:{user_id}", mapping=user_session)
        pipe.expire(f"session:{user_id}", 30 * 60)
        pipe.execute()

        session_data = r.hgetall(f"session:{user_id}")
        if session_data:
            session_data = {key.decode(): value.decode() for key, value in session_data.items()}

        pipe = r.pipeline()
        pipe.hset(f"session:{user_id}", "last_active_time", "2026-12-24T15:00:00")
        pipe.execute()

        updated_session_data = r.hgetall(f"session:{user_id}")
        updated_session_data = {key.decode(): value.decode() for key, value in updated_session_data.items()}

        return jsonify({
            "Session Data": session_data,
            "Updated Session Data": updated_session_data
        })

    except redis.exceptions.ConnectionError:
        return "Ошибка подключения к Redis.", 500
    except redis.exceptions.TimeoutError:
        return "Тайм-аут при подключении к Redis.", 500
    except RedisError as e:
        return f"Ошибка Redis: {e}", 500
    except Exception as e:
        return f"Общая ошибка: {e}", 500


if __name__ == '__main__':
    app.run(debug=True)
