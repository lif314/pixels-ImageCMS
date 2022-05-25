import pymysql.cursors


# 数据库操作
class PixelsDb():
    def __init__(self):
        # 连接数据库，创建连接对象connection
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='pixels_cms',
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8'
        )
        # 创建光标对象，一个连接可以有很多光标，一个光标跟踪一种数据状态。
        # 光标对象作用是：、创建、删除、写入、查询等等
        self.cur = self.connection.cursor()  # 返回字典类型数据

    # 新增用户
    def insert_user(self, name, passwd):
        sql = "INSERT INTO `user`(`name`, `password`) VALUES (%s, %s)"
        try:
            self.cur.execute(sql, (name, passwd))
            self.connection.commit()  # 提交执行
        except:
            self.connection.rollback()  # 回滚

    # 获取用户信息
    def get_user_byid(self, id):
        sql = 'SELECT * FROM  user where id=(%s)'
        try:
            self.cur.execute(sql, (id))
            return self.cur.fetchone()
        except:
            self.connection.rollback()  # 回滚

    # 查询所有用户
    def list_users(self):
        sql = 'SELECT * FROM user'
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()  # 接受全部返回行
        except:
            return "Error: unable to fetch data"

    # 插入图片信息
    def insert_pic(self, url, owner_id, owner_name, note, tags, score):
        # 类型全部都是%s
        sql = "INSERT INTO picture(`url`, `owner_id`, `owner_name`, `note`, `tags`, `score`) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            # print(sql)
            self.cur.execute(sql, (url, owner_id, owner_name, note, tags, score))
            self.connection.commit()  # 提交执行
        except:
            self.connection.rollback()  # 回滚

    # 查询图片详细信息
    def get_pic_byid(self, id):
        sql = 'SELECT * FROM  picture where id=(%s)'
        try:
            self.cur.execute(sql, (id))
            return self.cur.fetchone()
        except:
            self.connection.rollback()  # 回滚

    # 根据标签模糊查询，在tags中存在tag的数据，按照score进行排序
    def get_pic_recommend(self, tag):
        sql = "SELECT * FROM `picture` WHERE LOCATE(%s, `tags`) ORDER BY score DESC"
        try:
            self.cur.execute(sql, (tag))
            return self.cur.fetchall()
        except:
            self.connection.rollback()  # 回滚

    # 根据关键词模糊查询，在tags中存在tag的数据，按照score进行排序
    def get_pic_keyword(self, keyword):
        sql = "SELECT * FROM `picture` WHERE LOCATE(%s, `tags`) ORDER BY score DESC"
        try:
            self.cur.execute(sql, (keyword))
            return self.cur.fetchall()
        except:
            self.connection.rollback()  # 回滚

    def get_all_pics(self):
        sql = "SELECT * FROM `picture`"
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()  # 接受全部返回行
        except:
            return "Error: unable to fetch data"

    # 获取用户收藏的图片集
    def get_user_collect(self, userId):
        sql = "SELECT p.`id`, p.`url`,p.`owner_id`,p.`owner_name`,p.`tags`,p.`score` FROM `picture` AS p LEFT JOIN `collect` ON p.id=collect.image_id WHERE user_id=(%s)"
        try:
            self.cur.execute(sql, (userId))
            return self.cur.fetchall()  # 接受全部返回行
        except:
            return "Error: unable to fetch data"

    # 收藏图片
    def collect_image(self, userId, imageId):
        # 类型全部都是%s
        sql = "INSERT INTO collect(`user_id`, `image_id`) VALUES (%s, %s)"
        try:
            # print(sql)
            self.cur.execute(sql, (userId, imageId))
            self.connection.commit()  # 提交执行
        except:
            self.connection.rollback()  # 回滚

    # 取消收藏
    def cancel_collect_image(self, userId, imageId):
        # 类型全部都是%s
        sql = "DELETE FROM `collect` WHERE user_id=(%s) AND image_id=(%s)"
        try:
            # print(sql)
            self.cur.execute(sql, (userId, imageId))
            self.connection.commit()  # 提交执行
        except:
            self.connection.rollback()  # 回滚

    # 析构函数，关闭数据库
    def __del__(self):
        self.connection.close()
        self.cur.close()


if __name__ == '__main__':
    db = PixelsDb()
    # db.insert_user('Adam Boost', '111111')
    # res = db.list_users()
    # print(res)

    # 插入一张图片信息
    # db.insert_pic("http://pixels-dis.oss-cn-shanghai.aliyuncs.com/2022-5-23%2F8c47569c.png", 4, "llf", "people,dog,cat", "cat",
    #               90.12)
    # res = db.get_user_byid(4)
    res = db.get_pic_recommend('people')
    print(res)
