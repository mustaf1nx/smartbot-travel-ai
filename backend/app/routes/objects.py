from fastapi import APIRouter, Query
from typing import Optional, List
from ..utils.storage import save_object, list_objects, get_object, update_object
from ..services.dgis_client import scan_region
from ..services.enrich import enrich_basic
from ..services.score import total_rating, stage
from ..services.generate import generate_description
from ..models import ObjectIn, ObjectOut

router = APIRouter(prefix="/objects", tags=["objects"])

@router.get("", response_model=List[ObjectOut])
def get_all(category: Optional[str] = None, stage_filter: Optional[str] = None):
    items = list_objects()
    if category:
        items = [i for i in items if i.category == category]
    if stage_filter:
        items = [i for i in items if i.lead_stage == stage_filter]
    return items

@router.post("", response_model=ObjectOut)
async def create(obj: ObjectIn):
    enriched = enrich_basic(obj.dict())
    o = save_object(ObjectIn(**enriched))
    # расчёт рейтинга
    sc = total_rating(o.dict())
    o.rating = sc
    o.lead_stage = stage(sc)
    # генерация описания
    o.description_ai = await generate_description(o.dict())
    update_object(o)
    return o

@router.post("/scan", response_model=List[ObjectOut])
async def scan(region: str = Query(..., description="Напр.: Алматы")):
    raw = await scan_region(region)
    out = []
    for r in raw:
        enr = enrich_basic(r)
        o = save_object(ObjectIn(**enr))
        sc = total_rating(o.dict())
        o.rating = sc
        o.lead_stage = stage(sc)
        o.description_ai = await generate_description(o.dict())
        update_object(o)
        out.append(o)
    return out

@router.get("/{obj_id}", response_model=ObjectOut)
def one(obj_id: str):
    o = get_object(obj_id)
    if not o: 
        return {}
    return o
