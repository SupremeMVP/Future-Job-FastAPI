from typing import Optional, List

from pydantic import BaseModel


class JobItem(BaseModel):
    key: Optional[str] = None
    title: str
    level: str
    remote: bool
    contract: bool
    fte: bool
    location: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    hourly_low: Optional[float] = None
    hourly_high: Optional[float] = None
    base_low: Optional[float] = None
    base_high: Optional[float] = None
    bonus_low: Optional[float] = None
    bonus_high: Optional[float] = None
    equity_low: Optional[float] = None
    equity_high: Optional[float] = None
    health_benefits: Optional[bool] = None
    retirement_benefits: Optional[bool] = None
    overtime: Optional[bool] = None
    company: str