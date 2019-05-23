import json
import pymysql

# 数据库连接
db = pymysql.Connect(host='127.0.0.1',port=3306, user='root', password='123456', database='python1807tpp', charset='utf8')
# 游标
cursor = db.cursor()

# 打开文件，读取文件数据
with open('city.json', 'r') as f:
    # 加载json
    city_collection = json.load(f)

    # 数据源
    returnValue = city_collection['returnValue']

    # 获取所有的key
    letters = returnValue.keys()

    # 遍历操作
    for letter in letters:
        # 存入数据库 letter
        db.begin()
        # INSERT INTO letter(name) VALUES(letter)
        cursor.execute("INSERT INTO letter(name) VALUES('{}')".format(letter))
        db.commit()

        # 获取字母对应的城市
        cities = returnValue[letter]

        # 获取该字母对应的id 【插入城市数据时，需要指定是属于哪个字母 id】
        db.begin()
        # SELECT * FROM letter WHERE name=letter
        cursor.execute("SELECT * FROM letter WHERE name='{}'".format(letter))
        db.commit()

        # 取出字母对应的id
        letter_result = cursor.fetchone()
        letter_id = letter_result[0]

        # 遍历该字母对应的城市
        for city in cities:
            print(city)
            db.begin()
            # INSERT INTO city(id,cityCode, pinYin,regionName,c_letter) VALUES()
            cursor.execute("INSERT INTO city(id,cityCode, pinYin,regionName,c_letter) VALUES('{}','{}','{}','{}','{}')".format(city['id'],city['cityCode'], city['pinYin'], city['regionName'], letter_id))
            db.commit()
