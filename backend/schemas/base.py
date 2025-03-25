from pydantic import BaseModel
from typing import Optional, List

class CountryRanking(BaseModel):
    country: str
    points: float
    rank: int

class IndicatorData(BaseModel):
    country: str
    indicator: str
    value: Optional[float] = None
    unit: Optional[str] = None

class PillarResponse(BaseModel):
    rankings: List[CountryRanking]
    indicators: List[IndicatorData]

class OverallResponse(BaseModel):
    rankings: List[CountryRanking]
    total_countries: int
    average_score: float 