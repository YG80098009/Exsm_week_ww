from pydantic import BaseModel
from typing import Optional

class Weapon(BaseModel):
    weapon_id: str
    weapon_name: str
    weapon_type: str
    range_km: int
    weight_kg: float
    manufacturer: Optional[str] = "Unknown"
    origin_country: str
    storage_location: str
    year_estimated: int
    risk_level: Optional[str] = None