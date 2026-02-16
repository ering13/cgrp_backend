# -*- coding: utf-8 -*-

from fastapi import WebSocket
from typing import Dict, List


class ConnectionManager:
    def __init__(self):
        # user_id -> list of sockets
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()

        if user_id not in self.active_connections:
            self.active_connections[user_id] = []

        self.active_connections[user_id].append(websocket)

        print(f"User {user_id} connected")

    def disconnect(self, websocket: WebSocket, user_id: int):
        self.active_connections[user_id].remove(websocket)

        if not self.active_connections[user_id]:
            del self.active_connections[user_id]

        print(f"User {user_id} disconnected")

    async def broadcast(self, user_id: int, message: dict):
        if user_id not in self.active_connections:
            return

        for connection in self.active_connections[user_id]:
            await connection.send_json(message)


manager = ConnectionManager()