"""
Database connection utilities for the ServiceDesk API.
"""
import psycopg


def get_connection():
    """Create and return a connection to the Servicedesk database"""
    return psycopg.connect(
        "dbname=servicedesk user=creativity"
    )