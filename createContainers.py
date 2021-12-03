from onem2m import *
uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name"
ae = "Permission_Details"
cnt = "Data"
descriptor_cnt = "Descriptor"
Enter_AE="Door_Accessed"

create_ae(uri_cse,ae) # application entity
create_ae(uri_cse,Enter_AE)

uri_ae=uri_cse+"/"+ae
Enter_ae=uri_cse+"/"+Enter_AE
create_cnt(uri_ae,cnt)  #data container
create_cnt(uri_ae,descriptor_cnt) #descriptor container
create_cnt(uri_ae,"Notification")
create_cnt(Enter_ae,cnt)

uri_cnt=uri_ae+"/"+cnt
# des_cnt=uri_ae+"/"+descriptor_cnt
# notif_cnt=uri_ae+"/Notification"
create_data_cin(uri_cnt,"100") #data
# create_data_cin(des_cnt,"Name,Password") #description
# create_data_cin(notif_cnt,"N");

