from pymongo import MongoClient
from repositries import generics as gen
conn = MongoClient("mongodb://localhost:27017/AdExchange")


user_collection = conn.AdExchange.user

dsp_collection = conn.AdExchange.dsp


role_permission_collection = conn.AdExchange.role_permission



