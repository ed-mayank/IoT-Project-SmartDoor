from onem2m import *

uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
container_rel_path="/Permission_Details/Notification/cin_712" #give the relative path of container which you want to delete

delete_ae(uri_cse+container_rel_path)
