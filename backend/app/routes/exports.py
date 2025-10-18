from fastapi import APIRouter, Response
import pandas as pd
from ..utils.storage import list_objects
from ..models import ExportItem
from ..utils.common import price_range

router = APIRouter(prefix="/exports", tags=["exports"])

@router.get("/csv")
def export_csv():
    rows = []
    for o in list_objects():
        rows.append({
            "id": o.id,
            "name": o.name,
            "lat": o.lat,
            "lon": o.lon,
            "address": o.address,
            "category": o.category,
            "phone": o.phone,
            "email": o.email,
            "socials": ", ".join(o.socials or []),
            "website": o.website,
            "description_ai": o.description_ai,
            "rooms": o.rooms,
            "price_range": price_range(o.price_min, o.price_max),
            "rating": o.rating,
            "lead_stage": o.lead_stage,
        })
    df = pd.DataFrame(rows)
    csv_bytes = df.to_csv(index=False).encode("utf-8-sig")
    return Response(content=csv_bytes, media_type="text/csv",
                    headers={"Content-Disposition":"attachment; filename=objects_export.csv"})

@router.get("/json")
def export_json():
    return [ExportItem(
        id=o.id, name=o.name, lat=o.lat, lon=o.lon, address=o.address, category=o.category,
        phone=o.phone, email=o.email, socials=", ".join(o.socials or []), website=o.website,
        description_ai=o.description_ai, rooms=o.rooms,
        price_range=price_range(o.price_min,o.price_max), rating=o.rating, lead_stage=o.lead_stage
    ).dict() for o in list_objects()]
