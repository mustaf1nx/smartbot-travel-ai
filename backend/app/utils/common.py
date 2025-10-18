import uuid

def uid() -> str:
    return uuid.uuid4().hex

def price_range(minp: float | None, maxp: float | None) -> str | None:
    if minp is None and maxp is None: return None
    if minp is None: return f"до {int(maxp)}"
    if maxp is None: return f"от {int(minp)}"
    return f"{int(minp)}–{int(maxp)}"
