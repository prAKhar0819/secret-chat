import asyncio
import websockets
import json
from rich.console import Console
from rich.prompt import Prompt

console = Console()

async def admin_chat():
    uri = "ws://localhost:8001/ws/chat/"
    async with websockets.connect(uri) as websocket:
        console.print("[bold green]Admin connected to chat![/bold green]")

        async def receive_messages():
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                console.print(f"[bold cyan]{data['username']}:[/bold cyan] {data['message']}")

        asyncio.create_task(receive_messages())

        while True:
            message = Prompt.ask("[bold magenta]Admin[/bold magenta]")
            await websocket.send(json.dumps({"username": "Admin", "message": message}))

asyncio.run(admin_chat())

