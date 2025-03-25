from pydantic import BaseModel
from typing import Dict, List, Optional, Union, Any

class CountryRanking(BaseModel):
    """Schema for country ranking data"""
    country: str
    points: float
    rank: int
    score: float
    region: str
    
    class Config:
        schema_extra = {
            "example": {
                "country": "South Africa",
                "points": 232,
                "rank": 1,
                "score": 60.0,
                "region": "Southern Africa"
            }
        }

class CountryIndicator(BaseModel):
    """Schema for country indicator data"""
    country: str
    indicators: Dict[str, Any]
    
    class Config:
        schema_extra = {
            "example": {
                "country": "Kenya",
                "indicators": {
                    "adult_literacy_rate": 81.5,
                    "labor_force_with_advanced_education": 69.1,
                    "ict_skills_in_education_system": 67.54
                }
            }
        }

class RegionalAverage(BaseModel):
    """Schema for regional average data"""
    region: str
    average_score: float
    
    class Config:
        schema_extra = {
            "example": {
                "region": "Southern Africa",
                "average_score": 58.42
            }
        }