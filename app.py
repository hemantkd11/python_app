from flask import Flask , request
from uuid import uuid4
import pyodbc
from db import items
app = Flask(__name__)




# query to connect with database in written below
# class ItemDatabase:
#     def __init__(self):
#         self.conn = pyodbc.connect('Driver={SQL Server};'
#                                    'Server=kavita;'
#                                    'Database=Py_Test;'
#                                    'Trusted_Connection=yes;')
#         self.cursor = self.conn.cursor()






# @app.get('/get-data')
# def get_data():
#    return {"data":data}



items = {
    "2a620d9971af447fb19182013ae41df0":{ 
                        "name":"hemant",
                        "age":22
                        },
     "2bd71ce562224bc991811994e78e3db9":{
                        "name":"diwakar",
                        "age":23
                        }
}


 # http://127.0.0.1:5000/get-item

@app.get('/get-items') 
def get_items():
    return {"items": items}



# @app.get('/get-item/<string:name>') 
# def get_item(name):
#     for item in items:
#         if name == item['name']:
#             return item
#         return{'maessage':'Record not found'}
 

 ###### get item method
"""@app.get('/get-item') 
def get_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
            return item
        return{'maessage':'Record not found'}, 404 """

#### get item methon with unique key
@app.get('/get-item') 
def get_item():
    id = request.args.get('id')
    try:
        return items[id]
    except KeyError:
        return{'maessage':'Record not found'}, 404
    
      
@app.post('/add-item') 
def add_item():
    items[uuid4().hex]=request.get_json()
    return {'message':'item added succesfully'},201



# @app.post('/add-item')
# def add_item():
#     request_data = request.get_json()
#     for item in items:
#         if item['name'] == request_data['name']:
#             return{'message':'name already exist'}
#     items.append(request_data)
#     return{'message':'added successfully'}

# @app.post('/add-item')
# def add_item():
#     request_data = request.get_json()
#     for item in items:
#        if request_data['name']  not in items[item]:
#            items.append(request_data)
#            return{'message':'item added successfully'}
#        return{'message':'user already exist'}
           

# @app.post('/add-item')
# def add_item():
#     request_data = request.get_json()
#     for item in items:
#         if request_data not in item:
#             items.append(request_data)
#             return{'message':'item added successfully'}
#     return{'message':'item already exist'}
 


"""@app.put('/update-item') 
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name'] == request_data['name']:
            item['price'] = request_data['price']
            return{'message':'item updated successfully'}
        return {'message':'no record found'}, 404"""


@app.put('/update-item') 
def update_item():
    id = request.args.get('id')
    if id in items.keys():
       items[id] = request.get_json()
       return{'message':'item updated successfully'},200
    return {"message":"no recod found"},404
  


  


"""@app.delete('/delete-item') 
def delete_item():
    name = request.args.get('name')
    for item in items:
        if name == item['name']:
            items.remove(item)
            return {'message':'item deleted successfully'}
    return{'maessage':'Record not found'}, 404"""

@app.delete('/delete-item') 
def delete_item():
    id = request.args.get('id')
    if id in items.keys():
        del items[id]
        return {'message':'item deleted successfully'}
    return{'maessage':'Record not found'}, 404