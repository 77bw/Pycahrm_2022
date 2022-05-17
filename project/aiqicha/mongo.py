
import pymongo
from bson import ObjectId
from gridfs import GridFS


class MongoClient( object ):

    def __init__(self, ip, db=None, port="27017"):
        """构造函数"""
        self.client = pymongo.MongoClient("mongodb://" + ip + ":" + port)
        self.db = self.client[db]

    def close( self ):
        self.client.close()

    def count( self, collection, condition: dict ):
        """统计出现的次数 查询文档数目"""
        return self.db[collection].count_documents( condition )

    def insert_one( self, collection, data ):
        """
        插入一条记录 接收字典对象插入
        :param collection:  集合
        :param data: 数据
        :return: 插入记录id
        """
        ret = self.db[collection].insert_one( data )
        return ret.inserted_id

    def insert_many( self, collection, data ):
        """
        插入多条记录 接收文档列表（可迭代即可），返回InsertManyResult对象，其insert_ids属性表示插入多个文档的_id，可使用for循环迭代
        :param collection: 集合
        :param data: 数据
        :return: 插入记录id
        """
        ret = self.db[collection].insert_many( data )
        return ret.inserted_ids

    def update_one(self, collection, condition: dict, data):
        """更新一条记录 如果查找到的匹配数据多于一条，则只会修改第一条。
        :param collection: 集合
        :param condition:  查询的条件  { "alexa": "10000" }
        :param data:   要修改的字段   { "alexa": "12345" }
        :return:  返回修改的次数
        """
        return self.db[collection].update_one( condition, { "$set": data } ).modified_count

    def update( self, collection, condition: dict, data ):
        """
        更新所有记录  修改所有匹配到的记录
        :param collection: 集合
        :param condition: 过滤条件
        :param data: 要修改的字段
        :return: 更新数量
        """
        return self.db[collection].update_many( condition, { "$set": data } ).modified_count

    def find_one( self, collection, condition, sort = None ):
        """
        :param collection:  集合
        :param condition:  查询的条件
        :param column:
        :param sort:find()后追加sort(字段，排序方式)进行排序，传入排序使用的字段及排序方式
        - pymongo.ASCENDING表示升序排序
        - pymongo.DESCENDING表示降序排序
        sort([
            ("borough", pymongo.ASCENDING),
            ("zipcode", pymongo.ASCENDING)
        ])
        :return: 查询结果
        """
        cursor = self.db[collection].find_one( condition, sort = sort )
        return cursor

    def find( self, collection, *args, **kwargs ):
        """
        col.find({"hometown": "蒙古"})  # 等值查询
        col.find({"age": {"$gt": 18}})  # 比较运算符
        col.find({"hometown": "蒙古", "age": {"$gt": 18}})  # and条件
        col.find({"$or": [{"hometown": "蒙古"}, {"age": 18}]})  # or条件
        查询  查询集合中的所有数据
        :param collection: 集合
        :param condition: 查询条件
        :param column: 返回结果列
        :return: 查询结果
        """
        cursor= self.db[collection].find(*args, **kwargs )
        return cursor

    def delete_one(self, collection, filter, collation=None, hint=None, session=None):
        """删除一条记录"""
        return self.db[collection].delete_one(filter, collation, hint, session)

    def delete( self, collection, condition ):
        """  delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据
        删除所有文档：delete_many({})：查询条件为空即可
        删除记录
        :param collection: 集合
        :param condition: 过滤条件
        :return: 删除数量
        """
        return self.db[collection].delete_many( condition ).deleted_count

    def distinct( self, collection, column ):
        """
        返回指定字段的所有不同值
        @param collection: 集合
        @param column: 列名/字段名    "name"就可以查询字段name的不同值
        @return:
        """
        return self.db[collection].distinct(key = column)


    def get_file_md5( self, _id, collection ):
        gridfs_col = GridFS( self.db, collection )
        file = gridfs_col.get( _id )
        if file:
            return { '_id': file._id, 'md5': file.md5 }
        else:
            return None

    def upload_file_to_gridfs( self, collection, file_name, _id, content_type, file_data, metadata: dict = None ):
        """
        上传文件到gridfs

        :param collection: 集合
        :param file_name: 文件名
        :param _id: 关联id
        :param content_type: 文件类型，即文件扩展名
        :param file_data: 文件
        :param metadata: meta描述
        :return:
        """
        if metadata is None:
            metadata = { }
        default_metadata = {
            "_contentType": content_type,
            "isThumb": 'true',
            "targetId": _id,
            "_class": "com.ccr.dc.admin.mongo.MongoFsMetaData"
        }

        meta = { **default_metadata, **metadata }

        gridfs_col = GridFS( self.db, collection )
        id = gridfs_col.put( data = file_data, content_type = content_type, filename = file_name, metadata = meta )
        md5 = self.get_file_md5( id, collection )['md5']
        image_url = "/file/find/{}/{}".format( str( id ), md5 )
        return id, image_url

    def __del__( self ):
        self.client.close()

    def read_file_from_gridfs( self, collection, _id ):
        """
        从文件桶中读取文件

        :param collection: 集合
        :param _id: 文件id
        :return:
        """
        grid = GridFS( self.db, collection = collection )
        return grid.find_one( { '_id': ObjectId( _id ) } ).read()

    def get_filename( self, collection, _id ):
        """
        获取文件桶中文件名

        :param collection: 集合
        :param _id: id
        :return: 带扩展名的文件名称
        """
        grid = GridFS( self.db, collection = collection )
        fs = grid.find_one( { '_id': ObjectId( _id ) } )
        return fs.filename + '.' + fs.contentType

    def get_file_with_name( self, collection, _id ):
        """
        读取文件桶中文件，同时返回文件名

        :param collection: 集合
        :param _id: id
        :return:带扩展名的文件名称，文件
        """
        grid = GridFS( self.db, collection = collection )
        fs = grid.find_one( { '_id': ObjectId( id ) } )
        return fs.filename + '.' + fs.contentType, fs.read()


