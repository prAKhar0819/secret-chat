import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = self.scope["user"].username if self.scope["user"].is_authenticated else "Guest"
        self.room_group_name = "chat_admin"  # Use a single group for all users

        # Join the chat group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = self.username  # Use logged-in user's username

        print(f"\n[{username}] {message}")  # Log messages to terminal

        # Broadcast message to all users (including admin)
        await self.channel_layer.group_send(
            "chat_admin",
            {
                "type": "chat_message",
                "message": message,
                "username": username
            }
        )

    async def chat_message(self, event):
        """Send messages back to the user UI."""
        await self.send(text_data=json.dumps({
            "username": event["username"],
            "message": event["message"]
        }))

