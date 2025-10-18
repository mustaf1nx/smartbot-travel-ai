from typing import Dict
from .common import uid
from ..models import ObjectIn, ObjectOut

DB: Dict[str, ObjectOut] = {}

def save_object(obj_in: ObjectIn) -> ObjectOut:
    obj_id = uid()
    obj = ObjectOut(id=obj_id, **obj_in.dict())
    DB[obj_id] = obj
    return obj

def update_object(obj: ObjectOut):
    DB[obj.id] = obj

def list_objects():
    return list(DB.values())

def get_object(obj_id: str) -> ObjectOut | None:
    return DB.get(obj_id)

def bulk_upsert(items: list[ObjectOut]):
    for it in items:
        DB[it.id] = it