if __name__ == '__main__':
    mongo = MongoClient(ip='localhost',db='gm')
    data = [
                {
                    "regStatus": "存续",
                    "estiblishTime": 1374681600000,
                    "regCapital": "0万人民币",
                    "name": "北京百度网讯科技有限公司南京分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/010c44218af9a39e745a400850b48af0.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 139573097,
                    "category": "724",
                    "personType": 1,
                    "legalPersonName": "赵坤",
                    "base": "js"
                },
                {
                    "regStatus": "注销",
                    "estiblishTime": 1336406400000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司哈尔滨分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/5ed7edde6ac52f84fed757e78a23c49f.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 1615756664,
                    "category": "642",
                    "personType": 1,
                    "legalPersonName": "向海龙",
                    "base": "hlj"
                },
                {
                    "regStatus": "注销",
                    "estiblishTime": 1330617600000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司西安分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/1e21bc076c4f1629d8de5be85fd0e2cb.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 1566690935,
                    "category": "659",
                    "personType": 1,
                    "legalPersonName": "向海龙",
                    "base": "snx"
                },
                {
                    "regStatus": "注销",
                    "estiblishTime": 1326211200000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司重庆分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/53b97676f92b3ea6b7f37babdfbea680.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 412551136,
                    "category": "653",
                    "personType": 1,
                    "legalPersonName": "向海龙",
                    "base": "cq"
                },
                {
                    "regStatus": "在业",
                    "estiblishTime": 1211212800000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司广州分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/e94da5a7b0bb926632ac585766028e6f.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 139572971,
                    "category": "653",
                    "personType": 1,
                    "legalPersonName": "沈抖",
                    "base": "gd"
                },
                {
                    "regStatus": "在业",
                    "estiblishTime": 1210780800000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司东莞分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/762a5d7bd8f3a41a6ea39bbad6d946f0.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 139573020,
                    "category": "732",
                    "personType": 1,
                    "legalPersonName": "沈抖",
                    "base": "gd"
                },
                {
                    "regStatus": "存续",
                    "estiblishTime": 1209916800000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司上海分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/33c94402e09f1b2d027057f1ba61957f.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 711249800,
                    "category": "751",
                    "personType": 1,
                    "legalPersonName": "沈抖",
                    "base": "sh"
                },
                {
                    "regStatus": "注销",
                    "estiblishTime": 1209398400000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司佛山分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/809d933b2ef0d6392274daab2fa0c24d.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 2456357709,
                    "category": "642",
                    "personType": 1,
                    "legalPersonName": "刘计平",
                    "base": "gd"
                },
                {
                    "regStatus": "存续",
                    "estiblishTime": 1208448000000,
                    "regCapital": "",
                    "name": "北京百度网讯科技有限公司深圳分公司",
                    "logo": "https://img5.tianyancha.com/logo/lll/8e1aa6e84ff617657c2eeadae5b451f0.png@!f_200x200",
                    "alias": "北京百度",
                    "id": 139572921,
                    "category": "652",
                    "personType": 1,
                    "legalPersonName": "沈抖",
                    "base": "gd"
                }]

    # a=mongo.find('mongDB_gm',condition)
    a=mongo.insert_many(collection='mongDB_gm', data=data)
    for i in a:
        print(i)

    # condition={"name":"小明"}
    # a=mongo.count('mongDB_gm',condition)
    # print(a)
    # result=mongo.insert_many('mongDB_gm',data)
    # print(result)
    # for i in result:
    #     print(i)


