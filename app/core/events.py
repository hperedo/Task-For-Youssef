from typing import Callable
from fastapi import FastAPI
from contextlib import asynccontextmanager
from cryptography.fernet import Fernet
from app.core.config import settings

# Initialize Fernet with validated key
cipher_suite = Fernet(settings.valid_encryption_key.encode())

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type: str, fn: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(fn)

    def emit(self, event_type: str, data):
        if event_type in self.subscribers:
            for fn in self.subscribers[event_type]:
                fn(data)

event_bus = EventBus()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup events
    yield
    # Cleanup

