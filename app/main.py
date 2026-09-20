"""
Main application entry point for the ServiceDesk API

Defines the FastAPI application and API endpoints.
"""

from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, status

from app.models import TicketCreate, TicketUpdate

app = FastAPI()

tickets = []


@app.get("/")
def root():
    """Return a simple health response to confirm the API is running"""
    return {"message": "ServiceDesk API is running"}


@app.post("/tickets", status_code=status.HTTP_201_CREATED)
def create_ticket(ticket: TicketCreate):
    new_ticket = {
        "id": uuid4(),
        "title": ticket.title,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": "open",
        "requester": ticket.requester,
    }

    tickets.append(new_ticket)

    return new_ticket


@app.get("/tickets", status_code=status.HTTP_200_OK)
def get_tickets():
    return tickets


@app.get("/tickets/{ticket_id}", status_code=status.HTTP_200_OK)
def get_ticket_by_id(ticket_id: UUID):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ticket not found",
    )


@app.patch("/tickets/{ticket_id}", status_code=status.HTTP_200_OK)
def patch_existing_ticket(ticket_id: UUID, ticket: TicketUpdate):
    for existing_ticket in tickets:
        if existing_ticket["id"] == ticket_id:
            if ticket.status is not None:
                existing_ticket["status"] = ticket.status

            if ticket.priority is not None:
                existing_ticket["priority"] = ticket.priority

            return existing_ticket
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Ticket not found",
    )
