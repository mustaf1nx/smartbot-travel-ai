import httpx
from ..config import settings

BASE = "https://catalog.api.2gis.com/3.0/items"
# Документация: https://docs-new.2gis.com/ru/api/search
# Мы используем поиск по ключевым словам и региону.

CATEGORIES = [
    "глэмпинг", "юрты", "гостевой дом", "эко дом", "eco lodge", "mountain cabin"
]

async def search_places(query: str, region: str, page: int = 1, page_size: int = 20):
    params = {
        "q": query,
        "region": region,
        "page": page,
        "page_size": page_size,
        "key": settings.DGIS_API_KEY
    }
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.get(f"{BASE}", params=params)
        r.raise_for_status()
        return r.json()

async def scan_region(region: str):
    found = []
    for term in CATEGORIES:
        data = await search_places(term, region)
        for item in data.get("result", {}).get("items", []):
            # Вынимаем минимум полей (как есть; поля зависят от 2GIS конкретно)
            name = item.get("name")
            geo = item.get("point", {})
            address = item.get("address_name")
            contacts = item.get("contacts", [])
            phones = [c.get("value") for c in contacts if c.get("type") == "phone"]
            sites  = [c.get("value") for c in contacts if c.get("type") == "website"]
            socs   = [c.get("value") for c in contacts if c.get("type") == "instagram" or c.get("type") == "vk"]
            found.append({
                "name": name,
                "lat": geo.get("lat"),
                "lon": geo.get("lon"),
                "address": address,
                "phone": phones[0] if phones else None,
                "website": sites[0] if sites else None,
                "socials": socs
            })
    return found
