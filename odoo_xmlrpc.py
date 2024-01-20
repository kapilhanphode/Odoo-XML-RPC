from xmlrpc import client as xmlrpclib

url = 'http://localhost:9090/'  #user your local url or if you are running odoo on another system on same LAN
# you can use ip address like(http://192.168.10.55:9090 where 55 is ip address of system where odoo is running)

user = 'admin'                  #kapil - login user name
password = 'admin'              #1 - longin user password or you can use generated 'api key' instead of password
                                # (but from frontend it is not possible to login only from backend vai rpc)
db = 'test_071223'		#name of the database

#user authentication
common = xmlrpclib.ServerProxy(url+'xmlrpc/common')
user = common.login(db, user, password)
print(f'auth id is {user}')     #here you will get id of the user

#object 
models = xmlrpclib.ServerProxy(url+'/xmlrpc/2/object')
res_partner = models.execute_kw(db, user, password, 'res.partner', 'search', [()])
print(res_partner)
#-------------------------------------------------------------------------------------------------------------------------------
#total count of res.partner in odoo using xml-rpc
res_partner_count = models.execute_kw(db, user, password, 'res.partner', 'search_count', [()])
print(res_partner_count)
#-------------------------------------------------------------------------------------------------------------------------------
#get id and other fields data such as 'name','country_id','comment' which are defined in 'fields'
ids = models.execute_kw(db, user, password, 'res.partner', 'read', [res_partner], {'fields': ['name', 'country_id', 'comment']})
print(ids)
#-------------------------------------------------------------------------------------------------------------------------------
#create record in odoo using xml-rpc
create_id = models.execute_kw(db, user, password, 'res.partner', 'create', [{'name': "New Partner"}])
print(create_id)
#-------------------------------------------------------------------------------------------------------------------------------
#write/update record in odoo using xml-rpc
write = models.execute_kw(db, user, password, 'res.partner', 'write', [[create_id], {'name': "Newer partner"}])
display_data = models.execute_kw(db, user, password, 'res.partner', 'read', [[create_id], ['display_name']])
print(write)
print(display_data)
#-------------------------------------------------------------------------------------------------------------------------------
#custom method in odoo using xml-rpc
custom_model = models.execute(db, uid, password, 'customer.customer', 'test1', []) #where customer.customer is custome model and 'test1' is custom method present in same model
print('custom_model',custom_model)

#write below method in your custom model-customer.customer
def test1(self):
	obj = self.env['res.partner'].search_read([])
	print('obj',obj)
	return obj
#-------------------------------------------------------------------------------------------------------------------------------
#calling sql query in odoo using xml-rpc
sql_query = models.execute(db, uid, password, 'customer.customer', 'sql_query', [], 'select * from res_partner')
print('sql_query',sql_query)

#write below method in your custom model-customer.customer
def sql_query(self,query, allow_none=True):
    self.env.cr.execute(query)
    data = self.env.cr.fetchall()
    print('data',data)
    return data
#-------------------------------------------------------------------------------------------------------------------------------
#calling sql query in odoo using xml-rpc with the help of custom method
custom_model1 = models.execute(db, uid, password, 'customer.customer', 'test2', [])

#write below code in your custom model-customer.customer
def test2(self):
    data = self.sql_query('select * from res_partner')
    return data

def sql_query(self,query, allow_none=True):
    self.env.cr.execute(query)
    data = self.env.cr.fetchall()
    print('data',data)
    return data








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
