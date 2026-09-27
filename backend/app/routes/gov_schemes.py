"""
SETU — Government Schemes Scraper API Routes
=============================================
Provides endpoints to:
  - Search government schemes (with live scraping fallback)
  - Get the official government portal directory
  - Fetch scheme detail via URL scraping
  - Get live news/updates from government sources
  - Get scheme categories from myscheme.gov.in
"""

from typing import Optional
from fastapi import APIRouter, Query, HTTPException
from app.scraper.gov_scraper import (
    scrape_myscheme_search,
    scrape_myscheme_categories,
    scrape_scheme_detail,
    get_gov_portal_directory,
    scrape_live_updates,
    _get_curated_gov_schemes,
)

router = APIRouter(prefix="/gov-schemes", tags=["gov-schemes"])


@router.get("/search")
def search_gov_schemes(
    q: Optional[str] = Query("", description="Search query"),
    category: Optional[str] = Query("", description="Category filter"),
    state: Optional[str] = Query("", description="State filter"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=50),
):
    """
    Search government schemes — first attempts live scraping from
    myscheme.gov.in, falls back to curated verified data.
    """
    result = scrape_myscheme_search(
        query=q or "",
        category=category or "",
        state=state or "",
        page=page,
        limit=limit,
    )
    return result


@router.get("/portals")
def get_portal_directory():
    """
    Returns the verified directory of official government portals
    with apply links, categories, and features.
    """
    portals = get_gov_portal_directory()
    return {
        "total": len(portals),
        "portals": portals,
    }


@router.get("/categories")
def get_scheme_categories():
    """
    Returns scheme categories from myscheme.gov.in.
    """
    categories = scrape_myscheme_categories()
    return {
        "total": len(categories),
        "categories": categories,
    }


@router.get("/updates")
def get_live_updates():
    """
    Returns latest government scheme news and updates
    scraped from official sources.
    """
    updates = scrape_live_updates()
    return {
        "total": len(updates),
        "updates": updates,
    }


@router.get("/detail")
def get_scheme_detail(url: str = Query(..., description="Official scheme URL to scrape")):
    """
    Scrape detailed information from a specific government scheme page.
    """
    if not url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL — must start with http(s)")
    
    detail = scrape_scheme_detail(url)
    if not detail:
        raise HTTPException(status_code=502, detail="Could not fetch data from the provided URL")
    
    return detail


@router.get("/curated")
def get_curated_schemes(
    q: Optional[str] = Query("", description="Search query"),
    category: Optional[str] = Query("", description="Category filter"),
    state: Optional[str] = Query("", description="State filter"),
):
    """
    Returns curated, verified government scheme data
    (always available, no scraping required).
    """
    schemes = _get_curated_gov_schemes(
        query=q or "",
        category=category or "",
        state=state or "",
    )
    return {
        "total": len(schemes),
        "schemes": schemes,
        "source": "curated_verified",
    }
