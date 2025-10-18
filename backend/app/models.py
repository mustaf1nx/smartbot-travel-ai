from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

Category = Literal["lux_glamping","family_guesthouse","eco","ethno_yurt","mountain_cabin","other"]
LeadStage = Literal["hot","warm","cold"]

class ObjectIn(BaseModel):
    name: str
    lat: float
    lon: float
    address: Optional[str] = None
    category: Optional[Category] = "other"
    phone: Optional[str] = None
    email: Optional[str] = None
    socials: List[str] = []
    website: Optional[str] = None
    description_raw: Optional[str] = None
    photos: List[str] = []
    rooms: Optional[int] = None
    price_min: Optional[float] = None
    price_max: Optional[float] = None
    infra: List[str] = []

class ObjectOut(ObjectIn):
    id: str
    city: Optional[str] = None
    region: Optional[str] = None
    rating: float = 0.0
    lead_stage: LeadStage = "cold"
    description_ai: Optional[str] = None
    popularity: Optional[int] = None
    completeness: Optional[float] = None
    activity_score: Optional[float] = None
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    status: Literal["new","verified","in_progress"] = "new"

class ExportItem(BaseModel):
    id: str
    name: str
    lat: float
    lon: float
    address: str | None
    category: str
    phone: str | None
    email: str | None
    socials: str
    website: str | None
    description_ai: str | None
    rooms: int | None
    price_range: str | None
    rating: float
    lead_stage: str
