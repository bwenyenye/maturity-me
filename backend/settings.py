import os
from pathlib import Path

# Get absolute path to the backend directory
BASE_DIR = Path(__file__).resolve().parent

# Data directory is relative to the backend directory
DATA_DIR = BASE_DIR / "data"

# File paths - using Path for consistent path handling
OVERALL_RANKINGS_PATH = "AI Maturity Overall Performance.xlsx"
INFRASTRUCTURE_RANKINGS_PATH = "Infrastructure Ranking.xlsx"
INVESTMENTS_RANKINGS_PATH = "Investment Ranking.xlsx"

# If using Excel files, these are the file paths
OVERALL_RANKINGS_PATH: str = OVERALL_RANKINGS_PATH
DIGITAL_SKILLS_RANKINGS_PATH: str = "Digital Skills Ranking.xlsx"
DIGITAL_SKILLS_INDICATORS_PATH: str = "Digital Skills Indicators.xlsx"
INFRASTRUCTURE_INDICATORS_PATH: str = "Infrastructure Indicators.xlsx"
GOVERNANCE_RANKINGS_PATH: str = "Governance Ranking.xlsx"
GOVERNANCE_INDICATORS_PATH: str = "Governance Indicators.xlsx"
DATA_PILLAR_RANKINGS_PATH: str = "Data Ranking.xlsx"
DATA_PILLAR_INDICATORS_PATH: str = "Data Indicators.xlsx"

# Investments pillar
INVESTMENTS_INDICATORS_PATH = "Investment Indicators.xlsx"
