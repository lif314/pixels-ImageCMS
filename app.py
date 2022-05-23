from flask import Flask
from AliOSS import AliOss

app = Flask(__name__)

aliOss = AliOss.AliOss()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# 上传图片
@app.route("/image/upload")
def upload_file(img):
    url = aliOss.upload_file(img)
    print(url)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
