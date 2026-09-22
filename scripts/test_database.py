from app.database import get_connection

# ticket_id = uuid4()

# title = "Cannot upload files"
# description = "Cannot upload files to the company server"
# priority = "high"
# status = "open"
# requester = "test@test.no"

# with get_connection() as connection, connection.cursor() as cursor:
#     cursor.execute(
#         "INSERT INTO tickets (id, title, description, priority, status, requester)"
#         "VALUES (%s, %s, %s, %s, %s, %s)",
#         (
#             ticket_id,
#             title,
#             description,
#             priority,
#             status,
#             requester,
#         ),
#     )
ticket_id = "7bc39a89-a817-4120-8aaf-4955e6715304"

with get_connection() as connection, connection.cursor() as cursor:
    cursor.execute(
       "DELETE FROM tickets WHERE id = %s",
       (ticket_id,)
    )


   