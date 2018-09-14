from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pyodbc

Server = '127.0.0.1'  #本機
Database = 'Python_test' #資料庫名稱
username = 'sa'  #使用者
password = 'Opc.net' #密碼
table_name = 'kepware_4' #資料表
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};" 
                      "Server="+Server+";"
                      "Database="+Database+";"
                      "uid="+username+";pwd="+password+"")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM [Python_test].[dbo].[Tag]')

#抓該資料表的全部資料
for data in cursor:
    print( data[0],data[1],data[2],data[3])