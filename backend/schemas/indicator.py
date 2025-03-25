from pydantic import BaseModel
from typing import Dict, List, Optional, Union, Any

class Indicator(BaseModel):
    """Schema for indicator data"""
    id: str
    name: str
    description: Optional[str] = None
    pillar: str
    
    class Config:
        schema_extra = {
            "example": {
                "id": "adult_literacy_rate",
                "name": "Adult literacy rate",
                "description": "Adult literacy rate, population 15+ years, both sexes (%)",
                "pillar": "Digital Skills"
            }
        }

class IndicatorList(BaseModel):
    """Schema for list of indicators by pillar"""
    pillar: str
    indicators: List[Indicator]
    
    class Config:
        schema_extra = {
            "example": {
                "pillar": "Digital Skills",
                "indicators": [
                    {
                        "id": "adult_literacy_rate",
                        "name": "Adult literacy rate",
                        "description": "Adult literacy rate, population 15+ years, both sexes (%)",
                        "pillar": "Digital Skills"
                    },
                    {
                        "id": "labor_force_with_advanced_education",
                        "name": "Labor force with advanced education",
                        "description": "Percentage of labor force with advanced education",
                        "pillar": "Digital Skills"
                    }
                ]
            }
        }