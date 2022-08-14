from pymongo import MongoClient
from repositries import generics as gen
conn = MongoClient("mongodb://localhost:27017/AdExchange")


user_collection = conn.AdExchange.user

dsp_collection = conn.AdExchange.dsp


role_permission_collection = conn.AdExchange.role_permission


# user_collection.insert_one({"username" : "admin1", "password" : "$2b$12$5F6O6qRHCQ25n3EnE4W9Iu3WctIP3Ahug.Z3PPkydvq.enkcn/YTi", "role" : "admin"})


