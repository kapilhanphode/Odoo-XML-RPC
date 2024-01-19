from xmlrpc import client as xmlrpclib

url = 'http://localhost:9090/'  #user your local url or if you are running odoo on another system on same LAN
# you can use ip address like(http://192.168.10.55:9090 where 55 is ip address of system where odoo is running)

user = 'admin'                  #kapil - login user name
password = 'admin'              #1 - longin user password or you can use generated 'api key' instead of password
                                # (but from frontend it is not possible to login only from backend vai rpc)
db = 'test_071223'

#user authentication
common = xmlrpclib.ServerProxy(url+'xmlrpc/common')
user = common.login(db, user, password)
print(f'auth id is {user}')     #here you will get id of the user

#object
models = xmlrpclib.ServerProxy(url+'/xmlrpc/2/object')
res_partner = models.execute_kw(db, user, password, 'res.partner', 'search', [()])
print(res_partner)

#total count
res_partner_count = models.execute_kw(db, user, password, 'res.partner', 'search_count', [()])
print(res_partner_count)


ids = models.execute_kw(db, user, password, 'res.partner', 'read', [res_partner], {'fields': ['name', 'country_id', 'comment']})
print(ids)

#create record
create_id = models.execute_kw(db, user, password, 'res.partner', 'create', [{'name': "New Partner"}])
print(create_id)

#write/update record
write = models.execute_kw(db, user, password, 'res.partner', 'write', [[create_id], {'name': "Newer partner"}])
display_data = models.execute_kw(db, user, password, 'res.partner', 'read', [[create_id], ['display_name']])
print(write)
print(display_data)








# import requests
# import json
#
# url = "http://localhost:8080/web/webclient/version_info"
#
# payload = json.dumps({})
# headers = {
#   'Accept': 'application/json',
#   'Content-Type': 'application/json',
#   #'Cookie': 'session_id=b1a587e8743b95690f28c09f36bc1bc04d16851f'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
