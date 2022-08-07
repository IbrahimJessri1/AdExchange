
from config.db import conn
from repositries import generics as gen
from .hashing import Hash
from fastapi import HTTPException, status

def get_all():
    return gen.get_many(conn.AdExchange.user, {})