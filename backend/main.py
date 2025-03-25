# pip install pandas fastapi uvicorn numpy python-dotenv openpyxl
# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import digital_skills, infrastructure, governance, investments, data, overall_performance
import settings



# Create FastAPI app
app = FastAPI(
    title="Africa AI Readiness Index API",
    description="API for the Africa AI Readiness Index Dashboard",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(overall_performance.router, prefix="/api/overall", tags=["Overall Performance"])
app.include_router(digital_skills.router, prefix="/api/digital-skills", tags=["Digital Skills"])
app.include_router(infrastructure.router, prefix="/api/infrastructure", tags=["Infrastructure"])
app.include_router(governance.router, prefix="/api/governance", tags=["Governance"])
app.include_router(investments.router, prefix="/api/investments", tags=["Investments"])
app.include_router(data.router, prefix="/api/data", tags=["Data"])

@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to the Africa AI Readiness Index API"
   
    }