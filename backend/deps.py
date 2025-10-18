# app/deps.py
# Вспомогательные зависимости для FastAPI (например, доступ к конфигу или базе)

from fastapi import Depends
from .config import settings

def get_settings():
    """
    Возвращает объект с настройками (из config.py)
    """
    return settings
