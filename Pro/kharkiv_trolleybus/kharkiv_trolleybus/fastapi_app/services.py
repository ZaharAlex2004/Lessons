import httpx

DJANGO_SERVICE_URL = "http://django-service/api/endpoint/"

async def send_data_to_django():
    async with httpx.AsyncClient() as client:
        response = await client.get(DJANGO_SERVICE_URL)
        return response.json()
