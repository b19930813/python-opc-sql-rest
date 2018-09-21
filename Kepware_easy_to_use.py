import sys

sys.path.insert(0, "..")
from opcua import Client
from opcua import ua

global_UA_URL = None

def setting_UA_URL(UA_URL):
    global global_UA_URL
    global_UA_URL = UA_URL
    return global_UA_URL

def connect():
    try:
        #setting_UA_URL("opc.tcp://127.0.0.1:49320")
        global global_UA_URL
        client = Client(global_UA_URL)
        client.connect()
        return client
    except:
        print("Connect to OPC Server Error, Please check URL is correct or not")


def write(tag,value):
    channel_name,device_name,tag_name =  tag.split('.')

    objects = connect().get_objects_node()  # 之後用該objects取得寫入的Tag
    var = objects.get_child(["2:"+channel_name, "2:"+device_name, "2:"+tag_name])  # get_chird +[path]
    # 使用ua，必須先import ua / code: "from opcua import ua"
    dv = ua.DataValue(ua.Variant(value, ua.VariantType.UInt16))  # 宣告dv 指定為ua的DataValue，並指定數值以及資料型態
    var.set_value(dv)  # write tag  = set_value(經由ua轉換得到的數值/型態)'''




setting_UA_URL("opc.tcp://127.0.0.1:49320")
write("Channel1.Device1.Tag4",6000)

