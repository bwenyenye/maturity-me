from fastapi import APIRouter, HTTPException
from typing import List
from schemas.base import OverallResponse, CountryRanking
from utils.data_processor import DataProcessor
import settings

router = APIRouter()
data_processor = DataProcessor()

@router.get("/", response_model=OverallResponse)
async def get_overall_performance():
    try:
        df = data_processor.read_excel_file(settings.OVERALL_RANKINGS_PATH)
        rankings = data_processor.process_rankings(df)
        stats = data_processor.calculate_overall_stats(rankings)
        
        return OverallResponse(
            rankings=rankings,
            total_countries=stats["total_countries"],
            average_score=stats["average_score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 