import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional
import settings

class DataProcessor:
    def __init__(self):
        self.data_dir = Path(settings.DATA_DIR)
        
    def read_excel_file(self, file_path: str) -> pd.DataFrame:
        """Read data from Excel file"""
        try:
            full_path = self.data_dir / file_path
            if not full_path.exists():
                raise FileNotFoundError(f"File not found at: {full_path}")
            
            # Read the Excel file and print column names for debugging
            df = pd.read_excel(full_path)
            print(f"Columns found in {file_path}: {df.columns.tolist()}")
            return df
        except Exception as e:
            raise Exception(f"Error reading Excel file: {str(e)}")
    
    def process_rankings(self, df: pd.DataFrame) -> List[Dict]:
        """Process rankings data from DataFrame"""
        try:
            # Print available columns for debugging
            print(f"Available columns: {df.columns.tolist()}")
            
            # Check for alternative column names
            possible_country_cols = ['Country', 'country', 'Nation', 'nation']
            possible_points_cols = ['Points', 'points', 'Score', 'score']
            possible_rank_cols = ['Rank', 'rank', 'Ranking', 'ranking']
            
            # Find the actual column names
            country_col = next((col for col in possible_country_cols if col in df.columns), None)
            points_col = next((col for col in possible_points_cols if col in df.columns), None)
            rank_col = next((col for col in possible_rank_cols if col in df.columns), None)
            
            if not all([country_col, points_col, rank_col]):
                missing = []
                if not country_col:
                    missing.append(f"Country (tried: {possible_country_cols})")
                if not points_col:
                    missing.append(f"Points (tried: {possible_points_cols})")
                if not rank_col:
                    missing.append(f"Rank (tried: {possible_rank_cols})")
                raise ValueError(f"Missing required columns: {', '.join(missing)}")
            
            rankings = []
            for _, row in df.iterrows():
                rankings.append({
                    "country": str(row[country_col]),
                    "points": float(row[points_col]) if pd.notnull(row[points_col]) else 0.0,
                    "rank": int(row[rank_col]) if pd.notnull(row[rank_col]) else 0
                })
            return rankings
        except Exception as e:
            raise Exception(f"Error processing rankings: {str(e)}")
    
    def process_indicators(self, df: pd.DataFrame) -> List[Dict]:
        """Process indicators data from DataFrame"""
        try:
            indicators = []
            if "Country" not in df.columns:
                raise Exception("Missing required column: Country")
            
            for _, row in df.iterrows():
                country = str(row["Country"])
                for column in df.columns:
                    if column != "Country":
                        value = row[column]
                        # Handle various types of missing or invalid data
                        if pd.isna(value) or value in ['No data', 'Released', 'N/A', '-']:
                            value = None
                        else:
                            try:
                                value = float(value)
                            except (ValueError, TypeError):
                                value = None
                                
                        indicators.append({
                            "country": country,
                            "indicator": column,
                            "value": value
                        })
            return indicators
        except Exception as e:
            raise Exception(f"Error processing indicators: {str(e)}")
    
    def calculate_overall_stats(self, rankings: List[Dict]) -> Dict:
        """Calculate overall statistics"""
        points = [r["points"] for r in rankings]
        return {
            "total_countries": len(rankings),
            "average_score": sum(points) / len(points)
        } 