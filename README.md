# ServiceDesk API

A small REST API built with Python and FastAPI.

This project is a hands-on practice project focused on building REST APIs and developing fluency through repetition.
The project is intentionally kept small so the same API patterns can be practiced repeatedly.

## Purpose

The purpose of this project is to repeatedly practice the fundamentals of REST API development in a realistic service-desk scenario.

The API represents a simple internal IT service-desk system where employees can create and manage support tickets.

This is a learning project, not a production service-desk application.


## Technology

- Python
- FastAPI
- Pydantic
- Uvicorn
- pytest


## REST API Concepts Practiced

- HTTP methods
- REST resources
- API routing
- Request and response bodies
- JSON
- Path parameters
- UUID identifiers
- HTTP status codes
- Input validation
- Error handling
- CRUD operations
- Business rules
- API testing


## Ticket Resource

A ticket represents an issue or request submitted to an internal service desk.

Example:

```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "VPN connection not working",
    "description": "Unable to connect to the company VPN.",
    "priority": "high",
    "status": "open",
    "requester": "employee@example.no"
}
```


## API Endpoints

The API will gradually support the following operations:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/tickets` | Create a ticket |
| `GET` | `/tickets` | Retrieve all tickets |
| `GET` | `/tickets/{ticket_id}` | Retrieve a specific ticket |
| `PATCH` | `/tickets/{ticket_id}` | Update a ticket |
| `DELETE` | `/tickets/{ticket_id}` | Delete a ticket |