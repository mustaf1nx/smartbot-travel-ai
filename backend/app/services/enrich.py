from typing import Dict, Any

def guess_category(name: str) -> str:
    low = (name or "").lower()
    if "глэм" in low or "glamp" in low: return "lux_glamping"
    if "юр" in low or "yurt" in low: return "ethno_yurt"
    if "эко" in low or "eco" in low: return "eco"
    if "гостев" in low or "guest" in low: return "family_guesthouse"
    if "mountain" in low or "горн" in low or "chalet" in low: return "mountain_cabin"
    return "other"

def enrich_basic(item: Dict[str, Any]) -> Dict[str, Any]:
    # Можно подтягивать Instagram/сайт; тут мокаем поля
    item["rooms"] = item.get("rooms") or 6
    item["price_min"] = item.get("price_min") or 20000
    item["price_max"] = item.get("price_max") or 60000
    item["infra"] = item.get("infra") or ["Wi-Fi","Паркинг","Кухня"]
    item["category"] = item.get("category") or guess_category(item.get("name",""))
    return item
