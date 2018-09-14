import sys
import pyodbc

sys.path.insert(0, "..")
import logging
import time
from opcua import Client
from opcua import ua



class SubHandler(object):
    """
    Client to subscription. It will receive events from server
    """

    def datachange_notification(self, node, val, data):
        print(str(node)[25:-2],"value=",val)
        #save to database
        Server = '127.0.0.1'  # 本機
        Database = 'Python_test'  # 資料庫名稱
        username = 'sa'  # 使用者
        password = 'Opc.net'  # 密碼
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=" + Server + ";"
                                                   "Database=" + Database + ";"
                                                                            "uid=" + username + ";pwd=" + password + "")

        cursor = cnxn.cursor()
        cursor.execute("insert into [Python_test].[dbo].[Tag](Name,Value,Quality,Time) values("+"'"+str(node)[25:-2]+"'"","+str(val)+",'Good',"+time.strftime("%Y-%m-%d", time.localtime())+')')
        cnxn.commit()
        # 抓該資料表的全部資料
        #print("insert into Tag(Name,Value,Quality,Time) values("+str(node)[25:-2]+","+str(val)+",Good,"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+')')
'''
    def event_notification(self, event):
        print()
'''

#SubHandler Over



if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)
    client = Client("opc.tcp://127.0.0.1:49320")

    try:
        client.connect()
        root = client.get_root_node()
        objects = client.get_objects_node()   #之後用該objects取得寫入的Tag

        tag1 = client.get_node("ns=2;s=Channel1.Device1.Tag1") #Read用
        #write begin
        var = objects.get_child(["2:Channel1", "2:Device1", "2:Tag2"])  #get_chird +[path]
        #使用ua，必須先import ua / code: "from opcua import ua"
        dv = ua.DataValue(ua.Variant(7878, ua.VariantType.UInt16))  #宣告dv 指定為ua的DataValue，並指定數值以及資料型態
        var.set_value(dv) #write tag  = set_value(經由ua轉換得到的數值/型態)
        #write end
        handler = SubHandler()
        sub = client.create_subscription(1000, handler)
        handle1 = sub.subscribe_data_change(tag1)


        from IPython import embed

        embed()
        sub.unsubscribe(handle1)
        # sub.unsubscribe(handle2)
        sub.delete()
    finally:
        client.disconnect()

