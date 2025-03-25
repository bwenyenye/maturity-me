from fastapi import APIRouter, HTTPException
from typing import List
from schemas.base import PillarResponse, CountryRanking, IndicatorData
from utils.data_processor import DataProcessor
import settings

router = APIRouter()
data_processor = DataProcessor()

@router.get("/rankings", response_model=List[CountryRanking])
async def get_data_rankings():
    try:
        df = data_processor.read_excel_file(settings.DATA_PILLAR_RANKINGS_PATH)
        return data_processor.process_rankings(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/indicators", response_model=List[IndicatorData])
async def get_data_indicators():
    try:
        df = data_processor.read_excel_file(settings.DATA_PILLAR_INDICATORS_PATH)
        return data_processor.process_indicators(df)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=PillarResponse)
async def get_data_pillar_data():
    try:
        rankings_df = data_processor.read_excel_file(settings.DATA_PILLAR_RANKINGS_PATH)
        indicators_df = data_processor.read_excel_file(settings.DATA_PILLAR_INDICATORS_PATH)
        
        return PillarResponse(
            rankings=data_processor.process_rankings(rankings_df),
            indicators=data_processor.process_indicators(indicators_df)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
