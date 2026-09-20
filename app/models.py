"""
Pydentic schemas used to validate ServiceDesk API request data.
"""
from pydantic import BaseModel
from typing import Optional


class TicketCreate(BaseModel):
    """Schema for creating a new service desk ticket."""

    title: str
    description: str
    priority: str
    requester: str


class TicketUpdate(BaseModel):
    status: Optional[str] = None    
    priority: Optional[str] = None   