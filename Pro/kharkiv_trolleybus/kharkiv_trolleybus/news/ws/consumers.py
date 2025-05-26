import json
from channels.generic.websocket import AsyncWebsocketConsumer

active_connections = {}


class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        if text_data:
            try:
                text_data_json = json.loads(text_data)
                message = text_data_json.get('message', '')

                if message:
                    await self.send(text_data=json.dumps({
                        'message': message
                    }))
            except json.JSONDecodeError:
                await self.send(text_data=json.dumps({
                    'error': 'Invalid JSON format received'
                }))
        else:
            await self.send(text_data=json.dumps({
                'error': 'Received empty message'
            }))