"""
Pydantic schemas used to validate ServiceDesk API request data.
"""

from pydantic import BaseModel


class TicketCreate(BaseModel):
    """Schema for creating a new service desk ticket."""

    title: str
    description: str
    priority: str
    requester: str


class TicketUpdate(BaseModel):
    status: str | None = None    
    priority: str | None = None   