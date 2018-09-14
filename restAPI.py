from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pyodbc
import json
#using Flask frame to create Rest Server
app = Flask(__name__)
api = Api(app)


Server = '127.0.0.1'
Database = 'Python_test'
username = 'sa'
password = 'Opc.net'
table_name = 'kepware_4'
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" 
                      "Server="+Server+";"
                      "Database="+Database+";"
                      "uid="+username+";pwd="+password+"")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM [Python_test].[dbo].[Tag]')

DATAS = []
#get data from data and array with json
for data in cursor:
    DATAS.append({'id':str(data[0]).strip(),'name':str(data[1]).strip(),'value':str(data[2]).strip(),'quality':str(data[3]).strip()})



def abort_if_data_doesnt_exist(data_id):
    if data_id not in DATAS:
        abort(404, message="Data {} doesn't exist".format(data_id))


parser = reqparse.RequestParser()
parser.add_argument('task')

#setting Rest method/ get /put / delete
class Data(Resource):
    def get(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        return DATAS[data_id]

    def delete(self, data_id):
        abort_if_data_doesnt_exist(data_id)
        del DATAS[data_id]
        return '', 204

    def put(self, data_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        DATAS[data_id] = task
        return task, 201

#setting Rest Method : get/post; get=>all data
class DataList(Resource):
    def get(self):
        return DATAS

    def post(self):
        args = parser.parse_args()
        data_id = int(max(DATAS.keys()).lstrip('todo')) + 1
        data_id = 'data%i' % data_id
        DATAS[data_id] = {'task': args['task']}
        return DATAS[data_id], 201



api.add_resource(DataList, '/datas')
api.add_resource(Data, '/datas/<data_id>')

if __name__ == '__main__':
    app.run(host="192.168.0.204", port=5000, debug=True)