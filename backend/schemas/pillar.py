from pydantic import BaseModel
from typing import Dict, List, Optional, Union, Any
from .country import CountryRanking, CountryIndicator, RegionalAverage

class PillarSummary(BaseModel):
    """Schema for pillar summary data"""
    name: str
    weight: float  # Weight of the pillar in the overall score (0-1)
    indicator_count: int
    highest_score: float
    highest_score_country: str
    regional_averages: List[RegionalAverage]
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Digital Skills",
                "weight": 0.4,
                "indicator_count": 7,
                "highest_score": 75.0,
                "highest_score_country": "South Africa",
                "regional_averages": [
                    {"region": "Southern Africa", "average_score": 60.0},
                    {"region": "North Africa", "average_score": 54.67}
                ]
            }
        }

class PillarRankingsResponse(BaseModel):
    """Schema for pillar rankings response"""
    pillar: str
    rankings: List[CountryRanking]
    summary: PillarSummary
    
    class Config:
        schema_extra = {
            "example": {
                "pillar": "Digital Skills",
                "rankings": [
                    {
                        "country": "South Africa",
                        "points": 180,
                        "rank": 1,
                        "score": 75.0,
                        "region": "Southern Africa"
                    },
                    {
                        "country": "Egypt",
                        "points": 172,
                        "rank": 2,
                        "score": 71.67,
                        "region": "North Africa"
                    }
                ],
                "summary": {
                    "name": "Digital Skills",
                    "weight": 0.4,
                    "indicator_count": 7,
                    "highest_score": 75.0,
                    "highest_score_country": "South Africa",
                    "regional_averages": [
                        {"region": "Southern Africa", "average_score": 60.0},
                        {"region": "North Africa", "average_score": 54.67}
                    ]
                }
            }
        }

class IndicatorMetadata(BaseModel):
    """Schema for indicator metadata"""
    id: str
    name: str
    description: Optional[str] = None
    unit: Optional[str] = None  # e.g., "percentage", "score", "count"

class PillarIndicatorsResponse(BaseModel):
    """Schema for pillar indicators response"""
    pillar: str
    indicator: IndicatorMetadata
    countries: List[Dict[str, Any]]
    regional_averages: Dict[str, float]
    
    class Config:
        schema_extra = {
            "example": {
                "pillar": "Digital Skills",
                "indicator": {
                    "id": "adult_literacy_rate",
                    "name": "Adult literacy rate",
                    "description": "Adult literacy rate, population 15+ years, both sexes",
                    "unit": "percentage"
                },
                "countries": [
                    {
                        "country": "Kenya",
                        "value": 81.5,
                        "score": 68.2,
                        "region": "East Africa",
                        "regional_avg": 60.5,
                        "difference": 7.7
                    }
                ],
                "regional_averages": {
                    "East Africa": 60.5,
                    "North Africa": 74.2
                }
            }
        }