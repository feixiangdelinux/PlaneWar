# 想要连接mongo数据库首先要打开mongo服务，在命令行输入一下命令
# mongod --dbpath D:\Software\MongoDB\data
# 使用pymongo模块连接mongoDB数据库
from pymongo import MongoClient
import time

#

#
# for item in collection.find():
#     print(item)
# # print(collection.find_one())
#
#
#
# # # 删除集合collection中的所有数据
# # collection.remove()
# # 删除集合collection
# collection.drop()

class mongo_Helper:
    # 建立MongoDB数据库连接
    client = MongoClient('localhost', 27017)

    # 连接所需数据库,planedb为数据库名
    mydb = client["planedb"]

    # 连接所用集合，也就是我们通常所说的表，test为表名
    mycol = mydb["war"]
    def __init__(self):
        pass

    # 往数据库中插入一条数据
    def insert_data(self,user_db_info):
        mongo_Helper.mycol.insert_one({"user_name": user_db_info.user_name, "start_time": user_db_info.start_time, "end_time": user_db_info.end_time, "user_core": user_db_info.user_core})
    # 删除数据库中所有的数据
    def remove_all(self):
        mongo_Helper.mycol.drop()

    # 获取数据库中所有的数据
    def get_all(self):
        return mongo_Helper.mycol.find()

    def select(self):
        # x=mongo_Helper.mycol.insert_one({"user_name":"用户1","user_core":22})
        # x=mongo_Helper.mycol.insert_one({"user_name":"用户1","user_core":19})
        for item in mongo_Helper.mycol.find():
            print(item)

        print('调用成功')


