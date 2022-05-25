from alioss import AliOss
from flask_cors import CORS
from flask import Flask, jsonify, request
from collections import Counter
from werkzeug.utils import secure_filename
import os

from ImgClassificationService import image_classify
from MysqlDb import PixelsDb

app = Flask(__name__)
# 配置跨域
CORS(app, resources={r"/*": {"origins": "*"}})

# OSS 图片上传
aliOss = AliOss.AliOss()
# 保存在数据库中
pixelGb = PixelsDb()

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/login")
def hello_world():
    return "<p>Hello, World!</p>"


# 上传图片  将图片进行分类，将分类结果保存在数据库中
@app.route("/upload", methods=["POST"])
def upload_file():
    # 获取图像
    file = request.files.get("file")
    if file:
        # 上传到OSS
        # print(file.filename)
        # print(file)
        image_data = file.read()  # 一定要预先存储数据，否则read一次后就从缓存中清楚了，导致数据失效
        url = aliOss.upload_file(image_data)
        # print(file)
        # 图片分类,需要转换为二进制数据
        # print(image_data)
        res = image_classify(image_data)
        print("res\n", res)  # 预测前5个
        tags = res[0][0]
        score = res[0][1] * 100
        print(tags, score)
        # 保存在数据库中
        pixelGb.insert_pic(url=url, owner_id=5, owner_name="Adam Boost", note="pic", tags=tags, score=score)
        # 保存图片
        # filename = secure_filename(file.filename)
        # imagePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # file.save(imagePath)
        return jsonify({'data': 'success'})
    else:
        return jsonify({'data': 'error'})


# 查询所有的图片
@app.route("/images", methods=["GET"])
def get_all_images():
    res = pixelGb.get_all_pics()
    return jsonify({"data": res})


# 收藏图片
@app.route("/collect", methods=['GET'])
def collect_image():
    imageId = request.values.get("imageId")
    userId = request.values.get("userId")
    status = request.values.get("status")
    print(imageId, userId)
    if status == '1':  # 收藏
        pixelGb.collect_image(userId, imageId)
    elif status == '0':
        pixelGb.cancel_collect_image(userId, imageId)
    return jsonify({'data': 'success'})


# 获取用户所有的收藏
@app.route("/user/collect", methods=['GET'])
def get_user_collect():
    userId = request.values.get('userId')
    res = pixelGb.get_user_collect(userId)
    return jsonify({"data": res})


def count_tags():
    images = pixelGb.get_all_pics()
    tags = []
    for image in images:
        # print(image)
        tags.extend(image['tags'].split(", "))
    return Counter(tags)

# 预计算数据
tagDict = count_tags()
# print(tagDict)


# 获取所有的标签信息
# TODO 由于标签信息存储在数据库中，所以在返回图片信息时已经包含了标签信息
@app.route("/tags", methods=['GET'])
def get_tags():
    res = []
    for key in tagDict.keys():
        res.append({
            'label': key,
            'size': tagDict[key],
        })
    res.sort(key=lambda x: x['size'], reverse=True)
    return jsonify(res)


# 推荐图片信息  模糊查询数据库
@app.route("/recommend", methods=['GET'])
def get_top_k():
    keyword = request.values.get("keyword")
    res = pixelGb.get_pic_keyword(keyword)
    return jsonify({"data": res})


# 根据关键词进行搜索
@app.route("/search", methods=['GET'])
def search():
    keyword = request.values.get("keyword")
    res = pixelGb.get_pic_keyword(keyword)
    return jsonify({"data": res})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
