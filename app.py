from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.sparta


# HTML 화면 보여주기
@app.route('/')
def homepage():
    return render_template('index.html')


# 작성하기 API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    content_receive = request.form['content_give']

    doc = {'name': name_receive, 'content': content_receive}
    db.order.insert_one(doc)
    return jsonify({'msg': '작성완료'})


# 목록보기 API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.order.find({}, {'_id': False}))
    return jsonify({'all_order_txt': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
