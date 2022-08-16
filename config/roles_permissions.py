
#collection = conn.AdServer.role_permission
from config.db import role_permission_collection
from repositries import generics as gen

admin_permission = ["get_user", "self_update_user", "self_get_user"]

#collection.insert_one(
{
    "role" : "admin",
    "permissions" :admin_permission
}
#)


dsp_permission = ["self_update_account_dsp", "self_get_dsp"]

# role_permission_collection.insert_one(
# {
#     "role" : "dsp",
#     "permissions" :dsp_permission
# }
# )


gen.update_one(role_permission_collection, {"role" : "dsp"}, {"$set" : {"permissions" : dsp_permission}})
gen.update_one(role_permission_collection, {"role" : "admin"}, {"$set" : {"permissions" : admin_permission}})


#)



###add admin
# admin = User(username='admin1', password=hashing.Hash.bcrypt('123'), role='admin', create_date=str(datetime.datetime.now()))
# conn.AdServer.user.delete_many({"role" : 'admin'})
# conn.AdServer.user.insert_one(dict(admin))


