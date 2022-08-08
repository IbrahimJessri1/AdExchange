
from config.db import user_collection
from repositries import generics as gen
from .hashing import Hash
from fastapi import HTTPException, status

def get_all():
    return gen.get_many(user_collection, {})