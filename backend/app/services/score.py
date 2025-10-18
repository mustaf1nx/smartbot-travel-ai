from math import sqrt

def completeness(item: dict) -> float:
    keys = ["phone","website","socials","address","infra","price_min","price_max","rooms"]
    have = sum(1 for k in keys if item.get(k))
    return round(have / len(keys), 2)

def activity_score(item: dict) -> float:
    # Если есть соцсети — базовый буст; без интеграции считаем просто
    socs = item.get("socials") or []
    return 0.3 if socs else 0.0

def popularity(item: dict) -> int:
    # Мок: можно добавить счётчик упоминаний
    return 5 if item.get("socials") else 2

def potential(item: dict) -> float:
    # Простейшая эвристика: больше комнат + средняя цена => потенциал заполняемости
    rooms = item.get("rooms") or 0
    prmin = item.get("price_min") or 0
    prmax = item.get("price_max") or prmin
    avgp = (prmin + prmax)/2 if (prmin or prmax) else 0
    if avgp <= 0: return 0.2
    return min(1.0, (rooms/10)*0.4 + (sqrt(avgp/20000))*0.6)

def total_rating(item: dict) -> float:
    c = completeness(item)
    a = activity_score(item)
    p = potential(item)
    pop = min(1.0, (popularity(item)/10))
    # Веса можно подстраивать под критерии
    score = 0.35*c + 0.25*a + 0.25*p + 0.15*pop
    return round(score*10, 2)

def stage(score: float) -> str:
    if score >= 7.5: return "hot"
    if score >= 5.0: return "warm"
    return "cold"
