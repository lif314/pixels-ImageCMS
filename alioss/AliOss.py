import oss2
import datetime
import uuid


class AliOss:
    def __init__(self):
        # 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
        self.auth = oss2.Auth('LTAI5t6Sa6Z2fXFigPLcBYe6', 'EcMOd2Q4mFiUWCqC128XxZHjZugL1V')
        # yourEndpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
        self.endpoint = 'oss-cn-shanghai.aliyuncs.com'
        # 填写Bucket名称，例如examplebucket。
        self.bucket_name = 'pixels-dis'
        # 填写Bucket名称。
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)

    def upload_file(self, data):
        # with open(filePath, 'rb') as f:
        #     data = f.read()
        today = datetime.datetime.today()
        key = str(today.year) + '-' + str(today.month) + '-' + str(today.day) + "/" + str(uuid.uuid4()).split('-')[0] + ".png"
        self.bucket.put_object(key, data)
        return str(self.bucket.sign_url('GET', key, 60 * 60 * 24)).split('?')[0]

if __name__ == '__main__':
    oss = AliOss()
    url = oss.upload_file('./panda.jpg')
    print(url)