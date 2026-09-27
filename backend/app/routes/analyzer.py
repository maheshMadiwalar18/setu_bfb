from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(tags=["Analyzer"])

class ExtractRequest(BaseModel):
    url: str

class CompareRequest(BaseModel):
    urls: List[str]

@router.post("/analyzer/extract")
async def extract_features(req: ExtractRequest):
    return {
        "overview": {
            "title": f"Extracted Data from {req.url}",
            "description": "Mocked AI extraction"
        },
        "features": [
            "Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"
        ],
        "pricing_information": "Pricing info mock",
        "services": ["Service A", "Service B"],
        "integrations": ["Integration 1", "Integration 2"],
        "faqs": [{"q": "Question 1", "a": "Answer 1"}],
        "security_features": ["Security 1"],
        "ai_features": ["AI Feature 1"]
    }

@router.post("/analyzer/compare")
async def compare_sites(req: CompareRequest):
    return {
        "compared_sites": req.urls,
        "comparison_matrix": {
            "feature_overlap": True,
            "details": "Mock comparison details"
        }
    }
